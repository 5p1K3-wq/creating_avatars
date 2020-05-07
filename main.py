from PIL import Image

image = Image.open('img/example.jpeg')

red, green, blue = image.split()

pixel_shift = 100
width, height = image.size

red_cropped = red.crop((pixel_shift, 0, width, height))
red = red.crop((pixel_shift // 2, 0, width - pixel_shift // 2, height))
red_blend_img = Image.blend(red, red_cropped, 0.5)

blue_cropped = blue.crop((0, 0, width - pixel_shift, height))
blue = blue.crop((pixel_shift // 2, 0, width - pixel_shift // 2, height))
blue_blend_img = Image.blend(blue, blue_cropped, 0.5)

green = green.crop((pixel_shift // 2, 0, width - pixel_shift // 2, height))

new_image = Image.merge('RGB', (red_blend_img, blue_blend_img, green))

new_image.thumbnail((80, 80))
new_image.save('img/new_image.jpg')
