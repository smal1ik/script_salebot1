from PIL import Image
import urllib.request as request
from uuid import uuid4
import os

def generate(url_avatar):

    dir = os.path.abspath(os.curdir)
    uuid = str(uuid4())
    resource = request.urlopen(url_avatar)

    avatar = Image.open(resource)
    mask = Image.open(f'{dir}/images/mask.jpg')
    img_1 = Image.open(f'{dir}/images/img_1.jpg')
    mask_1 = Image.open(f"{dir}/images/mask_1.jpg").point(lambda x: 255 if x > 50 else 0).convert("1")
    img_2 = Image.open(f'{dir}/images/img_2.jpg')
    mask_2 = Image.open(f"{dir}/images/mask_2.jpg").point(lambda x: 255 if x > 50 else 0).convert("1")
    img_3 = Image.open(f'{dir}/images/img_3.jpg')
    mask_3 = Image.open(f"{dir}/images/mask_3.jpg").point(lambda x: 255 if x > 50 else 0).convert("1")
    img_4 = Image.open(f'{dir}/images/4.1.jpg')
    img_5 = Image.open(f'{dir}/images/5.1.jpg')

    # Аватарка
    X_SCALE_AVATAR = 81/avatar.width
    Y_SCALE_AVATAR = 84/avatar.height

    X_MASK_AVATAR = 243
    Y_MASK_AVATAR = 132

    WIDTH_AVATAR = int(avatar.width * X_SCALE_AVATAR)
    HEIGHT_AVATAR = int(avatar.height * Y_SCALE_AVATAR)

    # 1-е изображение
    X_SCALE_1 = 70/img_1.width
    Y_SCALE_1 = 73/img_1.height

    X_MASK_1 = 105
    Y_MASK_1 = 60

    WIDTH_1 = int(img_1.width * X_SCALE_1)
    HEIGHT_1 = int(img_1.height * Y_SCALE_1)

    # 2-е изображение
    X_SCALE_2 = 0/img_2.width
    Y_SCALE_2 = 0/img_2.height

    X_MASK_2 = 92
    Y_MASK_2 = 206

    WIDTH_2 = int(img_2.width * X_SCALE_2)
    HEIGHT_2 = int(img_2.height * Y_SCALE_2)

    # 3-е изображение
    X_SCALE_3 = 0/img_3.width
    Y_SCALE_3 = 0/img_3.height

    X_MASK_3 = 215
    Y_MASK_3 = 291

    WIDTH_3 = int(img_3.width * X_SCALE_3)
    HEIGHT_3 = int(img_3.height * Y_SCALE_3)

    # 4-е изображение
    X_SCALE_4 = 0/img_4.width
    Y_SCALE_4 = 0/img_4.height

    X_MASK_4 = 386
    Y_MASK_4 = 185

    WIDTH_4 = int(img_4.width * X_SCALE_4)
    HEIGHT_4 = int(img_4.height * Y_SCALE_4)

    # 5-е изображение
    X_SCALE_5 = 0/img_5.width
    Y_SCALE_5 = 0/img_5.height

    X_MASK_5 = 388
    Y_MASK_5 = 71

    WIDTH_5 = int(img_5.width * X_SCALE_5)
    HEIGHT_5 = int(img_5.height * Y_SCALE_5)

    mask.paste(avatar.resize((WIDTH_AVATAR, HEIGHT_AVATAR)), (X_MASK_AVATAR, Y_MASK_AVATAR))

    mask.paste(img_1, (X_MASK_1, Y_MASK_1), mask_1)
    mask.paste(img_2, (X_MASK_2, Y_MASK_2), mask_2)
    mask.paste(img_3, (X_MASK_3, Y_MASK_3), mask_3)
    mask.save(f"{dir}/generated_images/{uuid}.jpg")
    return uuid