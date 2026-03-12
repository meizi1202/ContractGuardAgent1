# 租赁合同风险规则库

leasingRisks = {
    "industry": "leasing",
    "name": "租赁合同",
    "version": "1.0",
    "description": "适用于租赁、租用类合同的风险规则",
    "riskCategories": [
        {
            "category": "rent",
            "name": "租金风险",
            "description": "租金相关风险",
            "risks": [
                {
                    "id": "LEA_RNT001",
                    "level": "critical",
                    "name": "租金约定不明确",
                    "patterns": [
                        r"租金.*另行协商",
                        r"租金.*待定",
                        r"租金.*未约定"
                    ],
                    "suggestion": "明确约定租金金额、支付方式和支付时间",
                    "legalReference": "《民法典》第704条"
                },
                {
                    "id": "LEA_RNT002",
                    "level": "warning",
                    "name": "租金调整机制缺失",
                    "patterns": [
                        r"租金.*不可调整",
                        r"租金.*不再变动",
                        r"租金.*保持不变"
                    ],
                    "suggestion": "建议约定租金调整机制，应对市场变化",
                    "legalReference": None
                },
                {
                    "id": "LEA_RNT003",
                    "level": "warning",
                    "name": "押金退还条件不清",
                    "patterns": [
                        r"押金.*不予退还",
                        r"押金.*退还.*另行约定",
                        r"押金.*退还.*条件.*未明确"
                    ],
                    "suggestion": "明确押金退还条件和时限",
                    "legalReference": "《民法典》第721条"
                },
                {
                    "id": "LEA_RNT004",
                    "level": "warning",
                    "name": "逾期滞纳金过高",
                    "patterns": [
                        r"滞纳金.*日.*千分之",
                        r"逾期.*罚款.*\d+%",
                        r"滞纳金.*超过.*本金"
                    ],
                    "suggestion": "滞纳金过高的可能不受法律保护",
                    "legalReference": "《民法典》第585条"
                }
            ]
        },
        {
            "category": "usage",
            "name": "使用风险",
            "description": "租赁物使用相关风险",
            "risks": [
                {
                    "id": "LEA_USG001",
                    "level": "warning",
                    "name": "用途限制过严",
                    "patterns": [
                        r"仅限.*使用",
                        r"不得.*改变.*用途",
                        r"擅自.*用途.*违约"
                    ],
                    "suggestion": "用途限制应合理",
                    "legalReference": None
                },
                {
                    "id": "LEA_USG002",
                    "level": "critical",
                    "name": "转租限制不合理",
                    "patterns": [
                        r"不得.*转租",
                        r"禁止.*转租.*任何.*情况",
                        r"转租.*须.*支付.*高额.*违约金"
                    ],
                    "suggestion": "应允许在一定条件下转租",
                    "legalReference": "《民法典》第716条"
                },
                {
                    "id": "LEA_USG003",
                    "level": "warning",
                    "name": "装修限制过严",
                    "patterns": [
                        r"不得.*装修",
                        r"禁止.*改造",
                        r"装修.*须.*支付.*高额.*费用"
                    ],
                    "suggestion": "装修限制应合理",
                    "legalReference": "《民法典》第715条"
                },
                {
                    "id": "LEA_USG004",
                    "level": "info",
                    "name": "日常维护责任不明",
                    "patterns": [
                        r"维护.*责任.*未约定",
                        r"维修.*另行协商"
                    ],
                    "suggestion": "明确日常维护责任划分",
                    "legalReference": "《民法典》第712条"
                }
            ]
        },
        {
            "category": "maintenance",
            "name": "维修风险",
            "description": "维修责任相关风险",
            "risks": [
                {
                    "id": "LEA_MTN001",
                    "level": "warning",
                    "name": "维修责任不清",
                    "patterns": [
                        r"维修.*责任.*未约定",
                        r"维修.*另行协商",
                        r"所有.*维修.*乙方.*承担"
                    ],
                    "suggestion": "明确出租人和承租人的维修责任",
                    "legalReference": "《民法典》第712条"
                },
                {
                    "id": "LEA_MTN002",
                    "level": "warning",
                    "name": "维护标准缺失",
                    "patterns": [
                        r"维护标准.*未约定",
                        r"维护要求.*另行通知"
                    ],
                    "suggestion": "明确租赁物的维护标准和要求",
                    "legalReference": None
                },
                {
                    "id": "LEA_MTN003",
                    "level": "warning",
                    "name": "维修响应时间过长",
                    "patterns": [
                        r"维修.*\d+.*工作日",
                        r"维修.*\d+.*天后.*响应"
                    ],
                    "suggestion": "维修响应时间应合理",
                    "legalReference": None
                }
            ]
        },
        {
            "category": "termination",
            "name": "终止风险",
            "description": "合同终止相关风险",
            "risks": [
                {
                    "id": "LEA_TER001",
                    "level": "critical",
                    "name": "提前解约条件不对等",
                    "patterns": [
                        r"甲方.*有权.*随时.*终止",
                        r"乙方.*不得.*提前.*终止",
                        r"甲方.*终止.*无须.*赔偿"
                    ],
                    "suggestion": "确保双方提前解约权利对等",
                    "legalReference": "《民法典》第722条"
                },
                {
                    "id": "LEA_TER002",
                    "level": "warning",
                    "name": "续租优先权缺失",
                    "patterns": [
                        r"无.*优先续租权",
                        r"续租.*另行协商",
                        r"优先续租.*未约定"
                    ],
                    "suggestion": "建议约定承租人优先续租权",
                    "legalReference": "《民法典》第732条"
                },
                {
                    "id": "LEA_TER003",
                    "level": "warning",
                    "name": "解约赔偿不对等",
                    "patterns": [
                        r"甲方.*违约.*赔偿.*\d+%.+乙方.*违约.*赔偿"
                    ],
                    "suggestion": "双方解约赔偿条件应大致对等",
                    "legalReference": None
                },
                {
                    "id": "LEA_TER004",
                    "level": "warning",
                    "name": "提前解约通知期过长",
                    "patterns": [
                        r"提前.*\d+.*个月.*通知",
                        r"终止.*须.*\d+.*个月.*书面"
                    ],
                    "suggestion": "提前解约通知期应合理",
                    "legalReference": None
                }
            ]
        },
        {
            "category": "condition",
            "name": "物况风险",
            "description": "租赁物状况相关风险",
            "risks": [
                {
                    "id": "LEA_CON001",
                    "level": "critical",
                    "name": "交付标准不明确",
                    "patterns": [
                        "交付标准.*另行约定",
                        r"交付.*状态.*未明确"
                    ],
                    "suggestion": "明确租赁物交付时的状态和标准",
                    "legalReference": "《民法典》第708条"
                },
                {
                    "id": "LEA_CON002",
                    "level": "warning",
                    "name": "瑕疵担保责任免除",
                    "patterns": [
                        r"不承担.*瑕疵.*责任",
                        r"交付.*现状.*为准",
                        r"瑕疵.*乙方.*自行.*负责"
                    ],
                    "suggestion": "出租人应对租赁物承担瑕疵担保责任",
                    "legalReference": "《民法典》第731条"
                },
                {
                    "id": "LEA_CON003",
                    "level": "info",
                    "name": "返还标准缺失",
                    "patterns": [
                        r"返还.*标准.*未约定",
                        r"返还.*状态.*另行协商"
                    ],
                    "suggestion": "明确租赁物返还时的标准",
                    "legalReference": "《民法典》第733条"
                }
            ]
        }
    ],
    # 行业识别关键词
    "industryKeywords": {
        "leasing": ["租赁", "租用", "出租", "承租", "租金", "房东", "租户", "房屋租赁", "设备租赁", "场地租赁"]
    }
}
