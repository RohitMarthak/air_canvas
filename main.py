import math
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

    while True:
        success, img = cap.read()
        img1 = handDetector.findHands(img)
        lmDict = handDetector.findPosition(img1, ids=[4, 8])

        # print(lmDict)
        if len(lmDict) != 0:

            lm8 = lmDict[8]
            lm4 = lmDict[4]

            board.cursor_img = board.draw_cursor(lm8)

            if prevPos == (-1, -1):
                prevPos = (lm8[0], lm8[1])

            print(lmDict)

            if euclidean_distance_2d(lm4, lm8) < 42:

                currentPos = (lm8[0], lm8[1])
                board.draw(prevPos, currentPos)
                prevPos = currentPos

            else:
                prevPos = (lm8[0], lm8[1])

            board.display()

        key = cv2.waitKey(1)

        if key == ord("r"):
            board.reset_board()

        # cv2.imshow("frame",img1)
        elif key == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
