"""document-parser: 文档解析技能

用于解析 doc, docx, pdf 文件内容
"""

__version__ = "1.1.0"

from .parser import DocumentParser, parse_document, parse_document_to_json

__all__ = [
    "DocumentParser",
    "parse_document",
    "parse_document_to_json"
]
