---
name: clause-extractor
description: 条款提取技能 - 从文档内容中提取关键信息，包括合同当事人、日期、金额、截止日期、联系方式等。仅提供提取指令，由 Claude Code 执行信息提取。
triggers:
  - 提取关键信息
  - 提取金额
  - 提取日期
  - 提取当事人
  - 提取条款
  - clause extractor
  - 条款提取
  - 提取联系人信息
  - 提取截止日期
  - 从文档中提取信息
---

# clause-extractor

条款提取技能 - 用于从文档内容中提取关键信息

## 功能描述

获取 document-parser 技能解析的内容信息，执行关键信息提取。此技能仅提供提取关键信息的指令，由 Claude Code 获取相关指令后执行信息提取。

## 提取的信息类型

### 1. 合同当事人 (parties)
- 甲方、乙方、丙方等
- 当事人名称

### 2. 日期信息 (dates)
- 签订日期
- 生效日期
- 截止日期

### 3. 金额信息 (amounts)
- 合同金额
- 付款金额
- 各种费用

### 4. 截止日期/期限 (deadlines)
- 履行期限
- 服务期
- 有效期

### 5. 联系方式 (contacts)
- 电话号码
- 邮箱地址
- 联系地址

## 使用方法

### 1. 在 Claude Code 中使用

当用户需要从文档中提取关键信息时：
- "从这个合同中提取所有金额信息"
- "提取合同当事人"
- "提取日期和截止日期"
- "提取联系方式"

Claude Code 会：
1. 检查是否已有解析内容
2. 如果没有，先使用 document-parser 解析文档
3. 使用 clause-extractor 提取相关信息

### 2. Python 代码调用

```python
from clause_extractor import ClauseExtractor

# 创建提取器实例
extractor = ClauseExtractor()

# 文档内容（通常来自 document-parser）
content = """
合同编号：2024001
甲方：北京科技有限公司
乙方：上海贸易有限公司
签订日期：2024年1月15日
合同金额：人民币100万元
"""

# 提取所有关键信息
result = extractor.extract_all(content)

# 或根据指令提取
result = extractor.extract_by_instruction(content, "提取所有金额信息")
```

### 3. 命令行调用

```bash
python .claude/skills/clause-extractor/src/extractor.py <提取指令>
```

## 提取指令示例

| 指令 | 说明 |
|------|------|
| 提取所有金额信息 | 提取合同中的金额数据 |
| 提取日期信息 | 提取所有日期相关内容 |
| 提取当事人 | 提取甲方、乙方等当事人信息 |
| 提取截止日期 | 提取期限和截止时间 |
| 提取联系方式 | 提取电话、邮箱、地址 |
| 提取所有 | 提取所有关键信息 |

## 输出格式

提取结果包含以下结构化信息：
- **parties**: 合同当事人信息
- **dates**: 日期信息列表
- **amounts**: 金额信息列表
- **deadlines**: 期限信息列表
- **contacts**: 联系方式（电话、邮箱、地址）

## 代码位置

技能代码位于: `.claude/skills/clause-extractor/src/`
