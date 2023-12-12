from PIL import Image
import urllib.request as request

def generate(url_avatar, answers, telegram_id):

    resource = request.urlopen(url_avatar)
    avatar = Image.open(resource)
    mask = Image.open('images/background.JPG')

    if answers[0] == 1:
        img_1 = Image.open('images/img_1_1.PNG')
    else:
        img_1 = Image.open('images/img_1_2.PNG')
    mask_1 = Image.open("images/img_1_mask.PNG").point(lambda x: 255 if x > 50 else 0).convert("1")

    if answers[1] == 1:
        img_2 = Image.open('images/img_2_1.PNG')
    else:
        img_2 = Image.open('images/img_2_2.PNG')
    mask_2 = Image.open("images/img_2_mask.PNG").point(lambda x: 255 if x > 50 else 0).convert("1")

    if answers[2] == 1:
        img_3 = Image.open('images/img_3_1.PNG')
    else:
        img_3 = Image.open('images/img_3_2.PNG')
    mask_3 = Image.open("images/img_3_mask.PNG").point(lambda x: 255 if x > 50 else 0).convert("1")

    if answers[3] == 1:
        img_4 = Image.open('images/img_4_1.PNG')
    else:
        img_4 = Image.open('images/img_4_2.PNG')
    mask_4 = Image.open('images/img_4_mask.PNG').point(lambda x: 255 if x > 50 else 0).convert("1")

    if answers[4] == 1:
        img_5 = Image.open('images/img_5_1.PNG')
    else:
        img_5 = Image.open('images/img_5_2.PNG')
    mask_5 = Image.open('images/img_5_mask.PNG').point(lambda x: 255 if x > 50 else 0).convert("1")

    # Аватарка
    X_SCALE_AVATAR = 560/avatar.width
    Y_SCALE_AVATAR = 560/avatar.height

    X_MASK_AVATAR = 1732
    Y_MASK_AVATAR = 923

    WIDTH_AVATAR = int(avatar.width * X_SCALE_AVATAR)
    HEIGHT_AVATAR = int(avatar.height * Y_SCALE_AVATAR)

    mask.paste(avatar.resize((WIDTH_AVATAR, HEIGHT_AVATAR)), (X_MASK_AVATAR, Y_MASK_AVATAR))

    mask.paste(img_1, (0,0), mask_1)
    mask.paste(img_2, (0,0), mask_2)
    mask.paste(img_3, (0,0), mask_3)
    mask.paste(img_4, (0,0), mask_4)
    mask.paste(img_5, (0,0), mask_5)
    mask.save(f"generated_images/{telegram_id}.jpg")
