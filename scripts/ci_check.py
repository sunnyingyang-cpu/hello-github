#!/usr/bin/env python3
"""仓库自检脚本：在每次 push / PR 时由 GitHub Actions 自动运行。

做的事：
1. 打印 Python 版本
2. 列出仓库里所有 Markdown 文件
3. 基本检查 README.md 是否存在且含一级标题
"""

import os
import sys

print("=== 仓库自检开始 ===")
print(f"Python 版本: {sys.version.split()[0]}")

# 递归列出所有 Markdown 文件（跳过 .git）
md_files = []
for root, dirs, files in os.walk("."):
    if ".git" in root:
        continue
    for f in files:
        if f.endswith(".md"):
            md_files.append(os.path.join(root, f).replace("./", "", 1))

print(f"找到 {len(md_files)} 个 Markdown 文件：")
for f in sorted(md_files):
    print(f"  - {f}")

# 基本检查：README 必须存在且含一级标题
readme = "README.md"
if not os.path.exists(readme):
    raise SystemExit("❌ 缺少 README.md")
with open(readme, encoding="utf-8") as fh:
    if not fh.read().lstrip().startswith("#"):
        raise SystemExit("❌ README.md 没有一级标题")

print("✅ README 检查通过")
print("=== 仓库自检完成 ===")
