from PIL import Image, ImageFilter


# img = Image.open('./Pokedex/pikachu.jpg')

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.convert('L')

# crooked = filtered_img.rotate(90)

# resize = filtered_img.resize((200, 200))
# resize.save("grey.png", 'png')


# img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.convert('L')
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("grey.png", 'png')


img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save("thumbnail.jpg")
print(img.size)
