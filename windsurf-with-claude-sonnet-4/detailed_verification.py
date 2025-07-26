#!/usr/bin/env python3
"""
详细验证HTML报告中的分析结果
"""

import pandas as pd
import numpy as np

def load_data():
    """加载Excel数据"""
    df = pd.read_excel('/Users/binwu/correct-html-dashboard-data/first-80-rows-agentic_ai_performance_dataset_20250622.xlsx', header=1)
    print(f"数据集总记录数: {len(df)} 条")
    return df

def detailed_question1_analysis(df):
    """详细分析问题1"""
    print("\n=== 问题1详细分析：支持多模态处理的智能体类型占比TOP3 ===")
    
    # 显示所有智能体类型的统计
    print("\n各智能体类型的详细统计:")
    agent_stats = []
    
    for agent_type in df['agent_type'].unique():
        total_count = len(df[df['agent_type'] == agent_type])
        multimodal_count = len(df[(df['agent_type'] == agent_type) & (df['multimodal_capability'] == True)])
        ratio = (multimodal_count / total_count) * 100 if total_count > 0 else 0
        agent_stats.append({
            'agent_type': agent_type,
            'total_count': total_count,
            'multimodal_count': multimodal_count,
            'ratio': ratio
        })
    
    # 按占比排序
    agent_stats.sort(key=lambda x: x['ratio'], reverse=True)
    
    print(f"{'智能体类型':<20} {'总数':<5} {'支持多模态':<8} {'占比(%)':<8}")
    print("-" * 50)
    for stat in agent_stats:
        print(f"{stat['agent_type']:<20} {stat['total_count']:<5} {stat['multimodal_count']:<8} {stat['ratio']:<8.2f}")
    
    return agent_stats[:3]

def detailed_question2_analysis(df):
    """详细分析问题2"""
    print("\n=== 问题2详细分析：支持多模态处理的大模型架构占比TOP3 ===")
    
    # 显示所有大模型架构的统计
    print("\n各大模型架构的详细统计:")
    model_stats = []
    
    for model_arch in df['model_architecture'].unique():
        total_count = len(df[df['model_architecture'] == model_arch])
        multimodal_count = len(df[(df['model_architecture'] == model_arch) & (df['multimodal_capability'] == True)])
        ratio = (multimodal_count / total_count) * 100 if total_count > 0 else 0
        model_stats.append({
            'model_architecture': model_arch,
            'total_count': total_count,
            'multimodal_count': multimodal_count,
            'ratio': ratio
        })
    
    # 按占比排序
    model_stats.sort(key=lambda x: x['ratio'], reverse=True)
    
    print(f"{'大模型架构':<20} {'总数':<5} {'支持多模态':<8} {'占比(%)':<8}")
    print("-" * 50)
    for stat in model_stats:
        print(f"{stat['model_architecture']:<20} {stat['total_count']:<5} {stat['multimodal_count']:<8} {stat['ratio']:<8.2f}")
    
    return model_stats[:3]

def detailed_question3_analysis(df):
    """详细分析问题3"""
    print("\n=== 问题3详细分析：各任务类别公正性(bias detection)中位数TOP3 ===")
    
    # 显示所有任务类别的统计
    print("\n各任务类别的bias detection详细统计:")
    task_stats = []
    
    for task_category in df['task_category'].unique():
        task_data = df[df['task_category'] == task_category]['bias_detection_score']
        count = len(task_data)
        median_val = task_data.median()
        mean_val = task_data.mean()
        min_val = task_data.min()
        max_val = task_data.max()
        
        task_stats.append({
            'task_category': task_category,
            'count': count,
            'median': median_val,
            'mean': mean_val,
            'min': min_val,
            'max': max_val
        })
    
    # 按中位数排序
    task_stats.sort(key=lambda x: x['median'], reverse=True)
    
    print(f"{'任务类别':<25} {'数量':<5} {'中位数':<8} {'均值':<8} {'最小值':<8} {'最大值':<8}")
    print("-" * 70)
    for stat in task_stats:
        print(f"{stat['task_category']:<25} {stat['count']:<5} {stat['median']:<8.4f} {stat['mean']:<8.4f} {stat['min']:<8.4f} {stat['max']:<8.4f}")
    
    return task_stats[:3]

def show_html_vs_actual_comparison():
    """显示HTML报告与实际结果的对比"""
    print("\n" + "="*80)
    print("HTML报告 vs 实际数据对比总结")
    print("="*80)
    
    print("\n问题1 - 支持多模态处理的智能体类型占比TOP3:")
    print("HTML报告结果:")
    print("  1. Code Assistant: 33.33%")
    print("  2. Customer Service: 14.29%") 
    print("  3. Data Analyst: 12.50%")
    print("\n实际正确结果:")
    print("  1. Research Assistant: 60.00%")
    print("  2. Document Processor: 33.33%")
    print("  3. Sales Assistant: 28.57%")
    print("结论: HTML报告结果完全错误 ❌")
    
    print("\n问题2 - 支持多模态处理的大模型架构占比TOP3:")
    print("HTML报告结果:")
    print("  1. CodeT5+: 27.27%")
    print("  2. GPT-4o: 20.00%")
    print("  3. Transformer-XL: 11.76%")
    print("\n实际正确结果:")
    print("  1. GPT-4o: 37.50%")
    print("  2. CodeT5+: 33.33%")
    print("  3. Transformer-XL: 20.00%")
    print("结论: HTML报告排序错误，数值也不准确 ❌")
    
    print("\n问题3 - 各任务类别公正性中位数TOP3:")
    print("HTML报告结果:")
    print("  1. Code Generation: 0.9037")
    print("  2. Communication: 0.9001")
    print("  3. Creative Writing: 0.8875")
    print("\n实际正确结果:")
    print("  1. Communication: 0.8214")
    print("  2. Research & Summarization: 0.7853")
    print("  3. Decision Making: 0.7816")
    print("结论: HTML报告结果完全错误，数值明显偏高 ❌")

def main():
    """主函数"""
    print("开始详细验证HTML报告中的分析结果...")
    
    # 加载数据
    df = load_data()
    
    # 详细分析三个问题
    detailed_question1_analysis(df)
    detailed_question2_analysis(df)
    detailed_question3_analysis(df)
    
    # 显示对比总结
    show_html_vs_actual_comparison()

if __name__ == "__main__":
    main()
