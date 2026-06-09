"""最小示例：生成一个剪映草稿，包含一段视频 + 一条字幕。

用法：
    1. 把一个测试视频放到 materials/ 目录，命名为 test.mp4
    2. 运行 ./venv/bin/python scripts/demo_draft.py
    3. 打开剪映，应能看到名为 "demo_draft" 的新草稿
"""
import os

import pyJianYingDraft as draft
from pyJianYingDraft import trange

# 剪映草稿根目录（macOS 默认路径）
DRAFT_ROOT = os.path.expanduser(
    "~/Movies/JianyingPro/User Data/Projects/com.lveditor.draft"
)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEO_PATH = os.path.join(PROJECT_DIR, "materials", "test.mp4")


def main():
    if not os.path.exists(VIDEO_PATH):
        raise SystemExit(f"请先把测试视频放到 {VIDEO_PATH}")

    draft_folder = draft.DraftFolder(DRAFT_ROOT)
    script = draft_folder.create_draft("demo_draft", 1920, 1080, allow_replace=True)

    # 添加视频轨道和素材
    script.add_track(draft.TrackType.video)
    video_material = draft.VideoMaterial(VIDEO_PATH)
    video_segment = draft.VideoSegment(video_material, trange("0s", "5s"))
    script.add_segment(video_segment)

    # 添加文本轨道和字幕
    script.add_track(draft.TrackType.text)
    text_segment = draft.TextSegment(
        "Hello 剪映自动化!",
        trange("0s", "5s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(color=(1.0, 1.0, 0.0)),
    )
    script.add_segment(text_segment)

    script.save()
    print(f"草稿已生成：{DRAFT_ROOT}/demo_draft")


if __name__ == "__main__":
    main()
