import cv2
import HandTrackingModule as htm
import numpy as np
from EuclideanDistance import euclidean_distance_2d
import Board


def main():

    board = Board.Board()

    cap = cv2.VideoCapture(0)
    handDetector = htm.HandDetector()
    prevPos = (-1, -1)
    currentPos = (-1,-1)
    erase = False
    Draw = True

    while True:

        success, img = cap.read()
        img1 = handDetector.findHands(img)
        lmDict = handDetector.findPosition(img1, ids=[8,12])


        # print(lmDict)
        if len(lmDict) != 0:

            lm8 = lmDict[8]
            lm12 = lmDict[12]

            if prevPos == (-1, -1):
                prevPos = (lm8[0], lm8[1])

            print(lmDict)
            currentPos = (lm8[0], lm8[1])

            if euclidean_distance_2d(lm8,lm12) > 40 :

                if(erase == False):
                    board.draw(prevPos, currentPos)

                else:
                    board.erase(currentPos)
                prevPos = currentPos

            else:
                prevPos = (lm8[0], lm8[1])


        board.display(currentPos)
        key = cv2.waitKey(1)

        if key == ord("r"):
            board.reset_board()

        elif key == ord("d"):
            draw = True
            erase = False

        # cv2.imshow("frame",img1)
        elif key == ord("e"):

            draw = False
            erase = True

        elif key == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()