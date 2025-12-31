# 🤝 贡献指南

感谢您对 LangChain 1.0 Family 模板项目的关注！我们欢迎所有形式的贡献，包括但不限于：

- 🐛 报告错误
- 💡 提出新功能建议
- 📝 改进文档
- 🔧 提交代码修复
- ✨ 开发新功能
- 🧪 编写测试用例

## 📋 目录

- [开发环境设置](#-开发环境设置)
- [贡献流程](#-贡献流程)
- [代码规范](#-代码规范)
- [提交规范](#-提交规范)
- [Pull Request 指南](#-pull-request-指南)
- [问题报告](#-问题报告)
- [文档贡献](#-文档贡献)

## 🛠️ 开发环境设置

### 前置要求

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Git
- 编辑器（推荐 VS Code + Python 插件）

### 设置步骤

1. **Fork 并克隆项目**
   ```bash
   git clone https://github.com/your-username/study-langchain.git
   cd study-langchain
   ```

2. **添加上游仓库**
   ```bash
   git remote add upstream https://github.com/original-owner/study-langchain.git
   ```

3. **创建开发环境**
   ```bash
   uv sync
   ```

4. **激活虚拟环境**
   ```bash
   source .venv/bin/activate  # Linux/Mac
   # 或
   .venv\Scripts\activate     # Windows
   ```

5. **安装开发依赖**
   ```bash
   uv sync --dev
   ```

6. **验证环境**
   ```bash
   python -m pytest
   python main.py
   ```

## 🔄 贡献流程

### 1. 创建分支

```bash
# 确保在最新的 main 分支
git checkout main
git pull upstream main

# 创建新分支（使用描述性名称）
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/your-bug-fix
# 或
git checkout -b docs/your-doc-update
```

### 2. 开发

- 遵循项目代码规范
- 添加必要的测试
- 更新相关文档
- 确保所有测试通过

### 3. 提交代码

```bash
# 添加文件
git add .

# 提交（遵循提交规范）
git commit -m "feat: add new model integration"

# 推送到你的 fork
git push origin feature/your-feature-name
```

### 4. 创建 Pull Request

- 在 GitHub 上创建 Pull Request
- 填写详细的 PR 描述
- 等待代码审查
- 根据反馈进行修改

## 📝 代码规范

### Python 代码风格

我们使用以下工具确保代码质量：

- **Black** - 代码格式化
- **Ruff** - 代码检查和格式化
- **mypy** - 类型检查

#### 格式化和检查

```bash
# 格式化代码
uv run black src/ tests/

# 代码检查
uv run ruff check src/ tests/

# 类型检查
uv run mypy src/
```

### 命名规范

| 类型 | 规范 | 示例 |
|------|------|------|
| 变量/函数 | snake_case | `user_name`, `get_data()` |
| 类 | PascalCase | `DeepResearchAgent` |
| 常量 | UPPER_SNAKE_CASE | `MAX_RETRIES` |
| 文件名 | snake_case | `deep_research_agent.py` |

### 文档字符串

使用 Google 风格的文档字符串：

```python
def create_agent(model_name: str, api_key: str) -> Agent:
    """创建一个新的 Agent 实例。
    
    Args:
        model_name: 模型名称
        api_key: API 密钥
        
    Returns:
        Agent: 配置好的 Agent 实例
        
    Raises:
        ValueError: 当 model_name 无效时
        
    Example:
        >>> agent = create_agent("gpt-4", "your-api-key")
        >>> isinstance(agent, Agent)
        True
    """
    pass
```

## 📋 提交规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

### 格式

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### 类型说明

| 类型 | 说明 |
|------|------|
| `feat` | 新功能 |
| `fix` | 错误修复 |
| `docs` | 文档更新 |
| `style` | 代码格式化 |
| `refactor` | 代码重构 |
| `test` | 测试相关 |
| `chore` | 构建过程或辅助工具的变动 |

### 示例

```bash
feat: add bytedance volcengine model support

- Implement ByteDanceVolcengineModel class
- Add configuration for volcengine API
- Update documentation with setup instructions

Closes #123
```

## 🔍 Pull Request 指南

### PR 标题

使用 Conventional Commits 格式：
- `feat: add new feature description`
- `fix: resolve issue description`
- `docs: update API documentation`

### PR 描述模板

```markdown
## 📝 变更描述
简要描述这个 PR 的目的和主要变更。

## 🔄 变更类型
- [ ] 新功能
- [ ] 错误修复
- [ ] 文档更新
- [ ] 重构
- [ ] 其他

## ✅ 检查清单
- [ ] 代码遵循项目规范
- [ ] 添加了必要的测试
- [ ] 测试全部通过
- [ ] 更新了相关文档
- [ ] 没有破坏现有功能

## 📸 截图（如适用）
添加截图来说明变更。

## 🔗 相关 Issue
Closes #(issue number)
```

### 审查流程

1. **自动检查** - CI/CD 流水线自动运行测试
2. **代码审查** - 维护者进行代码审查
3. **反馈修改** - 根据反馈进行修改
4. **合并** - 审查通过后合并到主分支

## 🐛 问题报告

### 报告 Bug

使用以下模板报告 bug：

```markdown
## 🐛 Bug 描述
简要描述遇到的问题。

## 🔄 复现步骤
1. 执行步骤 1
2. 执行步骤 2
3. 观察到错误

## 🎯 期望行为
描述期望的正确行为。

## 📱 环境信息
- OS: [例如 macOS 14.0]
- Python 版本: [例如 3.12.0]
- 项目版本: [例如 0.1.0]

## 📎 附加信息
添加错误日志、截图等信息。
```

### 功能请求

```markdown
## 💡 功能描述
描述希望添加的新功能。

## 🎯 使用场景
说明为什么需要这个功能以及使用场景。

## 📋 实现建议（可选）
如果有想法，可以提供实现建议。

## 🔗 相关资源
相关链接、参考资料等。
```

## 📚 文档贡献

### 文档类型

- **README.md** - 项目主文档
- **API 文档** - 代码中的文档字符串
- **教程** - 详细的使用教程
- **示例代码** - 代码示例

### 贡献方式

1. **改进现有文档**
   - 修正错误
   - 提高可读性
   - 更新过时信息

2. **添加新文档**
   - 新功能使用指南
   - 最佳实践
   - 常见问题解答

3. **翻译文档**
   - 中英文互译
   - 其他语言版本

## 🏆 贡献者认可

所有贡献者都会在项目中得到认可：

### 贡献者列表

在 README.md 中添加贡献者：

```markdown
## 🙏 贡献者

感谢所有为这个项目做出贡献的开发者！

- [@username](https://github.com/username) - 贡献描述
```

### 贡献统计

我们使用 GitHub 的贡献统计来跟踪所有贡献：
- 代码提交
- Pull Request
- Issue 报告和讨论
- 文档改进

## 📞 联系方式

如果您有任何问题或需要帮助：

- 📧 邮件: your-email@example.com
- 💬 GitHub Discussions: [讨论区](https://github.com/your-repo/discussions)
- 🐛 Issues: [问题追踪](https://github.com/your-repo/issues)

## 📄 许可证

通过贡献代码，您同意您的贡献将在 [MIT 许可证](LICENSE) 下发布。

---

再次感谢您的贡献！🎉