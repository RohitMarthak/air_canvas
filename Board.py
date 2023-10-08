import numpy as np
import cv2

class Board:

    def __init__(self,board_color=(0,0,0),cursor_color = (0,255,0),cursor_size = 1,draw_thickness = 3):
        self.canvas = np.zeros((500, 500, 3), dtype="uint8")
        self.cursor_img = np.zeros((500 ,500 ,3),dtype="uint8")


    def display(self):
        cv2.imshow("canvas",self.canvas)

    def reset_board(self):
            self.canvas = np.zeros((500, 500, 3), dtype="uint8")
            self.display()

    def draw(self,prevPos, currentPos):

        height, width, _ = self.canvas.shape
        prevPos = (width - prevPos[0], prevPos[1])
        currentPos = (width - currentPos[0], currentPos[1])
        cv2.line(self.canvas, prevPos, currentPos, (255, 0, 0), thickness=3)

    def draw_cursor(self, cursor_pos):
        cv2.circle(self.cursor_img, (cursor_pos[0], cursor_pos[1]), 1, (0, 255, 0), cv2.FILLED)