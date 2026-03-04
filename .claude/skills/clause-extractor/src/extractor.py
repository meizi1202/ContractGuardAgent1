"""条款提取器模块

从文档内容中提取关键信息
"""

import re
from typing import Dict, Any, List, Optional


class clauseExtractor:
    """条款提取器，用于从文档内容中提取关键信息"""

    # 常用条款类型模式
    clausePatterns = {
        "party": r"(?:甲方|乙方|丙方|当事人|签订方|合同方|委托方|受托方|承租方|出租方|买方|卖方|发包方|承包方)",
        "date": r"(\d{4})[年\-/](\d{1,2})[月\-/](\d{1,2})[日]?|(\d{4})[年\s]+(\d{1,2})[月\s]+(\d{1,2})",
        "amount": r"(?:人民币|美元|欧元|￥|\$|€)\s*[\d,]+(?:\.\d{2})?(?:万|亿|元|美元|欧元)?",
        "deadline": r"(\d{4})[年\-/](\d{1,2})[月\-/](\d{1,2})[日之前之后]|截至|截止|在.*日前",
        "contact": r"电话[:：]?\s*[\d\-]{7,}|邮箱[:：]?\s*[\w\.\-]+@[\w\.\-]+|地址[:：]",
        "term": r"(?:期限|有效期|服务期|租赁期|合作期|委托期)\s*[:：]?\s*\d+[年月天]",
    }

    def __init__(self):
        pass

    def extract(self, content: str, clauseTypes: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        从文档内容中提取关键信息

        Args:
            content: 文档文本内容
            clauseTypes: 要提取的条款类型列表，None 表示提取所有类型

        Returns:
            包含提取结果的字典
        """
        if not content:
            return {
                "success": False,
                "error": "内容为空"
            }

        if clauseTypes is None:
            clauseTypes = list(self.clausePatterns.keys())

        result = {
            "success": True,
            "extractedClauses": {}
        }

        for clauseType in clauseTypes:
            if clauseType in self.clausePatterns:
                pattern = self.clausePatterns[clauseType]
                matches = re.findall(pattern, content)
                if matches:
                    result["extractedClauses"][clauseType] = matches

        return result

    def extractParties(self, content: str) -> Dict[str, Any]:
        """提取合同当事人信息"""
        pattern = self.clausePatterns["party"]
        parties = re.findall(pattern, content)

        # 尝试提取当事人名称（通常在关键词后面）
        namePattern = r"(?:甲方|乙方|丙方|当事人|签订方|合同方)[:：]\s*([^\s，。,]{2,})"
        partyNames = re.findall(namePattern, content)

        return {
            "partyKeywords": parties,
            "partyNames": partyNames
        }

    def extractDates(self, content: str) -> List[str]:
        """提取日期信息"""
        pattern = self.clausePatterns["date"]
        dates = re.findall(pattern, content)
        return dates

    def extractAmounts(self, content: str) -> List[str]:
        """提取金额信息"""
        pattern = self.clausePatterns["amount"]
        amounts = re.findall(pattern, content)
        return amounts

    def extractDeadlines(self, content: str) -> List[str]:
        """提取截止日期信息"""
        pattern = self.clausePatterns["deadline"]
        deadlines = re.findall(pattern, content)
        return deadlines

    def extractContacts(self, content: str) -> Dict[str, Any]:
        """提取联系方式"""
        # 电话
        phonePattern = r"(?:电话|Tel|Mobile)[:：]?\s*([\d\-]{7,})"
        phones = re.findall(phonePattern, content)

        # 邮箱
        emailPattern = r"(?:邮箱|Email|E-mail)[:：]?\s*([\w\.\-]+@[\w\.\-]+)"
        emails = re.findall(emailPattern, content)

        # 地址
        addressPattern = r"(?:地址|Address)[:：]\s*([^\n]{5,100})"
        addresses = re.findall(addressPattern, content)

        return {
            "phones": phones,
            "emails": emails,
            "addresses": addresses
        }

    def extractContractAmount(self, content: str) -> Dict[str, Any]:
        """提取合同金额信息"""
        result = {}

        # 项目总金额
        totalPatterns = [
            r'项目总金额[为:]?\s*(\d{1,3}(?:,\d{3})*)元',
            r'总金额[为:]?\s*(\d{1,3}(?:,\d{3})*)元',
            r'合同总金额[为:]?\s*(\d{1,3}(?:,\d{3})*)元',
        ]
        for pattern in totalPatterns:
            match = re.search(pattern, content)
            if match:
                result["totalAmount"] = match.group(1) + " 元"
                break

        # 单价
        unitPatterns = [
            r'单价[为:]?\s*(\d{1,3}(?:,\d{3})*)\s*元/年',
            r'单价[为:]?\s*(\d{1,3}(?:,\d{3})*)\s*元',
        ]
        for pattern in unitPatterns:
            match = re.search(pattern, content)
            if match:
                result["unitPrice"] = match.group(1) + " 元/年"
                break

        return result

    def extractServiceTerm(self, content: str) -> Dict[str, Any]:
        """提取服务期信息"""
        result = {}

        # 服务期
        termMatch = re.search(r'服务期为每期(\d+)年', content)
        if termMatch:
            result["serviceTermYears"] = termMatch.group(1) + "年"

        # 月数
        monthMatch = re.search(r'服务期为每期(\d+)个月', content)
        if monthMatch:
            result["serviceTermMonths"] = monthMatch.group(1) + "个月"

        # 也匹配 "60个月" 这种格式
        if "serviceTermYears" not in result and "serviceTermMonths" not in result:
            monthTotal = re.search(r'(\d+)\s*个月', content)
            if monthTotal:
                result["serviceTermMonths"] = monthTotal.group(1) + "个月"

        # 预计开通时间
        startMatch = re.search(r'预计开通时间为(\d{4})年(\d{1,2})月(\d{1,2})日', content)
        if startMatch:
            result["expectedStartDate"] = f"{startMatch.group(1)}年{startMatch.group(2)}月{startMatch.group(3)}日"

        return result

    def extractPaymentInfo(self, content: str) -> Dict[str, Any]:
        """提取付款方式信息"""
        result = {}

        # 付款周期
        payCycleMatch = re.search(r'付款周期[：:]?\s*([^\n]{5,80})', content)
        if payCycleMatch:
            result["paymentCycle"] = payCycleMatch.group(1).strip()

        # 付款方式
        payMethodMatch = re.search(r'付款方式[：:]?\s*([^\n]{5,80})', content)
        if payMethodMatch:
            result["paymentMethod"] = payMethodMatch.group(1).strip()

        # 预付保证期
        prepayMatch = re.search(r'预付保证期[为:]?\s*(\d+)\s*天', content)
        if prepayMatch:
            result["prepaymentGuaranteeDays"] = prepayMatch.group(1) + "天"

        return result

    def extractSigningInfo(self, content: str) -> Dict[str, Any]:
        """提取签订信息"""
        result = {}

        # 签订地点
        placeMatch = re.search(r'签订地点[：:]?\s*([^\n]{5,50})', content)
        if placeMatch:
            result["signingPlace"] = placeMatch.group(1).strip()

        # 税率
        taxMatch = re.search(r'税率[：:]?\s*(\d+%)', content)
        if taxMatch:
            result["taxRate"] = taxMatch.group(1)

        # 签订日期
        dateMatch = re.search(r'签订日期[：:]?\s*(\d{4})年(\d{1,2})月(\d{1,2})日', content)
        if dateMatch:
            result["signingDate"] = f"{dateMatch.group(1)}年{dateMatch.group(2)}月{dateMatch.group(3)}日"

        return result

    def extractDefaultTerms(self, content: str) -> Dict[str, Any]:
        """提取违约条款信息"""
        result = {}

        # 违约金
        breachMatch = re.search(r'需支付.*?(\d+)%.*?合同金额', content)
        if breachMatch:
            result["breachPenaltyPercentage"] = breachMatch.group(1) + "%"

        # 提前终止
        terminationMatch = re.search(r'提前终止.*?支付.*?(\d+)%', content)
        if terminationMatch:
            result["earlyTerminationPenalty"] = terminationMatch.group(1) + "%"

        return result

    def extractAll(self, content: str) -> Dict[str, Any]:
        """
        提取所有类型的条款信息

        Args:
            content: 文档文本内容

        Returns:
            包含所有提取结果的字典
        """
        return {
            "success": True,
            "parties": self.extractParties(content),
            "dates": self.extractDates(content),
            "amounts": self.extractAmounts(content),
            "deadlines": self.extractDeadlines(content),
            "contacts": self.extractContacts(content),
            "contractAmount": self.extractContractAmount(content),
            "serviceTerm": self.extractServiceTerm(content),
            "paymentInfo": self.extractPaymentInfo(content),
            "signingInfo": self.extractSigningInfo(content),
            "defaultTerms": self.extractDefaultTerms(content)
        }

    def extractByInstruction(self, content: str, instruction: str) -> Dict[str, Any]:
        """
        根据自然语言指令提取信息

        Args:
            content: 文档文本内容
            instruction: 提取指令，如 "提取所有金额信息"

        Returns:
            提取结果
        """
        instructionLower = instruction.lower()

        # 解析指令
        if "金额" in instruction or "amount" in instructionLower:
            return {
                "instruction": instruction,
                "result": self.extractAmounts(content)
            }
        elif "日期" in instruction or "date" in instructionLower:
            return {
                "instruction": instruction,
                "result": self.extractDates(content)
            }
        elif "当事人" in instruction or "party" in instructionLower or "签署方" in instruction:
            return {
                "instruction": instruction,
                "result": self.extractParties(content)
            }
        elif "截止" in instruction or "deadline" in instructionLower or "期限" in instruction:
            return {
                "instruction": instruction,
                "result": self.extractDeadlines(content)
            }
        elif "联系" in instruction or "contact" in instructionLower:
            return {
                "instruction": instruction,
                "result": self.extractContacts(content)
            }
        elif "所有" in instruction or "all" in instructionLower:
            return {
                "instruction": instruction,
                "result": self.extractAll(content)
            }
        else:
            # 默认提取所有
            return {
                "instruction": instruction,
                "result": self.extractAll(content)
            }


def extractClauses(content: str, instruction: Optional[str] = None) -> Dict[str, Any]:
    """
    便捷函数：提取条款信息

    Args:
        content: 文档文本内容
        instruction: 可选的提取指令

    Returns:
        提取结果
    """
    extractor = clauseExtractor()

    if instruction:
        return extractor.extractByInstruction(content, instruction)
    else:
        return extractor.extractAll(content)


# Claude Code 技能指令模板
extractionInstructions = {
    "extractParties": "提取合同当事人信息（甲方、乙方等）",
    "extractDates": "提取所有日期信息",
    "extractAmounts": "提取所有金额信息",
    "extractDeadlines": "提取截止日期/期限信息",
    "extractContacts": "提取联系方式（电话、邮箱、地址）",
    "extractAll": "提取所有关键信息",
    "custom": "根据自定义指令提取信息"
}


