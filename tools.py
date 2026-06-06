"""
Learning Tools - AI学习工具
支持学习计划、知识图谱、练习生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class LearningTools:
    """
    AI学习工具
    支持：计划、图谱、练习
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_learning_plan(self, topic: str, level: str, duration: str) -> Dict:
        """生成学习计划"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{level}水平的学习者生成{topic}学习计划：

时长：{duration}

请返回JSON格式：
{{
    "phases": [
        {{"name": "阶段名", "duration": "时长", "topics": ["主题"], "resources": ["资源"], "projects": ["项目"]}}
    ],
    "milestones": ["里程碑"],
    "tips": ["学习建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"plan": content}

    def generate_knowledge_graph(self, topic: str) -> Dict:
        """生成知识图谱"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请生成{topic}的知识图谱：

请返回JSON格式：
{{
    "nodes": [
        {{"id": "节点ID", "label": "节点名", "level": "层级", "description": "描述"}}
    ],
    "edges": [
        {{"source": "源节点", "target": "目标节点", "relation": "关系"}}
    ]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"graph": content}

    def generate_exercises(self, topic: str, difficulty: str, count: int = 5) -> List[Dict]:
        """生成练习题"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请生成{count}道{topic}的{difficulty}难度练习题：

请返回JSON格式：
[
    {{"question": "题目", "type": "选择/填空/编程", "options": ["选项"], "answer": "答案", "explanation": "解释"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"exercises": content}]

    def generate_flashcards(self, topic: str, count: int = 10) -> List[Dict]:
        """生成闪卡"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请生成{count}张{topic}的闪卡：

请返回JSON格式：
[
    {{"front": "正面", "back": "背面", "category": "分类"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"flashcards": content}]

    def explain_concept(self, concept: str, level: str = "intermediate") -> str:
        """解释概念"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请用{level}水平解释{concept}：

要求：
1. 清晰易懂
2. 包含示例
3. 类比说明
4. 常见误区"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_quiz(self, topic: str, question_count: int = 10) -> Dict:
        """生成测验"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请生成{topic}的{question_count}道测验题：

请返回JSON格式：
{{
    "title": "测验标题",
    "questions": [
        {{"id": 1, "question": "问题", "type": "类型", "options": ["选项"], "correct": "正确答案", "points": 分值}}
    ],
    "total_points": 总分,
    "passing_score": 及格分
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"quiz": content}


def create_tools(**kwargs) -> LearningTools:
    """创建学习工具"""
    return LearningTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("Learning Tools")
    print()

    # 测试
    plan = tools.generate_learning_plan("Python编程", "beginner", "3个月")
    print(json.dumps(plan, ensure_ascii=False, indent=2))
