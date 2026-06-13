# 安全策略 / Security Policy

## 我们的承诺 / Our Commitment

AI Pulse 将用户隐私和数据安全作为最高优先。本项目设计原则之一是「数据永不出户」—— 一切运行在本地，无任何外部数据传输。

AI Pulse treats user privacy and data security as the highest priority. One of our core design principles is "data never leaves your machine" — everything runs locally with zero external data transmission.

## 安全特性 / Security Features

| 特性 | 说明 |
|------|------|
| 🏠 **纯本地运行** | 所有操作在用户本机完成，采集的新闻数据仅写入本地 HTML 文件 |
| 🔌 **零外部请求** | 生成的 HTML 页面没有任何外部 API 调用、无埋点、无遥测、无广告 |
| 🔑 **无需 API 密钥** | 不需要任何第三方服务 Token，仅使用 Claude Code 内置的 WebSearch/WebFetch |
| 📂 **仅操作项目目录** | 所有文件读写仅限于项目文件夹内（`index.html`、`archive/`、`.claude/`） |
| 👁️ **完全开源透明** | MIT 协议，100% 代码可审计，无后门、无混淆 |
| 🔒 **只读网络访问** | Claude Code 仅执行搜索和抓取操作，不上传任何本地文件或个人信息 |
| 🚫 **无遥测追踪** | 不接入任何统计、分析或用户行为追踪服务 |
| 📱 **离线可浏览** | 生成的 HTML 可在完全断网环境下浏览（仅首次需加载系统字体，字体亦为本地） |

## 信任边界 / Trust Boundary

```
用户本地机器 (User's Local Machine)
┌────────────────────────────────────────────┐
│  Claude Code (运行时)                       │
│  ├─ WebSearch ──→ 公网 (只读搜索)           │
│  ├─ WebFetch  ──→ 公网 (只读抓取)           │
│  └─ 文件写入 ──→ 项目目录 (仅 index.html + archive/) │
│                                              │
│  无出站数据 (No outbound data):              │
│  ✗ 不上传文件                               │
│  ✗ 不发送遥测                               │
│  ✗ 不收集个人信息                            │
│  ✗ 不需要登录/注册                           │
└────────────────────────────────────────────┘
```

## 依赖清单 / Dependency Inventory

| 依赖 | 类型 | 用途 |
|------|------|------|
| Claude Code | 运行时 | 唯一的运行依赖，提供搜索/抓取/生成能力 |
| 浏览器 | 查看器 | 任意现代浏览器打开 `index.html` |
| Git | 可选 | 用于克隆项目 |

**零 npm 包、零 Python 库、零外部 API、零云服务。**

## 报告漏洞 / Reporting a Vulnerability

如果你发现安全漏洞，请通过 GitHub Issues **私密报告**，勿公开披露。

If you discover a security vulnerability, please report it **privately** via GitHub Issues. Do not publicly disclose.

我们将在 48 小时内确认收到报告，并在 7 天内提供修复方案。

---

*最后更新：2026-06-14*
