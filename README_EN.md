# 🤖 LangChain 1.0 Family Template Project

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1.2.0+-green.svg)](https://python.langchain.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-1.0.3+-orange.svg)](https://langchain-ai.github.io/langgraph)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive **LangChain Family** (LangChain, LangGraph, LangSmith, DeepAgents) template project providing best practices for rapid intelligent Agent application development.

## ✨ Features

- 🚀 **Quick Start** - Out-of-the-box LangChain ecosystem configuration
- 🔧 **Multi-Model Support** - Integration with mainstream Chinese LLM services like Ali Bailian and ByteDance Volcengine
- 🛠️ **Development Tools** - Complete development, debugging, and monitoring toolchain
- 📚 **Example Projects** - Rich Agent implementation cases and tutorials
- 🌍 **Internationalization** - Bilingual documentation and community support

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Project Architecture](#-project-architecture)
- [Configuration](#-configuration)
- [Usage Guide](#-usage-guide)
- [API Documentation](#-api-documentation)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) - Recommended package manager

### Installation

1. **Clone the project**
   ```bash
   git clone <repository-url>
   cd study-langchain
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file and fill in necessary API Keys
   ```

4. **Verify installation**
   ```bash
   python main.py
   ```

## 🏗️ Project Architecture

```
study-langchain/
├── src/
│   ├── agents/          # Agent implementations
│   │   └── deep_research_agent.py
│   ├── models/          # Model integrations
│   │   ├── ali_bailian.py
│   │   └── bytedance_volcengine.py
│   ├── tools/           # Tool integrations
│   │   └── internet_search.py
│   └── prompts/         # Prompt templates
├── notebooks/           # Jupyter examples
│   └── 1.deep_research.ipynb
├── main.py              # Entry point
├── langgraph.json       # LangGraph configuration
└── README.md           # Project documentation
```

## ⚙️ Configuration

Configure the following environment variables in your `.env` file:

| Environment Variable | Description | Required |
|---------------------|-------------|----------|
| `BYTE_DANCE_VOLCENGINE_LLM_API_KEY` | ByteDance Volcengine API Key | ✅ |
| `ALI_BAILIAN_LLM_API_KEY` | Ali Bailian API Key | ✅ |
| `TAVILY_API_KEY` | Tavily Search API Key | ✅ |
| `LANGSMITH_API_KEY` | LangSmith monitoring Key | ⭕ |

## 📖 Usage Guide

### Deep Research Agent Example

1. **Jupyter Notebook Method**
   ```bash
   jupyter notebook notebooks/1.deep_research.ipynb
   ```

2. **LangSmith Debug Method**
   ```bash
   # Start LangGraph development server
   langgraph dev
   
   # Browser will automatically open LangSmith debug interface
   ```

### Custom Agent

```python
from src.agents.deep_research_agent import deep_research_agent
from src.models.ali_bailian import AliBailianModel

# Initialize model
model = AliBailianModel(api_key="your-api-key")

# Use Agent
result = deep_research_agent.invoke({
    "messages": [{"role": "user", "content": "Research latest AI technology trends"}]
})
```

## 📚 API Documentation

### Core Modules

#### Model Interfaces (`src/models/`)

- **AliBailianModel** - Ali Bailian Large Model Integration
- **ByteDanceVolcengineModel** - ByteDance Volcengine Large Model Integration

#### Tool Integrations (`src/tools/`)

- **InternetSearch** - Web search tool based on Tavily

#### Agent Implementations (`src/agents/`)

- **DeepResearchAgent** - Specialized deep research agent

## 🐛 Troubleshooting

### Common Issues

**Q: Tavily search SSL error**
```bash
# Solution: Ensure network proxy is working properly
export https_proxy=your-proxy-url
export http_proxy=your-proxy-url
```

**Q: LangSmith connection failed**
- Check if `LANGSMITH_API_KEY` is correct
- Ensure network connection is normal
- Verify `langgraph.json` configuration

**Q: Model call failed**
- Verify API Key validity
- Check model service status
- Confirm request format is correct

## 🤝 Contributing

We welcome all forms of contributions! Please check [CONTRIBUTING.md](CONTRIBUTING.md) for detailed information.

### Development Workflow

1. Fork the project
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Create Pull Request

## 📈 Project Status

### ✅ Completed Features

- [x] Complete LangChain ecosystem integration
- [x] Ali Bailian and ByteDance Volcengine model integration
- [x] Tavily search tool integration
- [x] Deep Research Agent implementation
- [x] LangSmith debugging support
- [x] Jupyter Notebook examples
- [x] Project documentation and configuration

### 🚧 In Progress

- [ ] More model provider support
- [x] Rich Agent examples

### 📅 Roadmap

- [ ] LangChain native Agent examples
- [ ] LangGraph workflow examples
- [ ] Performance monitoring and analytics
- [ ] Automated test coverage

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Thanks to the following open source projects:

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [DeepAgents](https://github.com/langchain-ai/deep-agents)

---

## 🌍 Internationalization

- **English Documentation** (Current)
- [中文文档](README.md)

## 📞 Contact Us

- 🐛 [Report Issues](https://github.com/your-repo/issues)
- 💬 [Discussions](https://github.com/your-repo/discussions)
- 📧 [Email Contact](mailto:your-email@example.com)