<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:atom="http://www.w3.org/2005/Atom">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>

<xsl:template match="/rss/channel">
  <html lang="zh-CN">
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title><xsl:value-of select="title"/> — RSS 订阅</title>
    <style>
      * { margin:0; padding:0; box-sizing:border-box; }
      body { font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif; background: #0a0a0f; color: #f5f5f7; padding: 40px 20px 80px; max-width: 700px; margin: 0 auto; }
      h1 { font-size: 28px; font-weight: 300; letter-spacing: -0.02em; margin-bottom: 4px; }
      .sub { font-size: 13px; color: #86868b; margin-bottom: 12px; }
      .actions { display: flex; gap: 10px; flex-wrap: wrap; margin: 20px 0 32px; }
      .btn { display: inline-flex; align-items: center; gap: 6px; padding: 8px 18px; border-radius: 8px; font-size: 13px; font-weight: 500; text-decoration: none; transition: opacity 0.2s; }
      .btn:hover { opacity: 0.85; }
      .btn-feed { background: #f26522; color: #fff; }
      .btn-site { background: rgba(99,102,241,0.2); color: #a5b4fc; border: 1px solid rgba(99,102,241,0.3); }
      .btn-copy { background: rgba(255,255,255,0.06); color: #9898a0; border: 1px solid rgba(255,255,255,0.08); cursor: pointer; font-family: inherit; }
      .item { background: rgba(255,255,255,0.02); border: 0.5px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 20px 22px; margin-bottom: 10px; transition: border-color 0.2s; }
      .item:hover { border-color: rgba(255,255,255,0.12); }
      .item-title { font-size: 17px; font-weight: 500; color: #f5f5f7; margin-bottom: 6px; }
      .item-title a { color: inherit; text-decoration: none; }
      .item-title a:hover { color: #818cf8; }
      .item-date { font-size: 11px; color: #86868b; margin-bottom: 10px; }
      .item-desc { font-size: 12px; color: #9898a0; line-height: 1.6; }
      .item-desc ul { padding-left: 16px; margin: 4px 0; }
      .item-desc li { margin-bottom: 2px; }
      .footer { margin-top: 40px; padding-top: 16px; border-top: 0.5px solid rgba(255,255,255,0.06); font-size: 11px; color: #86868b; }
    </style>
    <script>
      function copyURL() {
        navigator.clipboard.writeText(window.location.href).then(() => {
          var b = document.getElementById('copyBtn');
          b.textContent = '✓ 已复制';
          setTimeout(() => { b.textContent = '📋 复制订阅链接'; }, 1500);
        });
      }
    </script>
  </head>
  <body>
    <h1><xsl:value-of select="title"/></h1>
    <p class="sub"><xsl:value-of select="description"/></p>
    <div class="actions">
      <a class="btn btn-site" href="{link}">&#127760; 打开主页</a>
      <a class="btn btn-feed" href="{//atom:link/@href}">&#128276; 用 RSS 阅读器订阅</a>
      <button class="btn btn-copy" id="copyBtn" onclick="copyURL()">&#128203; 复制订阅链接</button>
    </div>

    <xsl:for-each select="item">
      <div class="item">
        <div class="item-title">
          <a href="{link}"><xsl:value-of select="title"/></a>
        </div>
        <div class="item-date"><xsl:value-of select="pubDate"/></div>
        <div class="item-desc"><xsl:value-of select="description" disable-output-escaping="yes"/></div>
      </div>
    </xsl:for-each>

    <div class="footer">
      <p>共 <xsl:value-of select="count(item)"/> 期 · 每天 08:00 / 12:00 / 20:00 更新 · <a href="{link}" style="color:#6366f1;">AI 脉搏</a></p>
    </div>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>
