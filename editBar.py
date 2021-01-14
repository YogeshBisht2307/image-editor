from tkinter import Frame, Button, LEFT
from tkinter import filedialog
from filterFrame import FilterFrame
from adjustFrame import AdjustFrame
import cv2


class EditBar(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master,bg="black")

        #declaring the menu buttons
        self.new_button = Button(self, bg="green" , fg="white", text="New")
        self.save_button = Button(self, text="Save", bg="blue" , fg="white",)
        self.save_as_button = Button(self, text="Save as", bg="blue" , fg="white",)
        self.draw_button = Button(self, text="Draw", bg="black" , fg="white",)
        self.crop_button = Button(self, text="Crop", bg="black" , fg="white",)
        self.filter_button = Button(self, text="Filter", bg="black" , fg="white",)
        self.adjust_button = Button(self, text="Adjust", bg="black" , fg="white",)
        self.clear_button = Button(self, text="Clear", bg="red" , fg="white",)

        #declaring function on menu buttons
        self.new_button.bind("<ButtonRelease>", self.new_button_released)
        self.save_button.bind("<ButtonRelease>", self.save_button_released)
        self.save_as_button.bind("<ButtonRelease>", self.save_as_button_released)
        self.draw_button.bind("<ButtonRelease>", self.draw_button_released)
        self.crop_button.bind("<ButtonRelease>", self.crop_button_released)
        self.filter_button.bind("<ButtonRelease>", self.filter_button_released)
        self.adjust_button.bind("<ButtonRelease>", self.adjust_button_released)
        self.clear_button.bind("<ButtonRelease>", self.clear_button_released)

        #packing and positioning menu buttons
        self.new_button.pack(side=LEFT)
        self.save_button.pack(side=LEFT)
        self.save_as_button.pack(side=LEFT)
        self.draw_button.pack(side=LEFT)
        self.crop_button.pack(side=LEFT)
        self.filter_button.pack(side=LEFT)
        self.adjust_button.pack(side=LEFT)
        self.clear_button.pack()

    #defining the function of menu buttons
    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:
            # deactivating the image viewer when in the draw,or crop state
            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()
            #opening the location of new photo
            filename = filedialog.askopenfilename()
            #reading the filename by using opencv and return geoometry of image
            image = cv2.imread(filename)
            if image is not None:
                self.master.filename = filename
                #using copy function so that we can get back to the original image after clearing filters.
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                #showing image using show_image function
                self.master.image_viewer.show_image()
                #assigning status of image weather seleted or not
                self.master.is_image_selected = True

    def save_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_button:
            # saving image when it is selected
            if self.master.is_image_selected:
                # deactivating the image viewer when in the draw,or crop state
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()

                #saving image
                save_image = self.master.processed_image
                image_filename = self.master.filename
                cv2.imwrite(image_filename, save_image)

    def save_as_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
            #saving image when it is selected
            if self.master.is_image_selected:
                #deactivating the image viewer when in the draw or crop state
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                #spliting the file name from . and leaving the last charecter [-1]
                original_file_type = self.master.filename.split('.')[-1]
                #asking the name of file that which name do you want to take
                filename = filedialog.asksaveasfilename()

                #updating file name
                filename = filename + "." + original_file_type

                save_image = self.master.processed_image
                cv2.imwrite(filename, save_image)

                self.master.filename = filename

    def draw_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.draw_button:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                #if image is not in crop_state ro draw state activating the draw state
                else:
                    self.master.image_viewer.activate_draw()

    def crop_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.crop_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                #if image not inn draw_state or crop_state activating the crop state
                else:
                    self.master.image_viewer.activate_crop()

    def filter_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.filter_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                #activating the filter frame class
                self.master.filter_frame = FilterFrame(master=self.master)
                self.master.filter_frame.grab_set()

    def adjust_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.adjust_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                #activating adjustframe class
                self.master.adjust_frame = AdjustFrame(master=self.master)
                self.master.adjust_frame.grab_set()

    def clear_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.clear_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                #clearing all the operating and returning to the original image
                self.master.processed_image = self.master.original_image.copy()
                #showing the image after clearning all the filters
                self.master.image_viewer.show_image()
