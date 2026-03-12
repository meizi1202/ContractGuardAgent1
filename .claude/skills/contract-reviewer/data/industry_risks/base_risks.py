# 通用风险规则库

baseRisks = {
    "industry": "general",
    "name": "通用风险规则",
    "version": "1.0",
    "description": "适用于所有类型合同的通用风险规则",
    "riskCategories": [
        {
            "category": "amount",
            "name": "金额风险",
            "description": "合同金额相关风险",
            "risks": [
                {
                    "id": "AMT001",
                    "level": "critical",
                    "name": "合同金额未明确",
                    "patterns": [
                        r"金额.*未确定",
                        r"金额.*待定",
                        r"金额.*另行约定",
                        r"金额.*不确定",
                        r"总金额.*暂定"
                    ],
                    "suggestion": "建议明确约定具体金额",
                    "legalReference": "《民法典》第543条"
                },
                {
                    "id": "AMT002",
                    "level": "warning",
                    "name": "金额大小写不一致",
                    "patterns": [
                        r"(\d+)元.*[零壹贰叁肆伍陆柒捌玖拾佰仟萬]+",
                        r"[零壹贰叁肆伍陆柒捌玖拾佰仟萬]+.*(\d+)元"
                    ],
                    "suggestion": "核对大小写金额是否一致",
                    "legalReference": None
                }
            ]
        },
        {
            "category": "term",
            "name": "期限风险",
            "description": "合同期限相关风险",
            "risks": [
                {
                    "id": "TRM001",
                    "level": "warning",
                    "name": "合同期限过长",
                    "patterns": [
                        r"期限.*[1-9]\d{1,2}年",
                        r"永久",
                        r"无固定期限",
                        r"长期有效"
                    ],
                    "suggestion": "建议设置合理期限，并约定续期条件",
                    "legalReference": None
                },
                {
                    "id": "TRM002",
                    "level": "warning",
                    "name": "期限约定不明确",
                    "patterns": [
                        r"期限.*另行通知",
                        r"有效期.*待定",
                        r"开始时间.*待定"
                    ],
                    "suggestion": "明确约定合同起止时间",
                    "legalReference": None
                }
            ]
        },
        {
            "category": "liability",
            "name": "责任风险",
            "description": "违约责任相关风险",
            "risks": [
                {
                    "id": "LIA001",
                    "level": "warning",
                    "name": "单方面免责条款",
                    "patterns": [
                        r"免责",
                        r"不承担.*责任",
                        r"概不负责",
                        r"不负.*任何责任",
                        r"乙方.*免责"
                    ],
                    "suggestion": "注意免责条款的合理性，双方责任应对等",
                    "legalReference": "《民法典》第497条"
                },
                {
                    "id": "LIA002",
                    "level": "critical",
                    "name": "违约金比例过高",
                    "patterns": [
                        r"违约金.*[3-9]\d%",
                        r"违约金.*1\d\d%",
                        r"日息.*千分之[5-9]",
                        r"日息.*百分之[5-9]"
                    ],
                    "suggestion": "违约金过高的，可能不受法律保护",
                    "legalReference": "《民法典》第585条"
                }
            ]
        },
        {
            "category": "termination",
            "name": "终止风险",
            "description": "合同终止相关风险",
            "risks": [
                {
                    "id": "TRM003",
                    "level": "warning",
                    "name": "单方面解除限制",
                    "patterns": [
                        r"不得解除",
                        r"不可终止",
                        r"单方面.*解除.*无效",
                        r"不得.*提前终止"
                    ],
                    "suggestion": "注意解约条款的公平性，保障双方权利",
                    "legalReference": "《民法典》第562条"
                },
                {
                    "id": "TRM004",
                    "level": "warning",
                    "name": "终止条件不对等",
                    "patterns": [
                        r"甲方.*有权.*终止",
                        r"乙方.*无权.*终止"
                    ],
                    "suggestion": "确保双方终止权利对等",
                    "legalReference": None
                }
            ]
        },
        {
            "category": "dispute",
            "name": "争议解决风险",
            "description": "争议解决条款相关风险",
            "risks": [
                {
                    "id": "DSP001",
                    "level": "info",
                    "name": "争议解决条款缺失",
                    "patterns": [
                        r"争议.*未约定",
                        r"纠纷.*另行协商"
                    ],
                    "suggestion": "建议补充争议解决条款",
                    "legalReference": None
                },
                {
                    "id": "DSP002",
                    "level": "info",
                    "name": "管辖约定不明",
                    "patterns": [
                        r"管辖.*待定",
                        r"法院.*另行约定"
                    ],
                    "suggestion": "明确约定管辖法院",
                    "legalReference": "《民事诉讼法》第34条"
                }
            ]
        }
    ],
    # 行业识别关键词
    "industryKeywords": {
        "procurement": ["采购", "供货", "供应", "买卖", "订购", "供应商"],
        "leasing": ["租赁", "租用", "出租", "承租", "租金", "房东", "租户"],
        "service": ["服务", "咨询", "顾问", "代理", "委托"],
        "construction": ["建设", "施工", "工程", "装修", "承包"],
        "technology": ["开发", "软件", "系统", "平台", "技术"]
    }
}
