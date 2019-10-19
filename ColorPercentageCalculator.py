from PIL import Image                       # Thanks, pillow!

def calculateColor(image, color):
    im = Image.open(image)                  # Opening the png file (don't have to save afterwards as I'm not editing it in any way)
    (width, height) = im.size               # Setting width and height as variables for comfort
    pixArray = im.load()                    # Loading the pixel values into what I believe is a 2D array (or something related to it)
    blackPixCount = 0                       # Colored pixel tally

    for y in range(0,height):               # Iterate over every Y coordinate
        for x in range(0,width):            # Iterate over every X coordinate on a given Y coordinate
            if pixArray[x,y] == color:      # Checking if pixel value == color
                blackPixCount += 1          # If so, the adding one to the colored pixel tally

    return blackPixCount/(width*height)

print(str(calculateColor("FYKOSpdf1200.png", (0,0,0)) * 100) + "%") # Print out the final percentage
