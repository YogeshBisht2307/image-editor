from tkinter import Toplevel, Button, RIGHT,LEFT, TOP, BOTTOM
import numpy as np
import cv2

#top level windwo for filter frame
class FilterFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master, bg="black",width=300,padx=20,pady=20, height=200)

        self.original_image = self.master.processed_image
        self.filtered_image = None

        self.negative_button = Button(master=self, text="Negative",bg="black" ,width=40, fg="white")
        self.black_white_button = Button(master=self, text="Black White", bg="black" ,width=40, fg="white")
        self.sepia_button = Button(master=self, text="Sepia",bg="black" ,width=40, fg="white")
        self.emboss_button = Button(master=self, text="Emboss",bg="black" , width=40,fg="white")
        self.gaussian_blur_button = Button(master=self, text="Gaussian Blur",bg="black" ,width=40, fg="white")
        self.cancel_button = Button(master=self, text="Cancel",bg="red" , fg="white")
        self.apply_button = Button(master=self, text="Apply",bg="blue" , fg="white")

        #defining event on button realse

        self.negative_button.bind("<ButtonRelease>", self.negative_button_released)
        self.black_white_button.bind("<ButtonRelease>", self.black_white_released)
        self.sepia_button.bind("<ButtonRelease>", self.sepia_button_released)
        self.emboss_button.bind("<ButtonRelease>", self.emboss_button_released)
        self.gaussian_blur_button.bind("<ButtonRelease>", self.gaussian_blur_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)
         #packing those button on the TopLevel
        self.negative_button.pack()
        self.black_white_button.pack()
        self.sepia_button.pack()
        self.emboss_button.pack()
        self.gaussian_blur_button.pack()
        self.cancel_button.pack(side=RIGHT)
        self.cancel_button.pack(side=RIGHT)
        self.apply_button.pack(side=LEFT)

    def negative_button_released(self, event):
        #calling negative function
        self.negative()
        self.show_image()

    def black_white_released(self, event):
        self.black_white()
        self.show_image()

    def sepia_button_released(self, event):
        self.sepia()
        self.show_image()

    def emboss_button_released(self, event):
        self.emboss()
        self.show_image()

    def gaussian_blur_button_released(self, event):
        self.gaussian_blur()
        self.show_image()

    def apply_button_released(self, event):
        self.master.processed_image = self.filtered_image
        self.show_image()
        self.close()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.filtered_image)

    def negative(self):
        self.filtered_image = cv2.bitwise_not(self.original_image)

    def black_white(self):
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)

    def sepia(self):
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])

        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)

    def emboss(self):
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])

        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)

    def gaussian_blur(self):
        self.filtered_image = cv2.GaussianBlur(self.original_image, (41, 41), 0)


    def close(self):
        self.destroy()
