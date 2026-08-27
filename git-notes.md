# Git 学习笔记

记录我学习 Git / GitHub 过程中，真实练习过的操作。

## 基础流程

- `git init` —— 初始化本地仓库
- `git add .` —— 把改动加入暂存区
- `git commit -m "说明"` —— 提交一个版本快照
- `git push` —— 推送到远程仓库

## 分支 Branch

- `git switch -c <分支名>` —— 新建并切换到分支
- `git switch main` —— 切回主分支
- `git merge --no-ff <分支名>` —— 合并分支并保留合并记录

## 远程 Remote

- `git remote -v` —— 查看远程地址
- `git push -u origin main` —— 推送并建立跟踪关系

## Pull Request

- 在功能分支上完成修改 → `git push` 推到 GitHub
- 在 GitHub 网页发起 Pull Request，请求把分支合并进 `main`
- 审查通过后合并，功能分支的使命完成

> 本文件由 `feature-git-notes` 分支添加，用来练习 Pull Request 的完整流程。
