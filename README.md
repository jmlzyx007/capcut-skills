# capcut-skills — 剪映自动化剪辑

使用 Python + Claude 自动生成剪映（JianYing / CapCut 中文版）草稿，实现自动化视频剪辑流水线。

## 原理

剪映的每个项目是一个本地草稿文件夹，核心是 `draft_content.json`（描述时间线、轨道、素材、字幕、特效）。本项目通过 [pyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) 直接生成该文件，剪映打开即可看到剪好的项目。

```
素材 → Claude 决策剪辑方案 → Python 生成草稿 → 剪映打开微调 → 导出
```

## 环境

- macOS（剪映专业版已安装）
- Python 3.9+
- 剪映草稿目录：`~/Movies/JianyingPro/User Data/Projects/com.lveditor.draft/`

## 安装

```bash
python3 -m venv venv
./venv/bin/pip install pyjianyingdraft
```

## 快速开始

1. 把一个测试视频放到 `materials/test.mp4`
2. 运行示例脚本：

```bash
./venv/bin/python scripts/demo_draft.py
```

3. 打开剪映，应能看到名为 `demo_draft` 的新草稿（含 5 秒视频 + 黄色字幕）

## 项目结构

```
├── scripts/        # Python 脚本（草稿生成逻辑）
│   └── demo_draft.py
├── materials/      # 本地素材（不入库）
├── venv/           # Python 虚拟环境（不入库）
└── README.md
```

## 已知限制

- pyJianYingDraft 在 macOS 上支持**草稿生成**和**模板模式**；**自动导出**仅支持 Windows + 剪映 6 以下版本，Mac 上最后导出需在剪映中手动操作
- 草稿生成功能需要剪映 5 及以上版本

## 后续计划

- [ ] 封装常用剪辑操作（切片、转场、配乐、批量字幕）
- [ ] 接入 Claude（Skill 或 MCP）自动决策剪辑方案
- [ ] 模板化批量混剪流水线
