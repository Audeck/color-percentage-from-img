from PIL import Image                       #Thanks, pillow!

im = Image.open("FYKOSpdf1200.png")         #Opening the png file (don't have to save afterwards as I'm not editing it in any way)
(width, height) = im.size                   #Setting width and height as variables for comfort (completely arbitrary; though might be worth not calling the library's function over and over - would have to measure the timing (at some point new local variables might be worth setting))
pixArray = im.load()                        #Loading the pixel values into what I believe is a 2D array (or something related to it)
blackPixCount = 0                           #Black pixel tally

for y in range(0,height):                   #Iterate over every Y coordinate
    for x in range(0,width):                #Iterate over every X coordinate on a given Y coordinate
        if pixArray[x,y] == (0,0,0):        #Checking if pixel value == black
            blackPixCount += 1              #If so, the adding one to the black pixel tally

print(blackPixCount/(width*height))         #Print out the final percentage of black pixels/all pixels
