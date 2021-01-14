from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL, RIGHT, LEFT
import tkinter as tk
from tkinter import ttk
import cv2


#top level window for adjustment frame

class AdjustFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master,bg="black",width=300,padx=20,pady=20, height=200)

        self.brightness_value = 0
        self.previous_brightness_value = 0

        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image
        #defining label for handling brightness
        self.brightness_label = Label(self, text="Brightness",bg="black")
        self.brightness_scale = Scale(self, from_=0, to_=2, length=250, resolution=0.1,
                                      orient=HORIZONTAL,bg="grey")
        #defining label for handling Red value
        self.r_label = Label(self, text="R",background="black")
        self.r_scale = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL,bg="red")
        #defining label for handling Green value
        self.g_label = Label(self, text="G",bg="black")
        self.g_scale = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL,bg="green")
        #defining label for handling Blue value
        self.b_label = Label(self, text="B",bg="black")
        self.b_scale = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL,bg="blue")
        #buttons to apply,see, or delete adjustment of image
        self.apply_button = Button(self, text="Apply" ,bg="blue",fg="white")
        self.preview_button = Button(self, text="Preview", bg="yellow",fg="black")
        self.cancel_button = Button(self, text="Cancel", bg="red",fg="white")

        #setting the scale of brightness 0 to 1
        self.brightness_scale.set(1)
        separator2 = ttk.Separator(master=self, orient=tk.HORIZONTAL)
        #applying function on clicking apply, preview, and cancel button
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.preview_button.bind("<ButtonRelease>", self.show_button_release)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        #packing button and label on the toplevel
        self.brightness_label.pack()
        self.brightness_scale.pack()
        self.r_label.pack()
        self.r_scale.pack()
        self.g_label.pack()
        self.g_scale.pack()
        self.b_label.pack()
        self.b_scale.pack()
        separator2.pack(fill=tk.X, padx=20, pady=10)
        self.cancel_button.pack(side=RIGHT)
        self.apply_button.pack(side=LEFT)
        self.preview_button.pack(side=LEFT)


    #operation on pressing apply button
    def apply_button_released(self, event):
        self.master.processed_image = self.processing_image
        self.close()
    #operation on pressing preview button
    def show_button_release(self, event):
        self.processing_image = cv2.convertScaleAbs(self.original_image, alpha=self.brightness_scale.get())
        b, g, r = cv2.split(self.processing_image)

        for b_value in b:
            cv2.add(b_value, self.b_scale.get(), b_value)
        for g_value in g:
            cv2.add(g_value, self.g_scale.get(), g_value)
        for r_value in r:
            cv2.add(r_value, self.r_scale.get(), r_value)

        self.processing_image = cv2.merge((b, g, r))
        self.show_image(self.processing_image)
    #closing the image on pressing cancel button
    def cancel_button_released(self, event):
        self.close()
    #function for showing image
    def show_image(self, img=None):
        self.master.image_viewer.show_image(img=img)
    #function for closing the adjustment toplevel
    def close(self):
        self.show_image()
        self.destroy()