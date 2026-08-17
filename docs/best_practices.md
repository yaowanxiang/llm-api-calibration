# 最佳实践指南

## 系统提示词优化技巧

### 1. 核心原则

- **保持简洁**: 系统提示词不是越长越好
- **明确角色**: 清晰定义AI的身份和专长
- **场景化**: 针对不同场景定制不同的提示词
- **行为约束**: 明确什么该做,什么不该做

### 2. 模块化设计

参考本项目的设计,将提示词分为以下模块:

```python
# 基础模块(始终加载)
base_prompt = "你是Claude,由Anthropic创建的AI助手..."

# 场景模块(根据任务动态加载)
if task == "writing":
    base_prompt += writing_module

# 工具模块(根据可用能力加载)
if enable_search:
    base_prompt += search_module
```

### 3. 场景优化

#### 学术写作场景

```
你的专长:
- 撰写符合顶会/期刊标准的学术论文
- 提供IMRAD结构建议和逻辑优化
- 审查并改进论文的语言和格式
```

#### 代码审查场景

```
你的专长:
- 深入分析代码的逻辑和效率
- 识别潜在bug和安全问题
- 提供代码重构建议
```

## 参数配置建议

### 1. 不要迷信temperature

2026年的研究证实:
- temperature在0.0-1.0范围内对问题解决性能无显著差异
- 新版Claude已废弃temperature/top_p参数
- 主要靠系统提示词控制行为

### 2. 场景化max_tokens

```python
tokens = {
    "research_writing": 4096,  # 长输出
    "code_review": 2048,       # 适中
    "daily_chat": 1024,         # 短对话
}
```

## 工具链集成

### 1. 搜索集成

```python
if enable_search:
    search_results = web_search(user_prompt)
    user_prompt = f"{user_prompt}\n\n[最新信息]\n{search_results}"
```

### 2. 上下文管理

```python
conversation_history = []

def add_context(user_msg, assistant_msg):
    conversation_history.extend([
        {"role": "user", "content": user_msg},
        {"role": "assistant", "content": assistant_msg}
    ])
    # 保持最近的N轮对话
    if len(conversation_history) > 20:
        conversation_history = conversation_history[-20:]
```

## 版本兼容性

### 1. 自动降级

```python
try:
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        temperature=0.7,  # 旧版参数
        ...
    )
except BadRequestError:
    # 新版已废弃,降级调用
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        ...  # 不带temperature
    )
```

### 2. 版本检测

```python
def get_model_version(model_name):
    """从模型名称提取版本信息"""
    # claude-3-5-sonnet-20240620 -> 20240620
    parts = model_name.split("-")
    return parts[-1] if parts else None

def check_deprecated_params(model_version):
    """检查参数是否废弃"""
    return model_version >= "20250514"
```

## 性能优化

### 1. 缓存配置

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_cached_config(scenario, language):
    """缓存配置,避免重复计算"""
    return generate_config(scenario, language)
```

### 2. 批量调用

```python
async def batch_calibrate(prompts, config):
    """批量调用API"""
    tasks = [call_api(prompt, config) for prompt in prompts]
    return await asyncio.gather(*tasks)
```

## 常见问题

### Q: 为什么我的API还是比官网慢?

A: 可能原因:
1. 网络延迟
2. 官网有CDN加速
3. 官网使用了流式输出

建议: 使用流式API(`stream=True`)改善体验。

### Q: 系统提示词多长合适?

A: 建议:
- 基础部分: 500-1000 tokens
- 场景模块: 500-1000 tokens
- 总计: 2000-3000 tokens

### Q: 如何验证校准效果?

A: 使用对比测试:

```python
# 测试相同问题
prompt = "写一段研究综述"

# API响应
api_response = calibrator.call_web_simulation(prompt)

# 人工在官网测试相同问题
# 对比完整性、细节、主动性
```

## 扩展阅读

- [Anthropic官方文档](https://docs.anthropic.com/)
- [Claude系统提示词分析](https://github.com/anthropics/claude-research)
- [LLM提示工程最佳实践](https://github.com/dair-ai/Prompt-Engineering-Guide)