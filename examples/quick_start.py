"""
LLM API Calibration Tool 快速开始
"""

from llm_api_calibration import APICalibrator

# 初始化校准器
calibrator = APICalibrator(
    api_key="your-api-key",  # 替换为你的API密钥
    model="claude-3-5-sonnet-20240620"
)

# 示例1: 基础学术写作
response = calibrator.call_with_calibration(
    prompt="写一段关于深度学习在医学影像应用的研究综述",
    config=calibrator.get_recommended_config(
        scenario="research_writing",
        language="chinese"
    )
)
print(response)

# 示例2: 模拟Web版(含自动搜索)
response = calibrator.call_web_simulation(
    prompt="分析2024年Claude模型的发展趋势",
    scenario="research_writing"
)
print(response)