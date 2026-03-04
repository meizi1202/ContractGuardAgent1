---
name: contract-reviewer
description: 合同审查智能体 - 完整合同审查流程：解析文档 + 提取关键信息 + 合规性审查 + 风险提示
triggers:
  - 合同审查
  - 审查合同
  - 分析合同
  - 合同风险
  - 合同合规
  - contract reviewer
  - 合同检查
---

# contract-reviewer

合同审查智能体 - 提供完整的合同审查流程服务

## 功能描述

整合文档解析、条款提取、合规性审查和风险提示的完整合同审查流程。自动完成从文档解析到风险报告输出的全流程。

## 审查流程

当用户请求合同审查时，按以下步骤执行：

### Step 1: 文档解析
使用 `/document-parser` 解析合同文件（支持 .doc, .docx, .pdf）

### Step 2: 条款提取
使用 `/clause-extractor` 提取关键信息：
- 合同当事人
- 签订日期、生效日期
- 合同金额、付款方式
- 履行期限、截止日期
- 联系方式

### Step 3: 合规性审查
检查合同要素：
- [ ] 合同主体是否明确
- [ ] 权利义务是否对等
- [ ] 违约责任是否清晰
- [ ] 争议解决条款是否完整
- [ ] 合同期限是否明确

### Step 4: 风险评估
识别潜在风险：
- 金额风险（金额不明确、付款条件不利）
- 期限风险（期限过长、续约条款不清晰）
- 责任风险（违约责任不对等、免责条款过多）
- 终止风险（退出机制、解约条件）
- 其他风险

## 使用方法

在 Claude Code 中直接触发：

| 触发方式 | 示例 |
|----------|------|
| 完整审查 | "帮我审查这份合同" |
| 指定文件 | "审查 contracts/协议.docx" |
| 只看风险 | "分析这份合同的风险" |
| 检查合规 | "检查合同是否符合规范" |

## 输出报告

审查完成后，生成结构化报告：

```json
{
  "success": true,
  "summary": {
    "totalIssues": 5,
    "critical": 1,
    "warning": 2,
    "info": 2
  },
  "extractedInfo": {
    "parties": ["甲方: xxx", "乙方: xxx"],
    "amount": "人民币100万元",
    "dates": {"signDate": "2024-01-15", "startDate": "2024-01-20"}
  },
  "compliance": {
    "complete": true,
    "missingClauses": []
  },
  "risks": [
    {
      "level": "critical",
      "type": "金额风险",
      "description": "合同金额未明确约定",
      "suggestion": "建议补充明确金额条款"
    }
  ]
}
```

## 代码位置

技能代码位于: `.claude/skills/contract-reviewer/src/`

## 依赖技能

- `/document-parser` - 文档解析
- `/clause-extractor` - 条款提取
