#!/usr/bin/env python3
"""
AI 新闻抓取脚本 - 多信源并行抓取
支持信源：量子位、36氪(RSS)、Solidot、雷锋网、钛媒体、IT之家、TechCrunch、The Verge、Ars Technica、Hacker News(API)、GitHub Trending、arXiv
"""

import urllib.request
import urllib.parse
import re
import json
import sys
import concurrent.futures
from datetime import datetime
from typing import List, Dict, Optional

sys.stdout.reconfigure(encoding='utf-8')

# 确保 stderr 也使用 UTF-8
import io
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


class NewsItem:
    """新闻条目"""
    def __init__(self, title: str, url: str, source: str, summary: str = "",
                 category: str = "general", timestamp: str = ""):
        self.title = title.strip()
        self.url = url
        self.source = source
        self.summary = summary
        self.category = category
        self.timestamp = timestamp
        self.score = 0

    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "url": self.url,
            "source": self.source,
            "summary": self.summary,
            "category": self.category,
            "timestamp": self.timestamp,
            "score": self.score
        }

    def __repr__(self):
        return f"[{self.source}] {self.title[:50]}..."


class BaseFetcher:
    """基础抓取器"""
    def __init__(self, name: str, url: str, timeout: int = 15):
        self.name = name
        self.url = url
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def fetch(self) -> str:
        """抓取网页内容"""
        try:
            req = urllib.request.Request(self.url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                return response.read().decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"[ERROR] {self.name}: {e}", file=sys.stderr)
            return ""

    def parse(self, html: str) -> List[NewsItem]:
        """解析 HTML，子类必须实现"""
        raise NotImplementedError

    def get_news(self) -> List[NewsItem]:
        """获取新闻列表"""
        html = self.fetch()
        if not html:
            return []
        return self.parse(html)


class QbitaiFetcher(BaseFetcher):
    """量子位抓取器"""
    def __init__(self):
        super().__init__("量子位", "https://www.qbitai.com")

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        pattern = r'<a[^>]*href="([^"]+)"[^>]*>([^<]{10,80})</a>'
        matches = re.findall(pattern, html)

        for link, title in matches:
            title = title.strip()
            if not title or len(title) < 15:
                continue
            ai_keywords = ['AI', '模型', '开源', 'GPT', 'Claude', 'DeepSeek', '谷歌',
                          '百度', '大模型', '智能', '算法', '机器人', '算力', '芯片',
                          '英伟达', 'Meta', 'OpenAI', 'Anthropic', 'LLM', 'Agent',
                          '训练', '推理', '多模态', '具身', '自动驾驶', '融资']
            if not any(kw in title for kw in ai_keywords):
                continue

            full_url = link if link.startswith('http') else f"https://www.qbitai.com{link}"
            items.append(NewsItem(
                title=title, url=full_url, source="量子位",
                category=self._categorize(title)
            ))

        return items[:10]

    def _categorize(self, title: str) -> str:
        if any(kw in title for kw in ['GPT', 'Claude', 'DeepSeek', 'LLM', '大模型', '基模']):
            return "model"
        elif any(kw in title for kw in ['开源', 'GitHub', '工具', '框架', '部署']):
            return "tool"
        elif any(kw in title for kw in ['融资', 'IPO', '收购', '投资']):
            return "industry"
        elif any(kw in title for kw in ['政策', '监管', '合规', '法律']):
            return "policy"
        elif any(kw in title for kw in ['机器人', '自动驾驶', '应用', '落地', '量产']):
            return "application"
        return "general"


class Kr36Fetcher(BaseFetcher):
    """36氪抓取器 - 使用 RSS"""
    def __init__(self):
        super().__init__("36氪", "https://36kr.com/feed")

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        # RSS 格式：先清理CDATA，再匹配
        # 36kr RSS格式: <title>...<![CDATA[...]]>...</title> 或 <title>...</title>
        # 先提取所有item块
        item_pattern = r'<item>(.*?)</item>'
        item_matches = re.findall(item_pattern, html, re.DOTALL)

        for item_html in item_matches:
            # 提取title
            title_match = re.search(r'<title>(.*?)</title>', item_html, re.DOTALL)
            if not title_match:
                continue
            title = title_match.group(1).strip()

            # 提取link
            link_match = re.search(r'<link>(.*?)</link>', item_html, re.DOTALL)
            if not link_match:
                continue
            link = link_match.group(1).strip()

            # 清理CDATA
            title = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', title)
            link = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', link)
            title = title.strip()
            link = link.strip()

            if not title or len(title) < 15:
                continue

            ai_keywords = ['AI', '模型', '开源', 'GPT', '大模型', '智能', '算法',
                          '机器人', '算力', '芯片', '英伟达', 'Meta', 'OpenAI',
                          'Anthropic', 'DeepSeek', '字节', '阿里', '腾讯', '百度',
                          '融资', 'IPO', '自动驾驶', '具身']
            if not any(kw in title for kw in ai_keywords):
                continue

            items.append(NewsItem(
                title=title, url=link, source="36氪",
                category=self._categorize(title)
            ))

        return items[:8]

    def _categorize(self, title: str) -> str:
        if any(kw in title for kw in ['GPT', 'Claude', 'DeepSeek', 'LLM', '大模型']):
            return "model"
        elif any(kw in title for kw in ['开源', '工具', '框架']):
            return "tool"
        elif any(kw in title for kw in ['融资', 'IPO', '投资']):
            return "industry"
        elif any(kw in title for kw in ['政策', '监管', '合规']):
            return "policy"
        elif any(kw in title for kw in ['机器人', '自动驾驶', '应用']):
            return "application"
        return "general"


class SolidotFetcher(BaseFetcher):
    """Solidot 抓取器"""
    def __init__(self):
        super().__init__("Solidot", "https://www.solidot.org")

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        pattern = r'<a[^>]*href="([^"]+)"[^>]*>([^<]{10,80})</a>'
        matches = re.findall(pattern, html)

        for link, title in matches:
            title = title.strip()
            if not title or len(title) < 15:
                continue
            ai_keywords = ['AI', '人工智能', '模型', '算法', '机器人', '芯片',
                          '算力', '自动驾驶', '智能', '科技', 'GPT', 'Claude',
                          'DeepSeek', 'OpenAI', 'Anthropic', 'LLM', '机器学习']
            if not any(kw in title for kw in ai_keywords):
                continue

            full_url = link if link.startswith('http') else f"https://www.solidot.org{link}"
            items.append(NewsItem(
                title=title, url=full_url, source="Solidot",
                category="general"
            ))

        return items[:8]


class LeiphoneFetcher(BaseFetcher):
    """雷锋网抓取器"""
    def __init__(self):
        super().__init__("雷锋网", "https://www.leiphone.com")

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        patterns = [
            r'<a[^>]*href="([^"]+)"[^>]*title="([^"]{10,80})"[^>]*>',
            r'<a[^>]*href="([^"]+)"[^>]*>([^<]{10,80})</a>',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, html)
            for match in matches:
                if len(match) == 2:
                    link, title = match
                else:
                    continue

                title = title.strip()
                if not title or len(title) < 15:
                    continue

                ai_keywords = ['AI', '人工智能', '模型', '算法', '机器人', '芯片',
                              '算力', '自动驾驶', '智能', '科技', 'GPT', 'Claude',
                              'DeepSeek', '具身', '大模型', '开源']
                if not any(kw in title for kw in ai_keywords):
                    continue

                full_url = link if link.startswith('http') else f"https://www.leiphone.com{link}"
                items.append(NewsItem(
                    title=title, url=full_url, source="雷锋网",
                    category="general"
                ))

        # 去重
        seen = set()
        unique = []
        for item in items:
            if item.title not in seen:
                seen.add(item.title)
                unique.append(item)

        return unique[:6]


class TmtpostFetcher(BaseFetcher):
    """钛媒体抓取器"""
    def __init__(self):
        super().__init__("钛媒体", "https://www.tmtpost.com")

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        pattern = r'<a[^>]*href="([^"]+)"[^>]*>([^<]{10,80})</a>'
        matches = re.findall(pattern, html)

        for link, title in matches:
            title = title.strip()
            if not title or len(title) < 15:
                continue

            ai_keywords = ['AI', '人工智能', '模型', '算法', '机器人', '芯片',
                          '算力', '自动驾驶', '智能', '科技', 'GPT', '大模型',
                          '开源', '融资', 'IPO']
            if not any(kw in title for kw in ai_keywords):
                continue

            full_url = link if link.startswith('http') else f"https://www.tmtpost.com{link}"
            items.append(NewsItem(
                title=title, url=full_url, source="钛媒体",
                category="general"
            ))

        return items[:6]


class IthomeFetcher(BaseFetcher):
    """IT之家抓取器"""
    def __init__(self):
        super().__init__("IT之家", "https://www.ithome.com")

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        # IT之家标题结构
        patterns = [
            r'<a[^>]*href="([^"]+)"[^>]*title="([^"]{10,80})"[^>]*>',
            r'<a[^>]*href="([^"]+)"[^>]*>([^<]{10,80})</a>',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, html)
            for match in matches:
                if len(match) == 2:
                    link, title = match
                else:
                    continue

                title = title.strip()
                if not title or len(title) < 15:
                    continue

                ai_keywords = ['AI', '人工智能', '模型', '算法', '机器人', '芯片',
                              '算力', '自动驾驶', '智能', '科技', 'GPT', '大模型',
                              '开源', '微软', '谷歌', '苹果']
                if not any(kw in title for kw in ai_keywords):
                    continue

                full_url = link if link.startswith('http') else f"https://www.ithome.com{link}"
                items.append(NewsItem(
                    title=title, url=full_url, source="IT之家",
                    category="general"
                ))

        # 去重
        seen = set()
        unique = []
        for item in items:
            if item.title not in seen:
                seen.add(item.title)
                unique.append(item)

        return unique[:6]


class TechCrunchFetcher(BaseFetcher):
    """TechCrunch 抓取器"""
    def __init__(self):
        super().__init__("TechCrunch", "https://techcrunch.com/category/artificial-intelligence/")

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        pattern = r'<a[^>]*href="([^"]+)"[^>]*>([^<]{10,100})</a>'
        matches = re.findall(pattern, html)

        for link, title in matches:
            title = title.strip()
            if not title or len(title) < 20:
                continue

            ai_keywords = ['AI', 'artificial intelligence', 'model', 'GPT', 'Claude',
                          'OpenAI', 'Anthropic', 'Google', 'Microsoft', 'Meta',
                          'LLM', 'machine learning', 'neural', 'robot', 'automation']
            if not any(kw.lower() in title.lower() for kw in ai_keywords):
                continue

            # 过滤导航链接
            if any(kw in link for kw in ['/category/', '/page/', '/author/', '/tag/']):
                continue

            full_url = link if link.startswith('http') else f"https://techcrunch.com{link}"
            items.append(NewsItem(
                title=title, url=full_url, source="TechCrunch",
                category="global"
            ))

        return items[:6]


class TheVergeFetcher(BaseFetcher):
    """The Verge 抓取器"""
    def __init__(self):
        super().__init__("The Verge", "https://www.theverge.com/ai-artificial-intelligence")
        self.timeout = 20  # The Verge 需要更长的超时时间

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        pattern = r'<a[^>]*href="([^"]+)"[^>]*>([^<]{10,100})</a>'
        matches = re.findall(pattern, html)

        for link, title in matches:
            title = title.strip()
            if not title or len(title) < 20:
                continue

            ai_keywords = ['AI', 'artificial intelligence', 'ChatGPT', 'Claude',
                          'Google', 'OpenAI', 'Anthropic', 'model', 'algorithm']
            if not any(kw.lower() in title.lower() for kw in ai_keywords):
                continue

            # 过滤导航链接
            if any(kw in link for kw in ['/category/', '/page/', '/author/', '/tag/']):
                continue

            full_url = link if link.startswith('http') else f"https://www.theverge.com{link}"
            items.append(NewsItem(
                title=title, url=full_url, source="The Verge",
                category="global"
            ))

        return items[:5]


class ArsTechnicaFetcher(BaseFetcher):
    """Ars Technica 抓取器"""
    def __init__(self):
        super().__init__("Ars Technica", "https://arstechnica.com/tag/ai/")

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        pattern = r'<a[^>]*href="([^"]+)"[^>]*>([^<]{10,100})</a>'
        matches = re.findall(pattern, html)

        for link, title in matches:
            title = title.strip()
            if not title or len(title) < 20:
                continue

            ai_keywords = ['AI', 'artificial intelligence', 'machine learning',
                          'neural', 'model', 'algorithm', 'GPT', 'ChatGPT']
            if not any(kw.lower() in title.lower() for kw in ai_keywords):
                continue

            # 过滤导航链接
            if any(kw in link for kw in ['/category/', '/page/', '/author/', '/tag/']):
                continue

            full_url = link if link.startswith('http') else f"https://arstechnica.com{link}"
            items.append(NewsItem(
                title=title, url=full_url, source="Ars Technica",
                category="global"
            ))

        return items[:5]


class GitHubTrendingFetcher(BaseFetcher):
    """GitHub Trending 抓取器"""
    def __init__(self):
        super().__init__("GitHub Trending", "https://github.com/trending?l=python&since=daily")

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        # GitHub trending 项目
        pattern = r'<h2[^>]*>.*?<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>.*?</h2>'
        matches = re.findall(pattern, html, re.DOTALL)

        for link, name in matches:
            # 清理 HTML 标签
            name = re.sub(r'<[^>]+>', '', name).strip()
            if not name or len(name) < 3:
                continue
            # 过滤非 AI 项目
            ai_keywords = ['ai', 'ml', 'llm', 'gpt', 'model', 'neural', 'deep', 'machine',
                          'agent', 'chat', 'diffusion', 'transformer', 'embedding']
            if not any(kw in name.lower() for kw in ai_keywords):
                continue

            full_url = f"https://github.com{link}" if not link.startswith('http') else link
            items.append(NewsItem(
                title=f"GitHub Trending: {name}",
                url=full_url,
                source="GitHub Trending",
                category="opensource"
            ))

        return items[:10]


class ArxivFetcher(BaseFetcher):
    """arXiv 论文抓取器"""
    def __init__(self):
        super().__init__("arXiv", "http://export.arxiv.org/api/query")
        self.timeout = 30  # arXiv 可能需要更长时间

    def fetch(self) -> str:
        """使用 arXiv API 获取最新 AI 论文"""
        try:
            query = "search_query=cat:cs.AI+OR+cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=10"
            url = f"{self.url}?{query}"
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                return response.read().decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"[ERROR] {self.name}: {e}", file=sys.stderr)
            return ""

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        try:
            # 提取论文条目
            entries = re.findall(r'<entry>(.*?)</entry>', html, re.DOTALL)

            for entry in entries:
                # 提取标题
                title_match = re.search(r'<title>([^<]+)</title>', entry)
                if not title_match:
                    continue
                title = title_match.group(1).strip()

                # 提取链接
                link_match = re.search(r'<id>([^<]+)</id>', entry)
                url = link_match.group(1).strip() if link_match else ""

                # 提取摘要
                summary_match = re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL)
                summary = summary_match.group(1).strip()[:200] if summary_match else ""

                if not title or len(title) < 10:
                    continue

                items.append(NewsItem(
                    title=title,
                    url=url,
                    source="arXiv",
                    summary=summary,
                    category="paper"
                ))
        except Exception as e:
            print(f"[ERROR] {self.name} parse: {e}", file=sys.stderr)

        return items[:5]


class HackerNewsFetcher(BaseFetcher):
    """Hacker News 抓取器 - 使用 Algolia API"""
    def __init__(self):
        super().__init__("Hacker News", "https://hn.algolia.com/api/v1/search_by_date")

    def fetch(self) -> str:
        """使用 Algolia API 获取 AI 相关新闻"""
        try:
            url = f"{self.url}?tags=story&query=AI&hitsPerPage=20"
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                return response.read().decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"[ERROR] {self.name}: {e}", file=sys.stderr)
            return ""

    def parse(self, html: str) -> List[NewsItem]:
        items = []
        try:
            data = json.loads(html)
            hits = data.get('hits', [])

            for hit in hits:
                title = hit.get('title', '').strip()
                url = hit.get('url', '')
                if not title or len(title) < 15:
                    continue
                if not url:
                    url = f"https://news.ycombinator.com/item?id={hit.get('objectID', '')}"

                ai_keywords = ['AI', 'machine learning', 'LLM', 'GPT', 'Claude',
                              'OpenAI', 'model', 'neural', 'algorithm', 'training',
                              'artificial intelligence']
                if not any(kw.lower() in title.lower() for kw in ai_keywords):
                    continue

                items.append(NewsItem(
                    title=title, url=url, source="Hacker News",
                    category="opensource"
                ))
        except Exception as e:
            print(f"[ERROR] {self.name} parse: {e}", file=sys.stderr)

        return items[:5]


class NewsAggregator:
    """新闻聚合器"""
    def __init__(self):
        self.fetchers = [
            QbitaiFetcher(),
            Kr36Fetcher(),
            SolidotFetcher(),
            LeiphoneFetcher(),
            TmtpostFetcher(),
            IthomeFetcher(),
            TechCrunchFetcher(),
            TheVergeFetcher(),
            ArsTechnicaFetcher(),
            HackerNewsFetcher(),
            GitHubTrendingFetcher(),
            ArxivFetcher(),
        ]

    def fetch_all(self, max_workers: int = 5) -> List[NewsItem]:
        """并行抓取所有信源"""
        all_news = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_fetcher = {
                executor.submit(f.get_news): f.name
                for f in self.fetchers
            }

            for future in concurrent.futures.as_completed(future_to_fetcher):
                name = future_to_fetcher[future]
                try:
                    news = future.result()
                    print(f"[OK] {name}: {len(news)} 条", file=sys.stderr)
                    all_news.extend(news)
                except Exception as e:
                    print(f"[ERROR] {name}: {e}", file=sys.stderr)

        return all_news

    def deduplicate(self, news: List[NewsItem]) -> List[NewsItem]:
        """去重：标题相似度 > 80% 视为重复"""
        unique = []
        seen_titles = []

        for item in news:
            is_duplicate = False
            for seen in seen_titles:
                if self._similarity(item.title, seen) > 0.8:
                    is_duplicate = True
                    break
            if not is_duplicate:
                seen_titles.append(item.title)
                unique.append(item)

        return unique

    def _similarity(self, a: str, b: str) -> float:
        """简单相似度计算"""
        a_set = set(a.lower())
        b_set = set(b.lower())
        if not a_set or not b_set:
            return 0.0
        intersection = len(a_set & b_set)
        union = len(a_set | b_set)
        return intersection / union if union > 0 else 0.0

    def score(self, news: List[NewsItem]) -> List[NewsItem]:
        """评分排序"""
        for item in news:
            score = 0
            # 来源质量
            quality_map = {
                "量子位": 3, "36氪": 3, "TechCrunch": 3,
                "Solidot": 2, "雷锋网": 2, "钛媒体": 2, "IT之家": 2,
                "The Verge": 3, "Ars Technica": 2, "Hacker News": 2
            }
            score += quality_map.get(item.source, 1) * 0.3

            # 热度信号
            hot_keywords = ['发布', '开源', '融资', 'IPO', '突破', '首发', '重磅']
            if any(kw in item.title for kw in hot_keywords):
                score += 3 * 0.4

            # 时效
            score += 2 * 0.3

            item.score = round(score, 2)

        return sorted(news, key=lambda x: x.score, reverse=True)

    def categorize(self, news: List[NewsItem]) -> Dict[str, List[NewsItem]]:
        """按板块分类"""
        categories = {
            "models": [],
            "tools": [],
            "policy": [],
            "applications": [],
            "opensource": [],
            "global": [],
            "papers": [],
            "general": []
        }

        for item in news:
            cat = item.category
            if cat == "model":
                categories["models"].append(item)
            elif cat == "tool":
                categories["tools"].append(item)
            elif cat == "policy":
                categories["policy"].append(item)
            elif cat == "application":
                categories["applications"].append(item)
            elif cat == "opensource":
                categories["opensource"].append(item)
            elif cat == "global":
                categories["global"].append(item)
            elif cat == "paper":
                categories["papers"].append(item)
            else:
                categories["general"].append(item)

        return categories

    def run(self) -> Dict:
        """完整流程"""
        print("=" * 50, file=sys.stderr)
        print("开始抓取 AI 新闻...", file=sys.stderr)
        print("=" * 50, file=sys.stderr)

        # 1. 抓取
        raw_news = self.fetch_all()
        print(f"\n原始抓取: {len(raw_news)} 条", file=sys.stderr)

        # 2. 去重
        unique_news = self.deduplicate(raw_news)
        print(f"去重后: {len(unique_news)} 条", file=sys.stderr)

        # 3. 评分
        scored_news = self.score(unique_news)

        # 4. 分类
        categorized = self.categorize(scored_news)

        # 输出统计
        print("\n=== 分类统计 ===", file=sys.stderr)
        for cat, items in categorized.items():
            print(f"  {cat}: {len(items)} 条", file=sys.stderr)

        return {
            "total": len(scored_news),
            "categories": {
                cat: [item.to_dict() for item in items[:10]]
                for cat, items in categorized.items()
            }
        }


def main():
    """主入口"""
    aggregator = NewsAggregator()
    result = aggregator.run()

    # 输出 JSON
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
