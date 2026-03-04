"""合同审查命令行工具

用于从命令行执行合同审查
"""

import sys
import json
import subprocess
from pathlib import Path

# 项目根目录 ( ContractGuardAgent1 )
# review.py 在 .claude/skills/contract-reviewer/src/ 下
# 需要向上一级到 .claude/skills/contract-reviewer，再两级到 .claude，再两级到项目根
PROJECT_ROOT = Path(__file__).resolve().parents[4]


def runScript(scriptPath: str, args: list = None) -> dict:
    """运行 Python 脚本并返回 JSON 结果"""
    cmd = [sys.executable, str(scriptPath)]
    if args:
        cmd.extend(args)

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding='utf-8'
    )

    if result.returncode != 0:
        raise Exception(f"脚本执行失败: {result.stderr}")

    # 尝试解析 JSON 输出
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        # 如果不是 JSON，返回原始文本
        return {"raw": result.stdout}


def main():
    """主函数"""
    # 检查参数
    if len(sys.argv) < 2:
        print("用法: python review.py <合同文件路径>")
        sys.exit(1)

    filePath = sys.argv[1]

    # 添加项目根目录到路径
    sys.path.insert(0, str(Path(__file__).parent))
    from reviewer import contractReviewer

    # Step 1: 解析文档
    print("正在解析文档...")
    parserScript = PROJECT_ROOT / ".claude" / "skills" / "document-parser" / "src" / "parser.py"
    parseResult = runScript(parserScript, [filePath])

    if not parseResult.get("success"):
        print(f"解析失败: {parseResult.get('error')}")
        sys.exit(1)

    content = parseResult.get("content", "")
    print(f"文档解析完成，段落数: {parseResult.get('paragraphCount')}, 表格数: {parseResult.get('tableCount')}")

    # Step 2: 合同审查 (包含条款提取)
    print("正在进行合同审查...")
    reviewer = contractReviewer()
    reviewResult = reviewer.review(content)

    # 输出结果
    print("\n" + "=" * 50)
    print("审查结果")
    print("=" * 50)

    summary = reviewResult.get("summary", {})
    print(f"\n问题汇总: 共 {summary.get('totalIssues', 0)} 项")
    print(f"  - 严重: {summary.get('critical', 0)}")
    print(f"  - 警告: {summary.get('warning', 0)}")
    print(f"  - 提示: {summary.get('info', 0)}")

    # 合规性检查
    compliance = reviewResult.get("compliance", {})
    print(f"\n合规性检查: {'通过' if compliance.get('complete') else '有缺失'}")
    if compliance.get("missingClauses"):
        print(f"缺失条款: {', '.join(compliance['missingClauses'])}")

    # 风险列表
    risks = reviewResult.get("risks", [])
    if risks:
        print("\n风险提示:")
        for risk in risks:
            levelTag = "[CRITICAL]" if risk["level"] == "critical" else "[WARNING]"
            print(f"  {levelTag} [{risk['type']}] {risk.get('suggestion', '')}")

    # 提取的关键信息
    extractedInfo = reviewResult.get("extractedInfo", {})
    if extractedInfo.get("parties"):
        print(f"\n合同当事人: {', '.join(extractedInfo['parties'][:5])}")
    if extractedInfo.get("amounts"):
        print(f"金额信息: {', '.join(extractedInfo['amounts'][:3])}")
    if extractedInfo.get("dates"):
        print(f"日期信息: {len(extractedInfo['dates'])} 个")

    print("\n" + "=" * 50)

    # 可选：输出完整 JSON
    if "--json" in sys.argv:
        print("\n完整JSON结果:")
        print(json.dumps(reviewResult, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
