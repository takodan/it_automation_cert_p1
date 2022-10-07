from PIL import Image
import os
import sys

def get_files_in_dir(dir_path):
    items_list = os.listdir(dir_path)
    item =""
    image_list = []
    for item in items_list:
        if os.path.isfile(os.path.join(dir_path, item)):
            image_list.append(item)
    
    print(image_list)
    return image_list



def rotate_an_image_270(im_class):
    out_image = im_class.rotate(270)
    return out_image

def resize_an_image_128x128(im_class):
    out_image = im_class.resize((128, 128))
    return out_image


def main():
    try_times = 0
    while try_times < 5 :
        source_path = input("please enter the source path: ")
        dest_path = input("please enter the destination path: ")
    # valid dir_path
        if os.path.isdir(source_path):
            print("directory valid")
            break
        else:
            print("directory invalid")
        try_times += 1
    
    images_list = get_files_in_dir(source_path)

    print("applying transform (roate270, resize128x128, JEPG) and save to the destination")
    #rotate, resize, and save as JEPG image
    for image in images_list:
        with Image.open(os.path.join(source_path, image)) as im_class:
            im_class_rotated = rotate_an_image_270(im_class)
            im_class_fin = resize_an_image_128x128(im_class_rotated)
            im_class_fin.save( os.path.join(dest_path, image))

    print("action complete")


if __name__ == "__main__":
    main()
