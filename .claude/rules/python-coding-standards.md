# Python 编码规范

本项目使用 **全驼峰命名 (camelCase)** 作为 Python 代码的命名规范。

## 命名规范

### 类名
- 使用 camelCase，首字母小写
- 示例：`clauseExtractor`, `documentParser`, `contractValidator`

### 函数名
- 使用 camelCase
- 示例：`extractParties`, `parseDocument`, `validateContract`

### 变量名
- 使用 camelCase
- 示例：`clausePatterns`, `filePath`, `extractedData`

### 常量
- 避免使用全大写，全部使用 camelCase
- 示例：`maxRetryCount` (不要用 MAX_RETRY_COUNT)

### 私有成员
- 私有方法和属性使用单下划线前缀 + camelCase
- 示例：`_parseDocx`, `_internalCache`

## 代码风格

### 缩进
- 使用 4 空格缩进

### 行长度
- 最大行长度 100 字符

### 导入
- 标准库 → 第三方库 → 本地模块
- 按字母顺序排列
- 示例：
  ```python
  import json
  import re
  from pathlib import Path
  from typing import Dict, Any, List, Optional

  from docx import Document
  from PyPDF2 import PdfReader

  from .clauseExtractor import clauseExtractor
  from .documentParser import documentParser
  ```

### 文档字符串
- 使用中文或英文皆可，保持一致
- 使用 Google 风格或 NumPy 风格
- 示例：
  ```python
  def extractParties(content: str) -> Dict[str, Any]:
      """Extract party information from contract content.

      Args:
          content: The text content of the contract

      Returns:
          Dictionary containing party information
      """
  ```

### 类型注解
- 为函数参数和返回值添加类型注解
- 示例：
  ```python
  def parseDocument(filePath: str) -> Dict[str, Any]:
      ...
  ```

## 最佳实践

### 单一职责
- 每个类/函数应该只有一个职责

### 避免魔法数字
- 使用有名称的常量替代
  ```python
  # 不推荐
  if status == 1:

  # 推荐
  ACTIVE_STATUS = 1
  if status == ACTIVE_STATUS:
  ```

### 错误处理
- 使用具体的异常类型
- 提供有意义的错误信息

### 性能考虑
- 避免在循环中进行字符串拼接
- 使用列表推导式代替简单循环
- 合理使用生成器处理大数据集

### 命令行与脚本规范
- **避免在 Bash 命令中直接编写复杂逻辑**：将功能实现封装到独立的 Python 文件中
- 使用 `python script.py` 调用脚本，而不是用 `python -c "..."` 执行复杂代码
- 保持命令行工具简洁，复杂逻辑放在模块代码中

### 中文编码处理
- **模块级别编码配置**：涉及中文输出的模块应在文件开头（import 之后）设置编码
- **Windows 兼容性**：在 Windows 环境下，标准输出默认不是 UTF-8，需要显式配置
- **配置方式**：
  ```python
  import sys
  import os

  if sys.platform == 'win32':
      if sys.stdout.encoding != 'utf-8':
          try:
              sys.stdout.reconfigure(encoding='utf-8')
          except Exception:
              os.environ['PYTHONIOENCODING'] = 'utf-8'
  ```
- **注意**：编码配置必须放在文件最开头（在任何其他代码之前），确保在模块被 import 时就生效，而不是只在 main() 函数中设置
