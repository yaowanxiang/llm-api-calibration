# LLM API Calibration Tool

> **统一API与订阅版的体验差异** - 解决API"降智"问题的通用方案

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 🎯 核心问题

**同一模型,API调用体验不如订阅版?**

这不是模型能力差异,而是配置与工具链的差异:

| 差异维度 | 订阅版(官网) | API版(开发者) |
|---------|-------------|---------------|
| **系统提示** | 官方精心调优 | 用户自写或缺失 |
| **生成参数** | 对话场景优化 | 默认值保守 |
| **工具能力** | 自动联网/解析 | 需手动实现 |
| **上下文管理** | 自动记忆 | 手动管理 |

## ✨ 核心功能

### 1. 智能提示工程

自动生成接近订阅版体验的系统提示,基于泄露的官方提示词结构优化。

### 2. 场景化配置

针对不同使用场景(学术写作/代码审查/数据分析/日常对话)提供定制化配置。

### 3. 工具链模拟

轻量级工具调用框架,模拟Web版的自动搜索能力。

### 4. 版本兼容性

自动检测并适配新版本API的参数变化。

## 📦 安装

### 方式1: 从源码安装

```bash
git clone https://github.com/yaowanxiang/llm-api-calibration.git
cd llm-api-calibration
pip install -e .
```

### 方式2: PyPI安装(发布后)

```bash
pip install llm-api-calibration
```

### 开发安装

```bash
pip install -e ".[dev]"
```

## 🚀 快速开始

```python
from llm_api_calibration import APICalibrator

# 初始化校准器
calibrator = APICalibrator(
    api_key="your-api-key",  # 替换为你的Anthropic API密钥
    model="claude-3-5-sonnet-20240620"
)

# 方式1: 基础学术写作
response = calibrator.call_with_calibration(
    prompt="写一段关于深度学习在医学影像应用的研究综述",
    config=calibrator.get_recommended_config(
        scenario="research_writing",
        language="chinese"
    )
)
print(response)

# 方式2: 模拟Web版(含自动搜索)
response = calibrator.call_web_simulation(
    prompt="分析2024年Claude模型的发展趋势",
    scenario="research_writing"
)
print(response)
```

## 📊 支持的场景

| 场景 | 说明 | max_tokens | 特殊能力 |
|-----|------|-----------|---------|
| `research_writing` | 学术写作 | 4096 | LaTeX生成/BibTeX引用/顶会规范 |
| `code_review` | 代码审查 | 2048 | Bug识别/性能优化/安全检查 |
| `data_analysis` | 数据分析 | 3072 | 统计检验/可视化/LaTeX表格 |
| `daily_chat` | 日常对话 | 1024 | 自然交流/亲和力/上下文记忆 |

## 🧪 测试

```bash
# 运行单元测试
pytest

# 运行测试并查看覆盖率
pytest --cov=llm_api_calibration
```

## 📚 文档

- [API参考](docs/api_reference.md)
- [最佳实践](docs/best_practices.md)
- [贡献指南](CONTRIBUTING.md)

## 🔬 技术原理

本项目基于对Claude Web版的深入分析:

1. **系统提示词结构**: 参考泄露的官方提示词(3,826行代码)
2. **参数废弃**: 新版本已废弃temperature/top_p,主要靠提示词控制
3. **工具链设计**: 模拟Web版的自动搜索、文档解析能力
4. **模块化架构**: 根据场景动态加载不同的提示模块

详细原理见[技术文档](docs/technical_details.md)

## 🤝 贡献

欢迎提交Issue和Pull Request! 参见[贡献指南](CONTRIBUTING.md)。

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 🙏 致谢

本项目基于以下研究:
- Anthropic官方文档
- GitHub泄露的Claude系统提示词
- 社区最佳实践
- 真实用户反馈

---

**作者**: yaowanxiang  
**邮箱**: yaowanxiang@qut.edu.cn  
**GitHub**: [@yaowanxiang](https://github.com/yaowanxiang)