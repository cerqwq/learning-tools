# 📖 Learning Tools

AI学习工具，支持学习计划、知识图谱、练习生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📋 学习计划生成
- 🕸️ 知识图谱生成
- 📝 练习题生成
- 🃏 闪卡生成
- 💡 概念解释
- 📊 测验生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from learning_tools import create_tools

tools = create_tools()

# 学习计划
plan = tools.generate_learning_plan("Python编程", "beginner", "3个月")

# 知识图谱
graph = tools.generate_knowledge_graph("机器学习")

# 练习题
exercises = tools.generate_exercises("Python", "medium", 10)

# 闪卡
flashcards = tools.generate_flashcards("数据结构", 20)

# 概念解释
explanation = tools.explain_concept("装饰器", "beginner")

# 测验
quiz = tools.generate_quiz("Python基础", 10)
```

## 📁 项目结构

```
learning-tools/
├── tools.py       # 学习工具核心
└── README.md
```

## 📄 许可证

MIT License
