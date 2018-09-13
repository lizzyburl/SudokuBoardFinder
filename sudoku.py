from PIL import Image, ImageDraw

im = Image.open("screenshot.png")
draw = ImageDraw.Draw(im)
# (30,280) - (1050, 280)
draw.line((30, 280, 1050, 280), fill="Red", width=5)

# (30, 1295) - (1050, 1295)
draw.line((30, 1295, 1050, 1295), fill="Red", width=5)

# (30, 280) - (30, 1295)
draw.line((30, 280, 30, 1295), fill="Red", width=5)

# (1050, 280) - (1050, 1295)
draw.line((1050, 280, 1050, 1295), fill="Red", width=5)


im.show()
