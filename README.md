# Dream_Archive——梦境存档

本项目旨在搭建一个平台，用来存储用户的梦境。

## 介绍

用户可以通过文字记录自己的梦境，该项目可以将用户的梦境转换为连续的图片或视频，并通过梦境分析用户的潜意识、周公解梦。在使用一段时间后，用户可以形成属于自己的与众不同的“梦境展览馆”。

## 项目结构

 /
    |-- app.py             # 应用主入口
    |-- requirements.txt   # 项目依赖
    |-- config.py          # 配置文件
    |-- .gitignore         # Git忽略文件
    |-- /app/              # 主应用目录
    |   |-- __init__.py      # 初始化应用
    |   |-- /models.py       # 数据库模型 (用户, 梦境)
    |   |-- /routes.py       # 路由 (API端点)
    |   |-- /services/       # 核心服务
    |   |   |-- __init__.py
    |   |   |-- image_service.py  # 梦境转图片/视频服务
    |   |   |-- analysis_service.py # 梦境分析服务
    |   |-- /static/         # 静态文件 (CSS, JS)
    |   |-- /templates/      # HTML模板
    |       |-- index.html
    |-- /tests/              # 测试用例
    |-- __init__.py
    |-- test_app.py
