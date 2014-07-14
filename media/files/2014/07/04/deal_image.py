import Image

im = Image.open("3.bmp")

# Resize the image
resize_n = 1.2
width, height = im.size
width /= resize_n
height /= resize_n
width, height = int(width), int(height)

new_im = im.resize((width, height), Image.BILINEAR)

# Create the resized image
new_im.save('debate.jpg')

print 'Processed..'
