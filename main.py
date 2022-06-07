import cv2

def deColorInator(orgImg):
    for row in range(len(orgImg)):
        for pixel in range(len(orgImg[row])):
            curpixel = (orgImg[row][pixel])
            pixAvg = sum(curpixel)/3
            # print(pixAvg)
            if pixAvg >= 130:
                curpixel[0] = 0
                curpixel[1] = 0
                curpixel[2] = 0
            else:
                curpixel[0] = 255
                curpixel[1] = 255
                curpixel[2] = 255

def makeArt(finalImg):
    for row in range(len(finalImg)):
        for pixel in range(len(finalImg[row])):
            curpixel = (finalImg[row][pixel])
            pixAvg = sum(curpixel)/3
            if pixAvg >= 130:
                print("5", end="")
            else:
                print(" ", end="")
        print("")




# img = cv2.imread("img.jpeg")
img = cv2.imread("hotdog.png")

img = cv2.resize(img, (80,40))

deColorInator(img)

makeArt(img)

cv2.imshow('Original Image', img)

cv2.waitKey(0)
