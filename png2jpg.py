from PIL import Image
import os
import cv2

from PIL import Image

# 输入文件路径
path = 'D:/python/new_3D_rec/my_code/NeRF-tf/nerf-master/data/nerf_llff_data/vasedeck_new_seg/images_8/'
# 输出文件夹路径
path_out = 'D:/python/new_3D_rec/my_code/NeRF-tf/nerf-master/data/nerf_llff_data/vasedeck_new_seg/image8_new/'
files = os.listdir(path)


def transparence2white(img):
    sp = img.shape  # 获取图片维度
    width = sp[0]  # 宽度
    height = sp[1]  # 高度
    for yh in range(height):
        for xw in range(width):
            color_d = img[xw, yh]  # 遍历图像每一个点，获取到每个点4通道的颜色数据
            print('color_d', color_d)
            if (color_d[2] == 0):  # 最后一个通道为透明度，如果其值为0，即图像是透明
                img[xw, yh] = [255, 255, 255]  # 则将当前点的颜色设置为白色，且图像设置为不透明
    return img


for file in files:

    img_name_input = path + file
    print(img_name_input)
    img1 = cv2.imread(img_name_input)
    # b, g, r = cv2.split(img1)
    # img_rgb = cv2.merge([r, g, b])
    # print('img1', img1.shape)
    # cv2.imshow('1', img_rgb)
    # cv2.waitKey(0)

    img = cv2.imread(img_name_input)
    img_output = transparence2white(img)

    file_a = file[0:8]
    print(file_a)
    img_name_output = path_out + file_a
    print(img_name_output)

    im = Image.fromarray(img_output)
    im.save(img_name_output + ".jpg")

    # im = Image.open(img_output)
    # im = im.convert('RGB')
    # im.save(img_name_output+".jpg", quality=95)
