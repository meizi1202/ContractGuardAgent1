# -*- coding: utf-8 -*-
"""风险规则查询引擎模块

提供风险规则知识库的查询功能，支持按行业分类查询风险规则
"""

import sys
import os
import argparse
from typing import Dict, Any, List, Optional
from pathlib import Path
import pandas as pd

# 模块级别编码配置 - 解决 Windows 控制台中文乱码问题
if sys.platform == 'win32':
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            os.environ['PYTHONIOENCODING'] = 'utf-8'


class riskRulesQueryEngine:
    """风险规则查询引擎

    负责加载和查询风险规则知识库，支持按行业类型查询
    """

    def __init__(self, basePath: str = None):
        """初始化查询引擎

        Args:
            basePath: 知识库文件的基础路径
        """
        if basePath is None:
            basePath = os.path.dirname(__file__)

        self.basePath = basePath
        self.industryMap = {
            "采购": "采购合同风险规则.xlsx",
            "租赁": "租赁合同风险规则.xlsx",
            "服务": "服务合同风险规则.xlsx",
            "通用": "通用风险规则.xlsx"
        }
        self.industryNames = {
            "采购": "采购合同",
            "租赁": "租赁合同",
            "服务": "服务合同",
            "通用": "通用"
        }
        self.severityEmoji = {
            "critical": "🔴 critical",
            "warning": "🟡 warning",
            "notice": "🔵 notice"
        }
        self.knowledgeBasePath = self._getKnowledgeBasePath()

    def _getKnowledgeBasePath(self) -> str:
        """获取知识库路径"""
        currentFile = os.path.abspath(__file__)
        srcDir = os.path.dirname(currentFile)
        skillDir = os.path.dirname(srcDir)
        claudeDir = os.path.dirname(skillDir)
        projectRoot = os.path.dirname(claudeDir)

        # 如果项目根目录下没有 docs 目录，尝试从当前工作目录获取
        if not os.path.exists(os.path.join(projectRoot, 'docs')):
            projectRoot = os.getcwd()

        return os.path.join(projectRoot, 'docs', 'knowledge_base', 'risk_rules')

    def _detectIndustry(self, query: str) -> Optional[str]:
        """从用户查询中检测行业类型

        Args:
            query: 用户输入的查询文本

        Returns:
            行业类型关键词，未识别到则返回 None
        """
        query = query.lower()

        for keyword in self.industryMap.keys():
            if keyword in query:
                return keyword

        return None

    def loadRules(self, industry: str) -> Optional[pd.DataFrame]:
        """加载指定行业的风险规则

        Args:
            industry: 行业关键词

        Returns:
            风险规则 DataFrame，失败返回 None
        """
        if industry not in self.industryMap:
            return None

        excelFile = self.industryMap[industry]
        filePath = os.path.join(self.knowledgeBasePath, excelFile)

        if not os.path.exists(filePath):
            print(f"文件不存在: {filePath}")
            return None

        try:
            df = pd.read_excel(filePath)
            return df
        except Exception as e:
            print(f"读取 Excel 文件失败: {e}")
            return None

    def formatOutput(self, df: pd.DataFrame, industry: str) -> str:
        """格式化输出风险规则

        Args:
            df: 风险规则 DataFrame
            industry: 行业类型

        Returns:
            格式化的输出文本
        """
        if df is None or len(df) == 0:
            return f"未找到 {self.industryNames.get(industry, industry)} 的风险规则"

        # 按风险类别分组
        categoryGroups = df.groupby('风险类别')

        # 构建输出
        industryName = self.industryNames.get(industry, industry)
        output = f"\n## {industryName} 风险规则\n\n"
        output += f"共 {len(df)} 条风险规则\n\n"

        for category, group in categoryGroups:
            output += f"### {category}\n\n"
            output += "| 风险项 | 严重级别 | 建议 |\n"
            output += "|--------|----------|------|\n"

            for _, row in group.iterrows():
                riskName = row.get('风险名称', '')
                severity = row.get('严重级别', '')
                suggestion = row.get('建议', '')

                severityDisplay = self.severityEmoji.get(severity, severity)
                suggestionDisplay = suggestion if pd.notna(suggestion) else '-'

                output += f"| {riskName} | {severityDisplay} | {suggestionDisplay} |\n"

            output += "\n"

        # 添加法律依据汇总
        output += "### 法律依据汇总\n\n"
        legalBasis = df[df['法律依据'].notna()]['法律依据'].unique()
        if len(legalBasis) > 0:
            for basis in legalBasis:
                output += f"- {basis}\n"
        else:
            output += "暂无法律依据信息\n"

        return output

    def query(self, query: str = None, industry: str = None, includeGeneral: bool = True) -> str:
        """查询风险规则

        Args:
            query: 用户查询文本（可选，用于自动识别行业）
            industry: 直接指定行业类型（可选）
            includeGeneral: 是否包含通用风险规则，默认 True

        Returns:
            格式化的查询结果
        """
        # 确定行业
        targetIndustry = None
        if industry:
            targetIndustry = industry
        elif query:
            targetIndustry = self._detectIndustry(query)

        # 如果未识别到行业，返回所有可用行业列表
        if targetIndustry is None:
            return self._listAvailableIndustries()

        # 加载指定行业的规则
        df = self.loadRules(targetIndustry)
        if df is None:
            return f"无法加载 {targetIndustry} 的风险规则，请检查知识库文件是否存在"

        # 如果不是查询通用规则，且指定了特定行业，则合并通用规则
        if includeGeneral and targetIndustry != "通用":
            dfGeneral = self.loadRules("通用")
            if dfGeneral is not None and len(dfGeneral) > 0:
                # 合并通用规则到行业规则后面
                df = pd.concat([df, dfGeneral], ignore_index=True)

        return self.formatOutput(df, targetIndustry)

    def _listAvailableIndustries(self) -> str:
        """列出所有可用的行业类型

        Returns:
            可用行业列表
        """
        output = "\n## 可用的风险规则类型\n\n"
        output += "请指定要查询的行业类型：\n\n"

        for keyword, name in self.industryNames.items():
            excelFile = self.industryMap[keyword]
            filePath = os.path.join(self.knowledgeBasePath, excelFile)
            status = "✓ 已配置" if os.path.exists(filePath) else "✗ 文件缺失"
            output += f"- **{keyword}**（{name}）: {status}\n"

        output += "\n使用方法：\n"
        output += "```bash\n"
        output += "python .claude/skills/risk-rules-query/src/queryEngine.py 采购\n"
        output += "```\n"

        return output


def main():
    """主函数 - 命令行入口"""
    parser = argparse.ArgumentParser(description='风险规则查询工具')
    parser.add_argument('industry', nargs='?', help='行业类型（采购/租赁/服务/通用）')
    parser.add_argument('--list', '-l', action='store_true', help='列出所有可用的风险规则类型')

    args = parser.parse_args()

    engine = riskRulesQueryEngine()

    if args.list:
        print(engine._listAvailableIndustries())
    elif args.industry:
        print(engine.query(industry=args.industry))
    else:
        print(engine._listAvailableIndustries())


if __name__ == '__main__':
    main()
