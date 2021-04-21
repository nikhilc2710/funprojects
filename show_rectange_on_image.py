from PIL import Image
img = Image.open("av/t7.jpg").convert('RGBA')
rect = Image.new("RGBA", (100,300), (255, 255, 255, 0))
img.paste(rect, (100,100))
img.show()
area = (100, 100, 300, 300)
# # img.show()
cropped_img = img.crop(area)
# cropped_img.show()