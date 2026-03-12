"""文档解析器测试"""

import sys
import os

# 模块级别编码配置 - 解决 Windows 控制台中文乱码问题
# 必须在任何其他代码之前执行
if sys.platform == 'win32':
    # 设置标准输出/错误编码为 UTF-8
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            # 如果无法重新配置，则设置环境变量
            os.environ['PYTHONIOENCODING'] = 'utf-8'
    if sys.stderr.encoding != 'utf-8':
        try:
            sys.stderr.reconfigure(encoding='utf-8')
        except Exception:
            pass

# 添加 src 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'document-parser', 'src'))

from parser import documentParser, parseDocument


def testDocumentParserInit():
    """测试解析器初始化"""
    parser = documentParser()
    assert parser.verbose == False
    assert '.docx' in parser.supportedFormats
    assert '.doc' in parser.supportedFormats
    assert '.pdf' in parser.supportedFormats
    print("[PASS] testDocumentParserInit passed")


def testDocumentParserVerbose():
    """测试 verbose 模式"""
    parser = documentParser(verbose=True)
    assert parser.verbose == True
    print("[PASS] testDocumentParserVerbose passed")


def testParseNonExistentFile():
    """测试解析不存在的文件"""
    parser = documentParser()

    try:
        parser.parse("/non/existent/file.docx")
        assert False, "应抛出异常"
    except FileNotFoundError as e:
        print("testParseNonExistentFile:", e)
        assert "不存在" in str(e)
    print("[PASS] testParseNonExistentFile passed")


def testParseUnsupportedFormat():
    """测试不支持的格式"""
    import tempfile

    parser = documentParser()

    # 创建临时文件
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
        tempPath = f.name

    try:
        parser.parse(tempPath)
        assert False, "应抛出异常"
    except ValueError as e:
        print("testParseUnsupportedFormat:", e)
        assert "不支持" in str(e)
    finally:
        os.unlink(tempPath)

    print("[PASS] testParseUnsupportedFormat passed")


def testParseDocxFile():
    """测试解析 docx 文件"""
    import glob

    # 查找项目中的 docx 文件
    docxFiles = glob.glob("**/*.docx", recursive=True)

    if docxFiles:
        parser = documentParser()
        result = parser.parse(docxFiles[0])
        print("testParseDocxFile:", result["format"], result.get("paragraphCount", 0))
        assert result["success"] == True, "解析应成功"
        assert result["format"] == "docx", "格式应为 docx"
        print("[PASS] testParseDocxFile passed")
    else:
        print("⊘ testParseDocxFile skipped (no docx files found)")


def testParseToJson():
    """测试解析并输出 JSON"""
    import glob
    import tempfile

    docxFiles = glob.glob("**/*.docx", recursive=True)

    if docxFiles:
        parser = documentParser()

        # 创建临时 JSON 文件
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            tempPath = f.name

        try:
            jsonStr = parser.parseToJson(docxFiles[0], tempPath)
            print("testParseToJson: JSON saved to", tempPath)

            # 验证文件已创建
            assert os.path.exists(tempPath), "JSON 文件应已创建"
            assert len(jsonStr) > 0, "JSON 内容不应为空"
            print("[PASS] testParseToJson passed")
        finally:
            if os.path.exists(tempPath):
                os.unlink(tempPath)
    else:
        print("⊘ testParseToJson skipped (no docx files found)")


def testParseDocumentFunction():
    """测试便捷函数"""
    import glob

    docxFiles = glob.glob("**/*.docx", recursive=True)

    if docxFiles:
        result = parseDocument(docxFiles[0])
        print("testParseDocumentFunction:", result["success"])
        assert result["success"] == True
        print("[PASS] testParseDocumentFunction passed")
    else:
        print("⊘ testParseDocumentFunction skipped (no docx files found)")


def testEnhanceTable():
    """测试表格增强功能"""
    parser = documentParser()

    tableData = [
        ["姓名", "年龄", "城市"],
        ["张三", "25", "北京"],
        ["李四", "30", "上海"]
    ]

    result = parser._enhanceTable(tableData, 0)
    print("testEnhanceTable:", result["rowCount"], "rows")
    assert result["rowCount"] == 3, "应有3行数据"
    assert result["headers"] == ["姓名", "年龄", "城市"], "表头应正确"
    assert result["hasNumericData"] == True, "应识别数值数据"
    print("[PASS] testEnhanceTable passed")


def testEnhanceEmptyTable():
    """测试空表格处理"""
    parser = documentParser()

    result = parser._enhanceTable([], 0)
    print("testEnhanceEmptyTable:", result)
    assert result["rowCount"] == 0, "行数应为0"
    print("[PASS] testEnhanceEmptyTable passed")


if __name__ == "__main__":
    print("=" * 50)
    print("开始运行 documentParser 测试")
    print("=" * 50)

    testDocumentParserInit()
    testDocumentParserVerbose()
    testParseNonExistentFile()
    testParseUnsupportedFormat()
    testParseDocxFile()
    testParseToJson()
    testParseDocumentFunction()
    testEnhanceTable()
    testEnhanceEmptyTable()

    print("=" * 50)
    print("所有测试通过!")
    print("=" * 50)
