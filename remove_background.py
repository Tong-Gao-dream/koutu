import os
# 输入文件路径
path = 'D:/python/new_3D_rec/my_code/NeRF-tf/nerf-master/data/nerf_llff_data/vasedeck_new_seg/images_8/'
# 输出文件夹路径
path_out = 'D:/python/new_3D_rec/my_code/NeRF-tf/nerf-master/data/nerf_llff_data/vasedeck_new_seg/image8_new/'
files = os.listdir(path)

for file in files:

    img_name_input = path + file

    img_name_output = path_out + file
    print(img_name_output)

    print('backgroundremover -i "' + str(img_name_input) + '" -o "' + str(img_name_output)+'"')
    os.system('backgroundremover -i "' + str(img_name_input) + '" -o "' + str(img_name_output)+'"')

1