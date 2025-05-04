import os
import shutil
import sys

"""
By Star Dream Studio
"""

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

FILES = [
    "intro.webm",
    "intro720p.webm",
    "intro-perfectworld.webm",
    "intro-perfectworld720p.webm"
]

def main():
    print("请输入你的 CS2 安装路径，例如：D:\\SteamLibrary\\steamapps\\common\\Counter-Strike Global Offensive")
    target_root = input("路径：").strip('"').strip()
    target_dir = os.path.join(target_root, "game", "csgo", "panorama", "videos")

    if not os.path.isdir(target_dir):
        print(f"❌ 没有找到有效的视频目录：{target_dir}")
        input("请检查路径后重试。按回车退出...")
        return

    for file in FILES:
        src = get_resource_path(f"videos/{file}")
        dst = os.path.join(target_dir, file)
        try:
            shutil.copy2(src, dst)
            print(f"✅ 替换成功：{file}")
        except Exception as e:
            print(f"❌ 替换失败：{file} 原因：{e}")

    print("\n 所有文件处理完毕！")
    input("按回车关闭窗口...")

if __name__ == "__main__":
    main()
