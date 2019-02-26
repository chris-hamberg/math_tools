# Quickly test for image equality based on RGB values. Expects PNG
from PIL import Image

def resize_images(img_1, img_2):
    '''Check image sizes, and normalize images'''
    num_pix_1 = img_1.width * img_1.height
    num_pix_2 = img_2.width * img_2.height
    if num_pix_1 > num_pix_2:
        img_1 = img_1.resize((img_2.width, img_2.height))
    elif num_pix_1 < num_pix_2:
        img_2 = img_2.resize((img_1.width, img_1.height))
    else:
        pass
    return img_1, img_2

def image_value(pic):
    ''' Get image color information'''
    color_data = 0
    for x in range(pic.width):
        for y in range(pic.height):
            tup = pic.getpixel((x, y))
            val = sum(tup)
            if val < 950: # 1020 == #FFFFFF; adjusted for some lossy
                color_data += val
    return color_data

def main():
    '''Accepts command line args or will ask for args at terminal
    if none are given. Args are fill paths to png files. Two args
    are required.'''
    import sys
    if not sys.argv[1:]:
        img_1 = input('Enter full path to image 1: ')
        img_2 = input('Enter full path to image 2: ')
    else:
        img_1, img_2 = sys.argv[1:]
        img_1, img_2 = Image.open(img_1), Image.open(img_2)
    img_1, img_2 = resize_images(img_1, img_2)
    # compare images based on color information (100000 might be a bit high)
    if abs(image_value(img_1) - image_value(img_2)) > 100000:
        print('The image information in the pictures is not identical')

if __name__ == '__main__': main()
