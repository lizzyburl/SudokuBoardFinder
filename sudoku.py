from PIL import Image, ImageDraw



# (x1, y1) defines the upper left corner.
# (x2, y2) defines the lower right corner.
# The reason we are using this function instead of draw.rectangle is because we want to specify the width of the line.
def drawSquare(x1, y1, x2, y2):
	line_width=3
	draw.line((x1, y1, x1, y2), fill="Red", width=line_width)
	draw.line((x1, y1, x2, y1), fill="Red", width=line_width)
	draw.line((x2, y1, x2, y2), fill="Red", width=line_width)
	draw.line((x1, y2, x2, y2), fill="Red", width=line_width)

# Returns a matrix of the coordinates for each square.
# Stored like: ((A1_x1, A1_y1, A1_x2, A1_y2), ((A2_x1, A2_y1, A2_x2, A2_y2), ...)
def getGridSquares(x1, y1, x2, y2):
	width = x2 - x1
	height = y2 - y1
	square_width = width / 9
	square_height = height / 9
	square_list = []
	for r in range (0,9):
		for c in range (0,9):
			square_x1 = x1 + square_width * c
			square_y1 = y1 + square_height * r
			square_x2 = x1 + square_width * c + square_width
			square_y2 = y1 + square_height * r + square_height
			drawSquare(square_x1, square_y1, square_x2, square_y2)
			square_list.append([square_x1, square_y1, square_x2, square_y2])
	return square_list


im = Image.open("screenshot.png")
draw = ImageDraw.Draw(im)
# (30,280) - (1048, 1295)
drawSquare(30, 280, 1047, 1293)
gridSquares = getGridSquares(30, 280, 1047, 1293)
print("Grid Squares")
print(gridSquares)


im.show()

