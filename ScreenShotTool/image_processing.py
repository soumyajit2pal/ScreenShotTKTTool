from PIL import Image, ImageTk

def image_resize(working_dir, image_name):
    image = Image.open(working_dir+"\\image\\" + image_name)
    image = image.resize((1920, 1020), Image.ANTIALIAS)
    image.save(working_dir+"\\image\\" + image_name, quality=20, optimize=True)