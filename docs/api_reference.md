# API参考文档

## APICalibrator

### 初始化

```python
from llm_api_calibration import APICalibrator

calibrator = APICalibrator(
    api_key="your-api-key",
    model="claude-3-5-sonnet-20240620"
)
```

### 方法

#### get_recommended_config()

获取推荐配置。

**参数:**
- `scenario` (str): 使用场景
  - `research_writing`: 学术写作
  - `code_review`: 代码审查
  - `data_analysis`: 数据分析
  - `daily_chat`: 日常对话
- `language` (str): 语言 (chinese/english)
- `enable_search` (bool): 是否启用搜索模拟
- `enable_code_execution` (bool): 是否启用代码执行模拟

**返回:**
- `Dict[str, Any]`: 配置字典

**示例:**
```python
config = calibrator.get_recommended_config(
    scenario="research_writing",
    language="chinese"
)
```

#### call_with_calibration()

使用校准配置调用API。

**参数:**
- `prompt` (str): 用户提示
- `config` (Optional[Dict]): 配置字典

**返回:**
- `str`: API响应文本

**示例:**
```python
response = calibrator.call_with_calibration(
    prompt="写一段研究综述",
    config=config
)
```

#### call_web_simulation()

模拟Web版Claude调用(含自动搜索)。

**参数:**
- `prompt` (str): 用户提示
- `scenario` (str): 使用场景

**返回:**
- `str`: API响应文本

**示例:**
```python
response = calibrator.call_web_simulation(
    prompt="分析AI发展趋势",
    scenario="research_writing"
)
```

## ClaudeWebSimulationStrategy

### 初始化

```python
from llm_api_calibration.strategies import ClaudeWebSimulationStrategy

strategy = ClaudeWebSimulationStrategy(
    enable_search=True,
    enable_code_execution=False,
    memory_window=10
)
```

### 方法

#### generate_config()

生成配置字典。

**参数:**
- `scenario` (str): 使用场景
- `language` (str): 语言

**返回:**
- `Dict[str, Any]`: 配置字典

**示例:**
```python
config = strategy.generate_config(
    scenario="research_writing",
    language="chinese"
)
```