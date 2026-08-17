from .core.calibrator import APICalibrator
from .strategies.claude_strategy import ClaudeWebSimulationStrategy
from .tools.search import web_search

__version__ = "0.1.0"
__author__ = "yaowanxiang"
__email__ = "yaowanxiang@qut.edu.cn"
__license__ = "MIT"
__description__ = "统一API与订阅版的体验差异 - 解决API降智问题的通用方案"
__url__ = "https://github.com/yaowanxiang/llm-api-calibration"

__all__ = [
    "__version__",
    "APICalibrator",
    "ClaudeWebSimulationStrategy",
    "web_search"
]