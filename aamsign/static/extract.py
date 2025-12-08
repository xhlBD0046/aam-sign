import os

# ===== 需要批量改名的目录 =====
# 可以写成绝对路径，也可以只写最后一级，用 BASE_DIR 拼接
BASE_DIR = r"E:\AAC\aam-sign\aamsign\static\images\general\index"

FOLDERS = [
    os.path.join(BASE_DIR, "col1"),
    os.path.join(BASE_DIR, "col2"),
    os.path.join(BASE_DIR, "col3"),
]

IMAGE_EXTS = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp",
    ".bmp", ".tif", ".tiff", ".svg", ".heic", ".jfif"
}


def rename_images_sequential(folder: str):
    """把 folder 里的图片按 1,2,3... 重新命名（保留后缀），避免命名冲突。"""
    if not os.path.isdir(folder):
        print(f"[跳过] {folder} 不是目录或不存在")
        return

    print(f"\n=== 处理目录: {folder} ===")

    # 先取出目录中所有图片文件
    files = [
        f for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
        and os.path.splitext(f)[1].lower() in IMAGE_EXTS
    ]

    # 排个序，这样每次顺序稳定
    files.sort()

    if not files:
        print("  （没有找到图片文件）")
        return

    # 第一步：先改成临时名字，避免与目标名字冲突
    tmp_names = []
    for idx, filename in enumerate(files, start=1):
        old_path = os.path.join(folder, filename)
        name, ext = os.path.splitext(filename)
        tmp_name = f"__tmp_{idx}{ext}"
        tmp_path = os.path.join(folder, tmp_name)

        os.rename(old_path, tmp_path)
        tmp_names.append((tmp_name, ext))

    # 第二步：再从临时名字改成最终的 1,2,3...
    for idx, (tmp_name, ext) in enumerate(tmp_names, start=1):
        tmp_path = os.path.join(folder, tmp_name)
        new_name = f"{idx}{ext}"
        new_path = os.path.join(folder, new_name)

        # 如果已经有同名文件（比如你第二次运行脚本），先删或改名，这里选择直接覆盖前先提示
        if os.path.exists(new_path):
            print(f"  [注意] {new_path} 已存在，自动覆盖")
            os.remove(new_path)

        os.rename(tmp_path, new_path)
        print(f"  {tmp_name}  ->  {new_name}")


def main():
    for folder in FOLDERS:
        rename_images_sequential(folder)


if __name__ == "__main__":
    # 建议先备份一份，再运行
    main()
