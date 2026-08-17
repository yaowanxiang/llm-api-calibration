"""
API校准核心模块
"""

import anthropic
from typing import Dict, Any, Optional
from datetime import datetime


class APICalibrator:
    """API校准器 - 让API调用体验接近订阅版"""
    
    def __init__(self, api_key: str, model: str = "claude-3-5-sonnet-20240620"):
        """
        初始化校准器
        
        Args:
            api_key: Anthropic API密钥
            model: 模型版本号
        """
        self.api_key = api_key
        self.model = model
        self.client = anthropic.Anthropic(api_key=api_key)
        
    def get_recommended_config(
        self, 
        scenario: str = "research_writing",
        language: str = "chinese",
        enable_search: bool = False,
        enable_code_execution: bool = False
    ) -> Dict[str, Any]:
        """
        获取推荐配置
        """
        from .strategies.claude_strategy import ClaudeWebSimulationStrategy
        
        strategy = ClaudeWebSimulationStrategy(
            enable_search=enable_search,
            enable_code_execution=enable_code_execution,
            memory_window=10
        )
        
        return strategy.generate_config(
            scenario=scenario,
            language=language
        )
    
    def call_with_calibration(
        self,
        prompt: str,
        config: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        使用校准配置调用API
        """
        if config is None:
            config = self.get_recommended_config()
            
        try:
            response = self.client.messages.create(
                model=config.get("model", self.model),
                max_tokens=config.get("max_tokens", 4096),
                system=config.get("system_prompt", ""),
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
            
        except anthropic.BadRequestError as e:
            error_str = str(e)
            if "temperature" in error_str or "top_p" in error_str:
                print("⚠️  检测到参数废弃,使用新版本调用方式")
                response = self.client.messages.create(
                    model=config.get("model", self.model),
                    max_tokens=config.get("max_tokens", 4096),
                    system=config.get("system_prompt", ""),
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text
            else:
                raise
    
    def call_web_simulation(
        self,
        prompt: str,
        scenario: str = "research_writing"
    ) -> str:
        """
        模拟Web版Claude的调用方式
        """
        config = self.get_recommended_config(
            scenario=scenario,
            enable_search=True
        )
        
        if config.get("enable_search"):
            from .tools.search import web_search
            search_results = web_search(prompt, max_results=3)
            prompt = f"{prompt}\n\n[自动检索到的最新信息]\n{search_results}"
        
        return self.call_with_calibration(prompt, config)