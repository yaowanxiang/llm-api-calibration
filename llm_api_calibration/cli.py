"""
CLI interface for LLM API Calibration Tool
"""

import argparse
import sys
from llm_api_calibration import APICalibrator


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="LLM API Calibration Tool - 统一API与订阅版的体验差异",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 学术写作场景
  llm-calibrate --scenario research_writing --language chinese --prompt "写研究综述"
  
  # 代码审查场景
  llm-calibrate --scenario code_review --prompt "审查这段代码"
  
  # 模拟Web版(含搜索)
  llm-calibrate --web-mode --prompt "分析AI发展趋势"
  
  # 显示推荐配置
  llm-calibrate --scenario research_writing --show-config
        """
    )
    
    parser.add_argument(
        '--api-key',
        help='Anthropic API密钥 (默认从环境变量ANTHROPIC_API_KEY读取)',
        default=None
    )
    
    parser.add_argument(
        '--model',
        default='claude-3-5-sonnet-20240620',
        help='模型版本号 (默认: claude-3-5-sonnet-20240620)'
    )
    
    parser.add_argument(
        '--scenario',
        choices=['research_writing', 'code_review', 'data_analysis', 'daily_chat'],
        default='research_writing',
        help='使用场景 (默认: research_writing)'
    )
    
    parser.add_argument(
        '--language',
        choices=['chinese', 'english'],
        default='chinese',
        help='语言 (默认: chinese)'
    )
    
    parser.add_argument(
        '--web-mode',
        action='store_true',
        help='启用Web版模拟模式 (含自动搜索)'
    )
    
    parser.add_argument(
        '--max-tokens',
        type=int,
        help='最大生成token数 (场景化自动配置)'
    )
    
    parser.add_argument(
        '--show-config',
        action='store_true',
        help='仅显示推荐配置,不执行调用'
    )
    
    parser.add_argument(
        '--prompt',
        help='用户提示内容'
    )
    
    parser.add_argument(
        '--output',
        help='输出到文件'
    )
    
    args = parser.parse_args()
    
    # 获取API密钥
    import os
    api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
    
    if not api_key:
        print("错误: 需要提供API密钥")
        print("方式1: 使用 --api-key 参数")
        print("方式2: 设置环境变量 ANTHROPIC_API_KEY")
        sys.exit(1)
    
    # 初始化校准器
    calibrator = APICalibrator(api_key=api_key, model=args.model)
    
    # 获取推荐配置
    config = calibrator.get_recommended_config(
        scenario=args.scenario,
        language=args.language,
        enable_search=args.web_mode
    )
    
    # 如果指定了max_tokens,覆盖默认值
    if args.max_tokens:
        config['max_tokens'] = args.max_tokens
    
    # 显示配置模式
    if args.show_config:
        print("="*60)
        print("推荐配置:")
        print("="*60)
        print(f"模型: {config['model']}")
        print(f"场景: {args.scenario}")
        print(f"语言: {args.language}")
        print(f"最大tokens: {config['max_tokens']}")
        print(f"启用搜索: {config['enable_search']}")
        print(f"记忆窗口: {config['memory_window']}轮")
        print("\n系统提示词预览:")
        print("-"*60)
        print(config['system_prompt'][:500] + "...")
        print("="*60)
        return
    
    # 执行调用
    if not args.prompt:
        print("错误: 需要提供 --prompt 参数")
        sys.exit(1)
    
    try:
        if args.web_mode:
            response = calibrator.call_web_simulation(
                prompt=args.prompt,
                scenario=args.scenario
            )
        else:
            response = calibrator.call_with_calibration(
                prompt=args.prompt,
                config=config
            )
        
        # 输出结果
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(response)
            print(f"✅ 响应已写入: {args.output}")
        else:
            print(response)
            
    except Exception as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()