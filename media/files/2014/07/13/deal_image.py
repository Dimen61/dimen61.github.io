import Image

im = Image.open("daffodil.jpg")

# Resize the image
resize_n = 1.75
width, height = im.size
width /= resize_n
height /= resize_n
width, height = int(width), int(height)

new_im = im.resize((width, height), Image.BILINEAR)

# Create the resized image
new_im.save('resized.jpg')

print 'Processed..'
