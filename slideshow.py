# # Mustafa Kaptan
# # Slideshow program

import sys, ConfigParser, time
from SimpleCV import Image
from SimpleCV import ImageSet
from SimpleCV import Display

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

    # Display
    display = Display()

    # Set of slide images
    slideSet = ImageSet("./experiments/" + filename)

    lineList = config.items('sequence')
    length = len(lineList)
    sleepList = list()

    # Sleep times
    for line in lineList:
        sleepList.append(int(line[1])/1000)

    # Main loop    
    while display.isNotDone():
        for index, img in enumerate(slideSet):
            img.show()
            time.sleep(sleepList[index])

    sys.exit()

if __name__ == "__main__":
    main()
    
