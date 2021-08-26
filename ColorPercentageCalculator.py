from PIL import Image

def calculateColor(image, color):
    im = Image.open(image)
    (width, height) = im.size
    pixArray = im.load()
    blackPixCount = 0

    for y in range(0, height):  # Iterate over every Y coordinate
        for x in range(0, width):  # Iterate over every X coordinate on a given Y coordinate
            if pixArray[x, y] == color:
                blackPixCount += 1

    return blackPixCount/(width*height)

print(str(calculateColor("FYKOSpdf1200.png", (0, 0, 0)) * 100) + "%")  # Print out the final percentage
