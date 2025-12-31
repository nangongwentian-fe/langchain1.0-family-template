# LangChain 1.0 Family（LangChain、LangGraph、LangSmith、DeepAgents）模板项目

## 项目简介

如果你计划使用LangChain框架开发Agent项目，本项目提供了一个最基本的LangChain全家桶项目模板，你可以基于这个模板进行快速开发，无需自己从头搭建项目。

## 快速开始

1. 安装项目依赖
   > 如果本机没有uv，请前往[uv官网](https://docs.astral.sh/uv/getting-started/installation/)安装。
   ```bash
   uv sync
   ```
2. 配置环境变量
   > 请在项目根目录下创建一个 `.env` 文件，配置必要的环境变量，例如 `BYTE_DANCE_VOLCENGINE_LLM_API_KEY`、`ALI_BAILIAN_LLM_API_KEY`、`TAVILY_API_KEY`、`LANGSMITH_API_KEY` 等。
3. 体验最基本的Deep Research Agent
   > 请在项目根目录下运行 `notebooks/1.deep_research.ipynb` 体验最基本的Deep Research Agent。
   > （Tavily搜索工具需要🪜，记得本机开全局，否则会报错SSL）
4. 体验在 `LangSmith` 中调试Deep Research Agent
   1. 启动 `LangSmith` 
      ```bash
      langgraph dev
      ```
   2. 启动成功之后会自动打开浏览器并且打开 `LangSmith` 的调试界面。

## 目前已完成

- [x] 安装LangChain、LangGraph、LangSmith、DeepAgents等依赖，搭建最基本的LangChain全家桶项目模板。
- [x] 实现 `阿里百炼` 和 `火山引擎` 的模型接入，并且规划项目文件夹架构。
- [x] 实现DeepAgents的案例Agent `deep_research_agent`，基于Tavily搜索工具的研究代理。并且实现了最基本的体验脚本 `notebooks/1.deep_research.ipynb`。
- [x] 实现在 `LangSmith` 中调试 `deep_research_agent`。

## 待实现

- [ ] 实现基于 `LangChain` 的Agent案例
- [ ] 实现基于 `LangGraph` 的Agent案例