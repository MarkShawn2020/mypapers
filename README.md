# MyPapers 论文一体化写作神器（Python）

### 项目框架
```text
.
└── mypapers
    ├── config          # 配置
    ├── crawl           # 数据爬虫
    ├── db              # 数据库
    ├── export          # 论文导出
    ├── plot            # 论文绘图
    ├── stats           # 统计模型
    ├── templates       # 论文模板
    └── utils           # 高级/辅助
```

### 项目说明
该项目致力于为科研论文的写作提供一个集成的环境，
使用本项目您可以便捷地完成论文框架的奠定、论文数据的获取、
论文模型的生成、修改和复现以及论文的word/latex导出，
我们预期该项目最终能为您提高50%的生产效率。

该项目将首先以金融领域的计量论文的书写为起点，
集成或二度开发Python的一些第三方包，
以达到部分甚至完全取代专业的计量软件，如Sas、Stata等。

该项目将对网络数据采集提供最大程度地友好支持，
将内嵌Selenium、Scrapy等数据采集工具，
并集成Sqlite、MySQL等多种数据库。

### TODO
- [ ] 集成多套基于MarkDown的论文模板
- [ ] 集成StatsModel等计量包
- [ ] 集成JupyterNotebook等环境
- [ ] 集成Docx、Latex等导出媒介