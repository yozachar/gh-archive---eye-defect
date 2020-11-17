'''
# Steps
# 1. Collect images
# 2. Extract data
# 3. Go with second method - 3 folders R, B, & G
# 4. Open all the folders together - Extract the colors and drop them seperately
# 5. Finally resize them
'''

# author: Jovial Joe Jayarson
# email: jovial7joe@hotmail.com
# title: Channelizeing images

import os
import sys
import shutil
from PIL import Image, UnidentifiedImageError

w_size = 224  # required width


def resize(img):
    '''Resize filtered images'''
    # img.size[0] ==> width
    # img.size[1] ==> height
    # calculate width:height  - to maintain the aspect ratio
    ratio = w_size / float(img.size[1])
    h_size = int(img.size[0] * ratio)  # calculate new:height
    # Image.LANCZOS filter smoothens the scaled images - but it is slower
    img = img.resize((h_size, w_size), Image.LANCZOS)
    return img


def process_img(item, f_path):
    '''Filter images to RGB channels'''
    red, green, blue = [], [], []

    f_name = os.path.basename(item)

    try:
        with Image.open(item) as img:
            data = img.getdata()
            for d in data:
                red.append((d[0], 0, 0, ))
                green.append((0, d[1], 0, ))
                blue.append((0, 0, d[2], ))
    except UnidentifiedImageError as e:
        print(">> Error: File Corrupted!")
        return

    for i, color in enumerate([red, green, blue]):
        new_file = f_path[i] + '/' + f_name
        print("Writing...", os.path.basename(new_file))
        img.putdata(color)
        new_img = resize(img)
        new_img.save(new_file)


def channelize(imp, inp, omp, onp):
    '''Prepare images for filering'''
    # RGB for mild-dr
    red_m = omp + '/red'
    os.makedirs(red_m)
    green_m = omp + '/green'
    os.makedirs(green_m)
    blue_m = omp + '/blue'
    os.makedirs(blue_m)

    # RGB for no-dr
    red_n = onp + '/red'
    os.makedirs(red_n)
    green_n = onp + '/green'
    os.makedirs(green_n)
    blue_n = onp + '/blue'
    os.makedirs(blue_n)

    m_cnt = 1
    for item_m in os.scandir(imp):
        print(str(m_cnt) + '.', end=' ')
        if item_m.path.endswith('.tif') and item_m.is_file():
            process_img(item_m.path, [red_m, green_m, blue_m])
        m_cnt += 1

    print("\n>> Pass MILD")

    n_cnt = 1
    for item_n in os.scandir(inp):
        print(str(n_cnt) + '.', end=' ')
        if item_n.path.endswith('.tif') and item_n.is_file():
            process_img(item_n.path, [red_n, green_n, blue_n])
        n_cnt += 1

    print("\n>> Pass NULL")


def setup_path():
    '''Setup directory and paths'''
    # input path
    in_dir = project_path + '/datasets/input'
    in_mild_path = in_dir + '/mild-dr'
    in_null_path = in_dir + '/no-dr'

    # output path
    out_dir = project_path + '/datasets/output'
    # check if output diretory already exists then delete it.
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)

    # create output directories
    os.makedirs(out_dir)
    out_mild_path = out_dir + '/mild-dr'
    os.makedirs(out_mild_path)
    out_null_path = out_dir + '/no-dr'
    os.makedirs(out_null_path)

    return in_mild_path, in_null_path, out_mild_path, out_null_path


if __name__ == "__main__":
    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    project_path = sys.path[-1]

    a, b, c, d = setup_path()
    print(">> Pass Setup")
    channelize(a, b, c, d)
    print("\n>> All Pass!")
