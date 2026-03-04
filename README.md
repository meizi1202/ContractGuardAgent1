# ContractGuardAgent1

一个用于**合同审查**的 Claude Code 智能体，提供完整的合同审查流程。

## 功能特性

- 📄 **文档解析** - 支持解析 doc、docx、pdf 格式的合同文档
- 🔍 **条款提取** - 自动提取合同当事人、日期、金额、截止日期、联系方式等关键信息
- ✅ **合规性审查** - 检查合同条款是否符合规范
- ⚠️ **风险提示** - 识别潜在风险并给出改进建议

## 支持的技能

| 技能 | 触发词 | 功能 |
|------|--------|------|
| 合同审查 | 合同审查、审查合同、分析合同 | 完整审查流程：解析+提取+审查+风险提示 |
| 条款提取 | 提取关键信息、提取金额、提取日期 | 从合同中提取当事人、日期、金额等 |
| 文档解析 | 解析文档、提取文本 | 解析 doc/docx/pdf 文件 |

## 项目结构

```
ContractGuardAgent1/
├── contracts/               # 合同文档存放目录
├── docs/                   # 项目文档
├── tests/                  # 测试文件
└── .claude/
    ├── settings.json       # Claude Code 设置
    ├── rules/              # 项目规范
    │   ├── python-coding-standards.md   # Python 编码规范
    │   ├── project-documentation.md      # 文档规范
    │   └── code-comments.md             # 注释规范
    └── skills/             # 技能模块
        ├── contract-reviewer/           # 合同审查主技能
        ├── clause-extractor/            # 条款提取技能
        └── document-parser/             # 文档解析技能
```

## 审查维度

### 合规性检查
- 合同要素是否完整
- 条款是否合法合规
- 格式是否符合标准

### 风险评估
- 金额风险
- 期限风险
- 违约责任
- 权利义务不对等
- 其他潜在风险

## 使用方法

在 Claude Code 中使用以下触发词：

```
合同审查        # 启动完整合同审查流程
审查合同        # 审查合同内容
分析合同        # 分析合同条款

提取关键信息    # 提取合同中的关键信息
提取金额        # 提取合同中的金额信息
提取日期        # 提取合同中的日期信息

解析文档        # 解析合同文档
提取文本        # 提取文档文本内容
```

## 技术栈

- **Python** - 主要开发语言
- **python-docx** - Word 文档解析
- **PyPDF2** - PDF 文档解析
- **Claude Code** - AI 智能体框架

## 规范说明

- 遵循 [Python 编码规范](.claude/rules/python-coding-standards.md)
- 遵循 [代码注释规范](.claude/rules/code-comments.md)
- 遵循 [项目文档规范](.claude/rules/project-documentation.md)

## 许可证

MIT License
