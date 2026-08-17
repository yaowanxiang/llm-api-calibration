import pytest
from llm_api_calibration import APICalibrator


class TestAPICalibrator:
    """测试API校准器"""
    
    @pytest.fixture
    def calibrator(self):
        """创建校准器实例(使用测试密钥)"""
        # 注意: 实际测试需要真实API密钥
        return APICalibrator(
            api_key="test-key",
            model="claude-3-5-sonnet-20240620"
        )
    
    def test_get_recommended_config(self, calibrator):
        """测试获取推荐配置"""
        config = calibrator.get_recommended_config(
            scenario="research_writing",
            language="chinese"
        )
        
        assert "system_prompt" in config
        assert "max_tokens" in config
        assert config["max_tokens"] == 4096
        assert config["enable_search"] == False
    
    def test_build_system_prompt(self, calibrator):
        """测试系统提示词构建"""
        config = calibrator.get_recommended_config()
        
        prompt = config["system_prompt"]
        
        # 验证关键组件
        assert "Claude" in prompt
        assert "核心行为准则" in prompt
        assert "学术写作场景" in prompt
        assert "联网搜索能力" in prompt
    
    def test_scenario_specific_config(self, calibrator):
        """测试场景特定配置"""
        # 代码审查场景
        config_code = calibrator.get_recommended_config(scenario="code_review")
        assert config_code["max_tokens"] == 2048
        assert "代码审查场景" in config_code["system_prompt"]
        
        # 数据分析场景
        config_data = calibrator.get_recommended_config(scenario="data_analysis")
        assert config_data["max_tokens"] == 3072
        assert "数据分析场景" in config_data["system_prompt"]
    
    def test_language_specific(self, calibrator):
        """测试语言特定配置"""
        # 英文配置
        config_en = calibrator.get_recommended_config(language="english")
        assert "english" in config_en["system_prompt"]
        
        # 中文配置
        config_cn = calibrator.get_recommended_config(language="chinese")
        assert "chinese" in config_cn["system_prompt"]