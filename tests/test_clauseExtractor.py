"""条款提取器测试"""

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
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'clause-extractor', 'src'))

from extractor import clauseExtractor, extractClauses


def testExtractParties():
    """测试提取合同当事人信息"""
    extractor = clauseExtractor()

    content = """
    甲方：北京科技有限公司
    乙方：上海贸易有限公司
    丙方：广州网络有限公司
    """

    result = extractor.extractParties(content)
    print("testExtractParties:", result)
    assert len(result["partyKeywords"]) > 0, "应提取到当事人关键词"
    assert len(result["partyNames"]) > 0, "应提取到当事人名称"
    print("[PASS] testExtractParties passed")


def testExtractDates():
    """测试提取日期信息"""
    extractor = clauseExtractor()

    content = """
    签订日期：2024年1月15日
    合同期限：自2024年1月1日起至2025年12月31日止
    """

    result = extractor.extractDates(content)
    print("testExtractDates:", result)
    assert len(result) > 0, "应提取到日期"
    print("[PASS] testExtractDates passed")


def testExtractAmounts():
    """测试提取金额信息"""
    extractor = clauseExtractor()

    content = """
    合同总金额：人民币100万元
    单价：每月5000元
    """

    result = extractor.extractAmounts(content)
    print("testExtractAmounts:", result)
    assert len(result) > 0, "应提取到金额"
    print("[PASS] testExtractAmounts passed")


def testExtractContacts():
    """测试提取联系方式"""
    extractor = clauseExtractor()

    content = """
    联系人：张先生
    电话：010-12345678
    邮箱：zhang@example.com
    地址：北京市朝阳区某某路123号
    """

    result = extractor.extractContacts(content)
    print("testExtractContacts:", result)
    assert len(result["phones"]) > 0, "应提取到电话"
    assert len(result["emails"]) > 0, "应提取到邮箱"
    assert len(result["addresses"]) > 0, "应提取到地址"
    print("[PASS] testExtractContacts passed")


def testExtractAll():
    """测试提取所有信息"""
    extractor = clauseExtractor()

    content = """
    合同编号：2024001
    甲方：北京科技有限公司
    乙方：上海贸易有限公司
    签订日期：2024年1月15日
    合同金额：人民币100万元
    联系人：张先生，电话：010-12345678，邮箱：zhang@example.com
    合同期限：自2024年1月15日起至2025年1月14日止
    """

    result = extractor.extractAll(content)
    print("testExtractAll:", result)
    assert result["success"] == True, "应返回成功"
    assert "parties" in result, "应包含当事人信息"
    assert "dates" in result, "应包含日期信息"
    assert "amounts" in result, "应包含金额信息"
    print("[PASS] testExtractAll passed")


def testExtractByInstruction():
    """测试根据指令提取信息"""
    extractor = clauseExtractor()

    content = """
    甲方：北京科技有限公司
    乙方：上海贸易有限公司
    合同金额：人民币100万元
    签订日期：2024年1月15日
    """

    # 测试提取金额
    result = extractor.extractByInstruction(content, "提取金额")
    print("testExtractByInstruction (amount):", result)
    assert "result" in result, "应返回结果"

    # 测试提取当事人
    result = extractor.extractByInstruction(content, "提取当事人")
    print("testExtractByInstruction (party):", result)
    assert "result" in result, "应返回结果"

    print("[PASS] testExtractByInstruction passed")


def testExtractClausesFunction():
    """测试便捷函数"""
    content = "甲方：北京科技有限公司，合同金额：人民币50万元"

    result = extractClauses(content)
    print("testExtractClausesFunction:", result)
    assert result["success"] == True, "应返回成功"
    print("[PASS] testExtractClausesFunction passed")


def testEmptyContent():
    """测试空内容"""
    extractor = clauseExtractor()

    result = extractor.extract("")
    print("testEmptyContent:", result)
    assert result["success"] == False, "空内容应返回失败"
    assert "error" in result, "应包含错误信息"
    print("[PASS] testEmptyContent passed")


if __name__ == "__main__":
    print("=" * 50)
    print("开始运行 clauseExtractor 测试")
    print("=" * 50)

    testExtractParties()
    testExtractDates()
    testExtractAmounts()
    testExtractContacts()
    testExtractAll()
    testExtractByInstruction()
    testExtractClausesFunction()
    testEmptyContent()

    print("=" * 50)
    print("所有测试通过!")
    print("=" * 50)
