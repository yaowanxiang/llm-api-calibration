# 贡献指南

感谢你对 llm-api-calibration 项目的兴趣!

## 如何贡献

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 开发设置

```bash
# 克隆仓库
git clone https://github.com/yaowanxiang/llm-api-calibration.git
cd llm-api-calibration

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装开发依赖
pip install -e ".[dev]"
```

## 代码规范

- 遵循 PEP 8 规范
- 使用类型提示
- 编写单元测试
- 添加文档字符串

## 测试

```bash
# 运行所有测试
pytest

# 运行测试并查看覆盖率
pytest --cov=llm_api_calibration
```