import numpy as np
import cv2

class Board:

    def __init__(self,board_color=(255,255,255),draw_thickness = 6,draw_color=(0,0,0)):

        self.draw_thickness = draw_thickness
        self.cursor = np.zeros((500,500,3),dtype="uint8")
        self.board_color = board_color
        self.canvas = np.full((500, 500, 3),self.board_color,dtype="uint8")

    def display(self,currentPos):

        self.currentPos = currentPos
        display_canvas = self.canvas.copy()
        cv2.circle(display_canvas, (self.canvas.shape[1] - currentPos[0], currentPos[1]), 4,(0,255,0))
        cv2.imshow("canvas",display_canvas)

    def reset_board(self):

        self.canvas = np.full((500, 500, 3),self.board_color, dtype="uint8")
        self.display(self.currentPos)

    def draw(self,prevPos, currentPos):

        height, width, _ = self.canvas.shape
        prevPos = (width - prevPos[0], prevPos[1])
        currentPos = (width - currentPos[0], currentPos[1])
        cv2.line(self.canvas, prevPos, currentPos, (255, 0, 0), thickness=self.draw_thickness)


    def erase(self,currentPos):

        cv2.circle(self.canvas,(self.canvas.shape[1]-currentPos[0],currentPos[1]),5,self.board_color,cv2.FILLED)


    # def change_board_color(self):
    #
    #     self.canvas+(255,255,255)