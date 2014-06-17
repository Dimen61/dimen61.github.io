import Image

im = Image.open("library.jpg")

# Resize the image
resize_n = 8
width, height = im.size
width /= resize_n
height /= resize_n

new_im = im.resize((width, height), Image.BILINEAR)

# Create the resized image
new_im.save('resized.jpg')
