"""合同审查器模块

提供完整的合同审查功能：解析 + 提取 + 审查 + 风险评估
"""

import re
from typing import Dict, Any, List, Optional


class contractReviewer:
    """合同审查器，提供完整的合同审查流程"""

    # 合规性检查项
    complianceChecks = {
        "party": {
            "name": "合同主体",
            "description": "合同当事人信息是否明确",
            "required": True
        },
        "amount": {
            "name": "金额条款",
            "description": "合同金额是否明确",
            "required": True
        },
        "date": {
            "name": "日期条款",
            "description": "签订日期和有效期是否明确",
            "required": True
        },
        "term": {
            "name": "履行期限",
            "description": "合同履行期限是否明确",
            "required": True
        },
        "liability": {
            "name": "违约责任",
            "description": "违约责任条款是否完整",
            "required": True
        },
        "dispute": {
            "name": "争议解决",
            "description": "争议解决条款是否完整",
            "required": False
        },
        "termination": {
            "name": "终止条款",
            "description": "合同终止条件是否明确",
            "required": False
        }
    }

    # 风险模式
    riskPatterns = [
        {
            "level": "critical",
            "type": "金额风险",
            "patterns": [
                r"金额.*未确定",
                r"待定",
                r"另行约定",
                r"不确定"
            ],
            "suggestion": "建议明确约定具体金额"
        },
        {
            "level": "warning",
            "type": "期限风险",
            "patterns": [
                r"期限.*过长",
                r"无固定期限",
                r"永久"
            ],
            "suggestion": "建议设置合理期限"
        },
        {
            "level": "warning",
            "type": "责任风险",
            "patterns": [
                r"免责",
                r"不承担.*责任",
                r"概不负责"
            ],
            "suggestion": "注意免责条款的合理性"
        },
        {
            "level": "warning",
            "type": "解约风险",
            "patterns": [
                r"不得解除",
                r"不可终止",
                r"单方面.*解除"
            ],
            "suggestion": "注意解约条款的公平性"
        }
    ]

    def __init__(self):
        pass

    def review(self, content: str) -> Dict[str, Any]:
        """执行完整的合同审查

        Args:
            content: 合同文本内容

        Returns:
            包含审查结果的字典
        """
        if not content:
            return {
                "success": False,
                "error": "内容为空"
            }

        # 1. 提取关键信息
        extractedInfo = self.extractKeyInfo(content)

        # 2. 合规性审查
        complianceResult = self.checkCompliance(content, extractedInfo)

        # 3. 风险评估
        riskResult = self.assessRisk(content)

        # 4. 生成总结
        summary = self.generateSummary(complianceResult, riskResult)

        return {
            "success": True,
            "summary": summary,
            "extractedInfo": extractedInfo,
            "compliance": complianceResult,
            "risks": riskResult
        }

    def extractKeyInfo(self, content: str) -> Dict[str, Any]:
        """提取合同关键信息

        Args:
            content: 合同文本内容

        Returns:
            提取的关键信息
        """
        info = {
            "parties": [],
            "amounts": [],
            "dates": [],
            "deadlines": [],
            "contacts": {}
        }

        # 提取当事人
        partyPatterns = [
            r"甲方[：:]\s*([^\n]{2,50})",
            r"乙方[：:]\s*([^\n]{2,50})",
            r"丙方[：:]\s*([^\n]{2,50})",
            r"委托方[：:]\s*([^\n]{2,50})",
            r"受托方[：:]\s*([^\n]{2,50})"
        ]
        for pattern in partyPatterns:
            matches = re.findall(pattern, content)
            info["parties"].extend(matches)

        # 提取金额
        amountPattern = r"(?:人民币|美元|欧元|￥|\$|€)\s*[\d,]+(?:\.\d{2})?(?:万|亿|元|美元|欧元)?"
        info["amounts"] = re.findall(amountPattern, content)

        # 提取日期
        datePattern = r"(\d{4})[年\-/](\d{1,2})[月\-/](\d{1,2})[日]?"
        info["dates"] = re.findall(datePattern, content)

        # 提取期限
        termPattern = r"(?:期限|有效期|服务期|租赁期)[：:]\s*([^\n]{2,30})"
        info["deadlines"] = re.findall(termPattern, content)

        # 提取联系方式
        phonePattern = r"电话[：:]\s*[\d\-]{7,}"
        info["contacts"]["phones"] = re.findall(phonePattern, content)

        return info

    def checkCompliance(self, content: str, extractedInfo: Dict[str, Any]) -> Dict[str, Any]:
        """执行合规性审查

        Args:
            content: 合同文本内容
            extractedInfo: 提取的关键信息

        Returns:
            合规性检查结果
        """
        results = {}
        missingClauses = []

        for key, check in self.complianceChecks.items():
            isPresent = False
            detail = ""

            if key == "party":
                isPresent = len(extractedInfo.get("parties", [])) > 0
                detail = f"发现 {len(extractedInfo.get('parties', []))} 方当事人"

            elif key == "amount":
                isPresent = len(extractedInfo.get("amounts", [])) > 0
                detail = f"发现 {len(extractedInfo.get('amounts', []))} 处金额"

            elif key == "date":
                isPresent = len(extractedInfo.get("dates", [])) > 0
                detail = f"发现 {len(extractedInfo.get('dates', []))} 个日期"

            elif key == "term":
                isPresent = len(extractedInfo.get("deadlines", [])) > 0
                detail = f"发现 {len(extractedInfo.get('deadlines', []))} 个期限"

            elif key == "liability":
                isPresent = "违约" in content or "责任" in content
                detail = "找到违约责任相关条款" if isPresent else "未找到违约责任条款"

            elif key == "dispute":
                isPresent = "争议" in content or "仲裁" in content or "诉讼" in content
                detail = "找到争议解决条款" if isPresent else "未找到争议解决条款"

            elif key == "termination":
                isPresent = "终止" in content or "解除" in content or "到期" in content
                detail = "找到终止条款" if isPresent else "未找到终止条款"

            results[key] = {
                "name": check["name"],
                "description": check["description"],
                "present": isPresent,
                "detail": detail,
                "required": check["required"]
            }

            if check["required"] and not isPresent:
                missingClauses.append(check["name"])

        return {
            "complete": len(missingClauses) == 0,
            "missingClauses": missingClauses,
            "details": results
        }

    def assessRisk(self, content: str) -> List[Dict[str, Any]]:
        """评估合同风险

        Args:
            content: 合同文本内容

        Returns:
            风险列表
        """
        risks = []

        for riskType in self.riskPatterns:
            for pattern in riskType["patterns"]:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    risks.append({
                        "level": riskType["level"],
                        "type": riskType["type"],
                        "matched": matches[0] if isinstance(matches[0], str) else str(matches[0]),
                        "suggestion": riskType["suggestion"]
                    })
                    break  # 每个风险类型只添加一次

        return risks

    def generateSummary(self, complianceResult: Dict[str, Any], riskResult: List[Dict[str, Any]]) -> Dict[str, Any]:
        """生成审查总结

        Args:
            complianceResult: 合规性检查结果
            riskResult: 风险评估结果

        Returns:
            审查总结
        """
        critical = sum(1 for r in riskResult if r["level"] == "critical")
        warning = sum(1 for r in riskResult if r["level"] == "warning")
        info = sum(1 for r in riskResult if r["level"] == "info")

        return {
            "totalIssues": len(riskResult) + len(complianceResult.get("missingClauses", [])),
            "critical": critical,
            "warning": warning,
            "info": info,
            "missingClausesCount": len(complianceResult.get("missingClauses", []))
        }
