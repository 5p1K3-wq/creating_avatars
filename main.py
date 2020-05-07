from PIL import Image

image = Image.open('img/example.jpeg')

# Divide the picture into channels and save
red, green, blue = image.split()

pixel_shift = 100
width, height = image.size

# We shift the left channel to the red
red_cropped = red.crop((pixel_shift, 0, width, height))
red = red.crop((pixel_shift // 2, 0, width - pixel_shift // 2, height))
red_blend_img = Image.blend(red, red_cropped, 0.5)

# We shift the right channel to the blue
blue_cropped = blue.crop((0, 0, width - pixel_shift, height))
blue = blue.crop((pixel_shift // 2, 0, width - pixel_shift // 2, height))
blue_blend_img = Image.blend(blue, blue_cropped, 0.5)

# Green channel photo mode
green = green.crop((pixel_shift // 2, 0, width - pixel_shift // 2, height))

# Let's collect a picture from the offset channels and the cropped green channell
new_image = Image.merge('RGB', (red_blend_img, blue_blend_img, green))

# Let's make a thumbnail of 80 by 80
new_image.thumbnail((80, 80))
new_image.save('img/new_image.jpg')
