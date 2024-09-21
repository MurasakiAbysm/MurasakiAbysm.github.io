import os


def get_image_filenames(directory):
    """获取指定目录下所有图像文件的文件名"""
    image_filenames = []
    # 列出目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件扩展名
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')):
            image_filenames.append(filename)
    return image_filenames


# 获取当前目录下所有图片的文件名
image_filenames = get_image_filenames(os.getcwd())

# 打印所有找到的图片文件名
for filename in image_filenames:
    print(f"/irons/{filename}")
