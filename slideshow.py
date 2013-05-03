# # Mustafa Kaptan
# # Slideshow program
import sys, ConfigParser, time
from SimpleCV import *
import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (100, 100, 100)

def start_countdown(screen):
    # Get screens width,height -> center
    centerX = screen.get_width() / 2
    centerY = screen.get_height() / 2

    # Font
    countfont = pygame.font.Font('turkish.ttf', 150)

    # Start screen
    startScreen = Image()
    for i in range (4, 0, -1):

        if i > 1:
            # Draw an anti-aliased circle
            #gfxdraw.aacircle(screen, centerX, centerY, 150, WHITE)
            newlayer.circle((centerX,centerY), 150, filled=False, color = Color.WHITE)
            counttext = countfont.render("" + str(i - 1), True, WHITE)
            screen.blit(counttext, (centerX - 40, centerY - 90))
        pygame.display.flip()
        pygame.time.delay(1000)

def main():
    # Get file name
    if len(sys.argv) < 2:
        print "<%s> usage : <%s> <directory name>" %(sys.argv[0], sys.argv[0])
        sys.exit()
    else:
        filename = sys.argv[1]

    config = ConfigParser.RawConfigParser()
    try:
        config.readfp(open("./experiments/" + filename + "/config.ini"))
    except IOError: 
        print "Error: can\'t find file or read data"
        sys.exit()

    pygame.init()
    # Drawing layer
    #newlayer = DrawingLayer((width,height))

    # Screen
    display = Display(flags=pygame.FULLSCREEN)
    screen.set_caption("Slideshow")

    # Invisible mouse
    pygame.mouse.set_visible(False)

    # Set of slide images
    slideSet = ImageSet("./experiments/" + filename)

    lineList = config.items('sequence')
    length = len(lineList)
    sleepList = list()

    # Save lines to Image class and Slideshow list
    for line in lineList:
        sleepList.append(int(line[1])/1000)

    # Start the countdown
    start_countdown()

    # Main loop    
    while display.isNotDone():
        for index, img in enumerate(slideSet):
            img.show()
            time.sleep(sleepList[index])

    sys.exit()

if __name__ == "__main__":
    main()
