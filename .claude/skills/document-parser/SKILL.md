---
name: document-parser
description: 文档解析技能 - 用于解析 doc、docx、pdf 文件内容并提取文本信息。支持 .docx、.doc、.pdf 格式，提取段落、表格、页码等完整内容。
triggers:
  - 读取 doc 文件
  - 读取 docx 文件
  - 读取 pdf 文件
  - 解析 doc 文件
  - 解析 docx 文件
  - 解析 pdf 文件
  - 提取文档内容
  - document parser
  - 文档解析
---

## 支持的文件格式

- `.docx` - Microsoft Word 2007+ 格式
- `.doc` - Microsoft Word 97-2003 格式（支持有限）
- `.pdf` - PDF 文档

## 使用方法

### 1. 在 Claude Code 中使用

当用户上传 doc/docx/pdf 文件并希望读取内容时：
- "帮我读取这个合同文件 contract.pdf"
- "解析这个 docx 文档"
- "提取文档内容"

Claude Code 会自动调用 document-parser 技能解析该文件。


### 2. 命令行调用

```bash
python .claude/skills/document-parser/src/parser.py <文件路径>
```

## 输出格式

解析结果包含以下字段：
- **success**: 是否解析成功
- **format**: 文件格式（pdf/docx/doc）
- **file_name**: 文件名
- **file_path**: 文件路径
- **content**: 文档全文内容
- **page_count**: 页数
- **pages**: 分页内容列表

## 错误处理

- `FileNotFoundError`: 文件不存在
- `ValueError`: 不支持的文件格式

## 代码位置

技能代码位于: `.claude/skills/document-parser/src/`
