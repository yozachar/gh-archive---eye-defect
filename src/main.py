# Todo
# 1. Collect images
# 2. Extract data
# 3. Go with second method - 3 folders R, B, & G
# Open all the folders together - Extract the colors and drop them seperately
# Finally resize them

from PIL import Image

img = Image.open('test_in.tif')
data = img.getdata()

r = [(d[0], 0, 0) for d in data]
g = [(0, d[1], 0) for d in data]
b = [(0, 0, d[2]) for d in data]

img.putdata(r)
img.save('r.tif')
img.putdata(g)
img.save('g.tif')
img.putdata(b)
img.save('b.tif')