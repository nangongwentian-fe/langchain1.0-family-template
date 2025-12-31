# 🤖 LangChain 1.0 Family 模板项目

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1.2.0+-green.svg)](https://python.langchain.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-1.0.3+-orange.svg)](https://langchain-ai.github.io/langgraph)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个功能完备的 **LangChain 全家桶**（LangChain、LangGraph、LangSmith、DeepAgents）项目模板，为快速构建智能 Agent 应用提供最佳实践。

## ✨ 特性

- 🚀 **快速启动** - 开箱即用的 LangChain 生态系统配置
- 🔧 **多模型支持** - 集成阿里百炼、火山引擎等国内主流 LLM 服务
- 🛠️ **开发工具** - 完整的开发、调试、监控工具链
- 📚 **示例项目** - 丰富的 Agent 实现案例和教程
- 🌍 **国际化** - 中英文文档和社区支持

## 📋 目录

- [快速开始](#-快速开始)
- [项目架构](#-项目架构)
- [配置说明](#-配置说明)
- [使用指南](#-使用指南)
- [API 文档](#-api-文档)
- [故障排除](#-故障排除)
- [贡献指南](#-贡献指南)

## 🚀 快速开始

### 前置要求

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) - 推荐的包管理工具

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd study-langchain
   ```

2. **安装依赖**
   ```bash
   uv sync
   ```

3. **配置环境变量**
   ```bash
   cp .env.example .env
   # 编辑 .env 文件，填入必要的 API Keys
   ```

4. **验证安装**
   ```bash
   python main.py
   ```

## 🏗️ 项目架构

```
study-langchain/
├── src/
│   ├── agents/          # Agent 实现
│   │   └── deep_research_agent.py
│   ├── models/          # 模型集成
│   │   ├── ali_bailian.py
│   │   └── bytedance_volcengine.py
│   ├── tools/           # 工具集成
│   │   └── internet_search.py
│   └── prompts/         # 提示词模板
├── notebooks/           # Jupyter 示例
│   └── 1.deep_research.ipynb
├── main.py              # 入口文件
├── langgraph.json       # LangGraph 配置
└── README.md           # 项目文档
```

## ⚙️ 配置说明

在 `.env` 文件中配置以下环境变量：

| 环境变量 | 说明 | 必需 |
|---------|------|------|
| `BYTE_DANCE_VOLCENGINE_LLM_API_KEY` | 火山引擎 API Key | ✅ |
| `ALI_BAILIAN_LLM_API_KEY` | 阿里百炼 API Key | ✅ |
| `TAVILY_API_KEY` | Tavily 搜索 API Key | ✅ |
| `LANGSMITH_API_KEY` | LangSmith 监控 Key | ⭕ |

## 📖 使用指南

### Deep Research Agent 示例

1. **Jupyter Notebook 方式**
   ```bash
   jupyter notebook notebooks/1.deep_research.ipynb
   ```

2. **LangSmith 调试方式**
   ```bash
   # 启动 LangGraph 开发服务器
   langgraph dev
   
   # 浏览器会自动打开 LangSmith 调试界面
   ```

### 自定义 Agent

```python
from src.agents.deep_research_agent import deep_research_agent
from src.models.ali_bailian import AliBailianModel

# 初始化模型
model = AliBailianModel(api_key="your-api-key")

# 使用 Agent
result = deep_research_agent.invoke({
    "messages": [{"role": "user", "content": "研究最新的 AI 技术趋势"}]
})
```

## 📚 API 文档

### 核心模块

#### 模型接口 (`src/models/`)

- **AliBailianModel** - 阿里百炼大模型集成
- **ByteDanceVolcengineModel** - 火山引擎大模型集成

#### 工具集成 (`src/tools/`)

- **InternetSearch** - 基于 Tavily 的网络搜索工具

#### Agent 实现 (`src/agents/`)

- **DeepResearchAgent** - 深度研究专用 Agent

## 🐛 故障排除

### 常见问题

**Q: Tavily 搜索报 SSL 错误**
```bash
# 解决方案：确保网络代理正常工作
export https_proxy=your-proxy-url
export http_proxy=your-proxy-url
```

**Q: LangSmith 连接失败**
- 检查 `LANGSMITH_API_KEY` 是否正确
- 确认网络连接正常
- 验证 `langgraph.json` 配置

**Q: 模型调用失败**
- 验证 API Key 有效性
- 检查模型服务状态
- 确认请求格式正确

## 🤝 贡献指南

我们欢迎所有形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细信息。

### 开发流程

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📈 项目状态

### ✅ 已完成功能

- [x] LangChain 生态系统完整集成
- [x] 阿里百炼、火山引擎模型接入
- [x] Tavily 搜索工具集成
- [x] Deep Research Agent 实现
- [x] LangSmith 调试支持
- [x] Jupyter Notebook 示例
- [x] 项目文档和配置

### 🚧 进行中

- [ ] 更多模型提供商支持
- [ ] 丰富的 Agent 示例

### 📅 待开发

- [ ] LangChain 原生 Agent 示例
- [ ] LangGraph 工作流示例
- [ ] 性能监控和分析
- [ ] 自动化测试覆盖

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

感谢以下开源项目的支持：

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [DeepAgents](https://github.com/langchain-ai/deep-agents)

---

## 🌍 国际化

- [English Documentation](README_EN.md)
- [中文文档](README.md) (当前)

## 📞 联系我们

- 🐛 [报告问题](https://github.com/your-repo/issues)
- 💬 [讨论区](https://github.com/your-repo/discussions)
- 📧 [邮件联系](mailto:your-email@example.com)