# 采购合同风险规则库

procurementRisks = {
    "industry": "procurement",
    "name": "采购合同",
    "version": "1.0",
    "description": "适用于采购、供货、买卖类合同的风险规则",
    "riskCategories": [
        {
            "category": "payment",
            "name": "付款风险",
            "description": "采购合同付款相关风险",
            "risks": [
                {
                    "id": "PUR_PAY001",
                    "level": "critical",
                    "name": "付款条件不明确",
                    "patterns": [
                        r"付款方式.*待定",
                        r"付款时间.*另行通知",
                        r"付款.*另行协商",
                        r"付款.*未约定"
                    ],
                    "suggestion": "明确约定付款方式、付款时间和付款比例",
                    "legalReference": "《民法典》第628条"
                },
                {
                    "id": "PUR_PAY002",
                    "level": "critical",
                    "name": "预付款比例过高",
                    "patterns": [
                        r"预付款.*[7-9]\d%",
                        r"预付款.*100%",
                        r"预付.*金额.*超过.*合同总价"
                    ],
                    "suggestion": "预付款比例过高会增加采购方风险，建议控制在30%以内",
                    "legalReference": None
                },
                {
                    "id": "PUR_PAY003",
                    "level": "warning",
                    "name": "验收后付款延迟",
                    "patterns": [
                        r"验收.*\d+.*日后.*付款",
                        r"验收后.*个月.*付款",
                        r"尾款.*验收.*\d+.*天"
                    ],
                    "suggestion": "明确验收标准和付款时限",
                    "legalReference": None
                },
                {
                    "id": "PUR_PAY004",
                    "level": "warning",
                    "name": "付款条件过于苛刻",
                    "patterns": [
                        r"付款.*须.*完全.*满意",
                        r"付款.*须.*甲方.*书面确认"
                    ],
                    "suggestion": "付款条件应具体可执行",
                    "legalReference": None
                }
            ]
        },
        {
            "category": "delivery",
            "name": "交付风险",
            "description": "货物交付相关风险",
            "risks": [
                {
                    "id": "PUR_DEL001",
                    "level": "critical",
                    "name": "交付标准不清",
                    "patterns": [
                        r"交付标准.*待定",
                        r"交付.*另行约定",
                        r"货物.*规格.*未明确"
                    ],
                    "suggestion": "明确货物的规格、型号、数量、质量标准",
                    "legalReference": "《民法典》第511条"
                },
                {
                    "id": "PUR_DEL002",
                    "level": "warning",
                    "name": "交货地点不明确",
                    "patterns": [
                        r"交货地点.*待定",
                        r"交货地点.*另行通知",
                        r"交货.*地点.*未约定"
                    ],
                    "suggestion": "明确交货地点及运输费用承担",
                    "legalReference": None
                },
                {
                    "id": "PUR_DEL003",
                    "level": "warning",
                    "name": "验收流程缺失",
                    "patterns": [
                        r"验收.*未约定",
                        r"验收.*另行协商",
                        r"无需.*验收"
                    ],
                    "suggestion": "明确验收标准、流程和时限",
                    "legalReference": "《民法典》第620条"
                },
                {
                    "id": "PUR_DEL004",
                    "level": "warning",
                    "name": "交货时间不明确",
                    "patterns": [
                        r"交货时间.*待定",
                        r"交货.*另行通知",
                        r"交付时间.*未约定"
                    ],
                    "suggestion": "明确具体交货时间和分期交货安排",
                    "legalReference": None
                }
            ]
        },
        {
            "category": "quality",
            "name": "质量风险",
            "description": "货物质量相关风险",
            "risks": [
                {
                    "id": "PUR_QLT001",
                    "level": "critical",
                    "name": "质量标准模糊",
                    "patterns": [
                        r"质量.*符合.*相关标准",
                        r"质量.*达到.*行业标准",
                        r"质量.*按照.*国家标准",
                        r"质量.*良好.*即可"
                    ],
                    "suggestion": "明确具体质量标准，最好有量化指标",
                    "legalReference": "《民法典》第509条"
                },
                {
                    "id": "PUR_QLT002",
                    "level": "warning",
                    "name": "保修期不合理",
                    "patterns": [
                        r"保修期.*少于.*\d+个月",
                        r"无保修",
                        r"不享受.*保修",
                        r"质保期.*\d+个月.*以内"
                    ],
                    "suggestion": "根据产品特性约定合理保修期",
                    "legalReference": "《产品质量法》第40条"
                },
                {
                    "id": "PUR_QLT003",
                    "level": "warning",
                    "name": "检验方法不明确",
                    "patterns": [
                        r"检验方法.*另行约定",
                        r"以.*甲方.*检验.*为准"
                    ],
                    "suggestion": "明确检验方法和标准",
                    "legalReference": "《民法典》第620条"
                },
                {
                    "id": "PUR_QLT004",
                    "level": "warning",
                    "name": "质量异议期限过短",
                    "patterns": [
                        r"异议期.*\d+天",
                        r"质量.*问题.*\d+天内.*提出"
                    ],
                    "suggestion": "质量异议期限应合理",
                    "legalReference": None
                }
            ]
        },
        {
            "category": "penalty",
            "name": "违约风险",
            "description": "违约责任相关风险",
            "risks": [
                {
                    "id": "PUR_PEN001",
                    "level": "critical",
                    "name": "违约金比例失衡",
                    "patterns": [
                        r"甲方.*违约金.*\d+%.+乙方.*违约金",
                        r"乙方.*违约金.*比例.*高于.*甲方"
                    ],
                    "suggestion": "双方违约金比例应大致对等",
                    "legalReference": "《民法典》第585条"
                },
                {
                    "id": "PUR_PEN002",
                    "level": "warning",
                    "name": "逾期交货责任过轻",
                    "patterns": [
                        r"逾期交货.*仅.*支付.*\d+%",
                        r"逾期.*赔偿.*不超过.*合同金额"
                    ],
                    "suggestion": "逾期交货责任应与采购方损失相当",
                    "legalReference": None
                },
                {
                    "id": "PUR_PEN003",
                    "level": "warning",
                    "name": "单方面终止责任不对等",
                    "patterns": [
                        r"甲方.*终止.*须.*赔偿",
                        r"乙方.*终止.*不.*承担.*责任"
                    ],
                    "suggestion": "确保双方终止合同的责任对等",
                    "legalReference": None
                }
            ]
        },
        {
            "category": "title",
            "name": "所有权风险",
            "description": "货物所有权相关风险",
            "risks": [
                {
                    "id": "PUR_TTL001",
                    "level": "warning",
                    "name": "所有权转移时间不明确",
                    "patterns": [
                        r"所有权.*另行约定",
                        r"所有权.*转移.*时间.*未约定"
                    ],
                    "suggestion": "明确所有权转移时间和条件",
                    "legalReference": "《民法典》第224条"
                },
                {
                    "id": "PUR_TTL002",
                    "level": "info",
                    "name": "知识产权归属不清",
                    "patterns": [
                        r"知识产权.*另行协商",
                        r"技术.*成果.*归属.*未明确"
                    ],
                    "suggestion": "明确知识产权归属",
                    "legalReference": None
                }
            ]
        }
    ],
    # 行业识别关键词
    "industryKeywords": {
        "procurement": ["采购", "供货", "供应", "买卖", "订购", "供应商", "货物", "产品", "设备", "材料"]
    }
}
