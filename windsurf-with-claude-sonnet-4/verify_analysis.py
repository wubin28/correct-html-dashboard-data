#!/usr/bin/env python3
"""
验证HTML报告中的分析结果是否与Excel原始数据相符
"""

import pandas as pd
import numpy as np

def load_data():
    """加载Excel数据"""
    df = pd.read_excel('/Users/binwu/correct-html-dashboard-data/first-80-rows-agentic_ai_performance_dataset_20250622.xlsx', header=1)
    print(f"数据集总记录数: {len(df)} 条")
    return df

def verify_question1(df):
    """
    验证问题1：支持多模态处理的智能体类型占比TOP3
    HTML报告结果：
    - Code Assistant: 33.33%
    - Customer Service: 14.29%
    - Data Analyst: 12.50%
    """
    print("\n=== 问题1验证：支持多模态处理的智能体类型占比TOP3 ===")
    
    # 筛选支持多模态的记录
    multimodal_agents = df[df['multimodal_capability'] == True]
    print(f"支持多模态的智能体总数: {len(multimodal_agents)}")
    
    # 计算各智能体类型的占比
    agent_type_counts = multimodal_agents['agent_type'].value_counts()
    agent_type_total = multimodal_agents.groupby('agent_type').size()
    all_agent_type_total = df.groupby('agent_type').size()
    
    # 计算占比（支持多模态的该类型 / 该类型总数）
    ratios = {}
    for agent_type in agent_type_counts.index:
        multimodal_count = agent_type_counts[agent_type]
        total_count = all_agent_type_total[agent_type]
        ratio = (multimodal_count / total_count) * 100
        ratios[agent_type] = ratio
    
    # 按占比排序
    sorted_ratios = sorted(ratios.items(), key=lambda x: x[1], reverse=True)
    
    print("\n实际分析结果（支持多模态在该智能体类型中的占比）:")
    for i, (agent_type, ratio) in enumerate(sorted_ratios[:10]):  # 显示前10个
        print(f"{i+1}. {agent_type}: {ratio:.2f}%")
    
    print("\nHTML报告中的结果:")
    html_results = [
        ('Code Assistant', 33.33),
        ('Customer Service', 14.29),
        ('Data Analyst', 12.50)
    ]
    for i, (agent_type, ratio) in enumerate(html_results):
        print(f"{i+1}. {agent_type}: {ratio}%")
    
    return sorted_ratios[:3], html_results

def verify_question2(df):
    """
    验证问题2：支持多模态处理的大模型架构占比TOP3
    HTML报告结果：
    - CodeT5+: 27.27%
    - GPT-4o: 20.00%
    - Transformer-XL: 11.76%
    """
    print("\n=== 问题2验证：支持多模态处理的大模型架构占比TOP3 ===")
    
    # 筛选支持多模态的记录
    multimodal_agents = df[df['multimodal_capability'] == True]
    
    # 计算各大模型架构的占比
    model_arch_counts = multimodal_agents['model_architecture'].value_counts()
    all_model_arch_total = df.groupby('model_architecture').size()
    
    # 计算占比（支持多模态的该架构 / 该架构总数）
    ratios = {}
    for model_arch in model_arch_counts.index:
        multimodal_count = model_arch_counts[model_arch]
        total_count = all_model_arch_total[model_arch]
        ratio = (multimodal_count / total_count) * 100
        ratios[model_arch] = ratio
    
    # 按占比排序
    sorted_ratios = sorted(ratios.items(), key=lambda x: x[1], reverse=True)
    
    print("\n实际分析结果（支持多模态在该大模型架构中的占比）:")
    for i, (model_arch, ratio) in enumerate(sorted_ratios[:10]):  # 显示前10个
        print(f"{i+1}. {model_arch}: {ratio:.2f}%")
    
    print("\nHTML报告中的结果:")
    html_results = [
        ('CodeT5+', 27.27),
        ('GPT-4o', 20.00),
        ('Transformer-XL', 11.76)
    ]
    for i, (model_arch, ratio) in enumerate(html_results):
        print(f"{i+1}. {model_arch}: {ratio}%")
    
    return sorted_ratios[:3], html_results

def verify_question3(df):
    """
    验证问题3：各任务类别公正性(bias detection)中位数TOP3
    HTML报告结果：
    - Code Generation: 0.9037
    - Communication: 0.9001
    - Creative Writing: 0.8875
    """
    print("\n=== 问题3验证：各任务类别公正性(bias detection)中位数TOP3 ===")
    
    # 计算各任务类别的bias_detection_score中位数
    task_medians = df.groupby('task_category')['bias_detection_score'].median().sort_values(ascending=False)
    
    print("\n实际分析结果（各任务类别bias detection中位数，从高到低）:")
    for i, (task_category, median) in enumerate(task_medians.items()):
        print(f"{i+1}. {task_category}: {median:.4f}")
    
    print("\nHTML报告中的结果:")
    html_results = [
        ('Code Generation', 0.9037),
        ('Communication', 0.9001),
        ('Creative Writing', 0.8875)
    ]
    for i, (task_category, median) in enumerate(html_results):
        print(f"{i+1}. {task_category}: {median}")
    
    return list(task_medians.items())[:3], html_results

def main():
    """主函数"""
    print("开始验证HTML报告中的分析结果...")
    
    # 加载数据
    df = load_data()
    
    # 验证三个问题
    actual_q1, html_q1 = verify_question1(df)
    actual_q2, html_q2 = verify_question2(df)
    actual_q3, html_q3 = verify_question3(df)
    
    # 总结验证结果
    print("\n" + "="*60)
    print("验证结果总结:")
    print("="*60)
    
    print("\n问题1 - 支持多模态处理的智能体类型占比TOP3:")
    print("HTML报告是否正确:", "✓" if [x[0] for x in actual_q1] == [x[0] for x in html_q1] else "✗")
    if [x[0] for x in actual_q1] != [x[0] for x in html_q1]:
        print("正确结果应为:")
        for i, (agent_type, ratio) in enumerate(actual_q1):
            print(f"  {i+1}. {agent_type}: {ratio:.2f}%")
    
    print("\n问题2 - 支持多模态处理的大模型架构占比TOP3:")
    print("HTML报告是否正确:", "✓" if [x[0] for x in actual_q2] == [x[0] for x in html_q2] else "✗")
    if [x[0] for x in actual_q2] != [x[0] for x in html_q2]:
        print("正确结果应为:")
        for i, (model_arch, ratio) in enumerate(actual_q2):
            print(f"  {i+1}. {model_arch}: {ratio:.2f}%")
    
    print("\n问题3 - 各任务类别公正性中位数TOP3:")
    print("HTML报告是否正确:", "✓" if [x[0] for x in actual_q3] == [x[0] for x in html_q3] else "✗")
    if [x[0] for x in actual_q3] != [x[0] for x in html_q3]:
        print("正确结果应为:")
        for i, (task_category, median) in enumerate(actual_q3):
            print(f"  {i+1}. {task_category}: {median:.4f}")

if __name__ == "__main__":
    main()
