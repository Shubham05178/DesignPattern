import time
class HighResolutionImage:
    def __init__(self,file_name):
        self.__file_name=file_name
        self.__image_data=None
        self._load_img()
    def _load_img(self):
        time.sleep(1)
        self.__image_data=f"[[LOADED DATA OF {self.__file_name}]]"
        print(f"Loaded data of {self.__file_name}")
        
    def display(self):
        print(f"{self.__image_data}")
class ImageProxy:
    def __init__(self,file_name):
        self.__file_name=file_name
        self.__real_img=None
    def display(self):
        if self.__real_img is None:
            self.__real_img=HighResolutionImage(self.__file_name)
        self.__real_img.display()
class PhotoGallery:
    def __init__(self):
        self._images:list[ImageProxy]=[]
    def add_image(self,file_name):
        image_proxy=ImageProxy(file_name)
        self._images.append(image_proxy)
    def display_gallery(self):
        for image in self._images:
            image.display()

    def show_image(self, index: int):
        self._images[index - 1].display()

start_time = time.time()
photo_gallery = PhotoGallery()
photo_gallery.add_image("image1.png")
photo_gallery.add_image("image2.png")
photo_gallery.add_image("image3.png")
photo_gallery.add_image("image4.png")
end_time = time.time()
print(f"{end_time - start_time:.1f}")

photo_gallery.show_image(2)
print("----------")
photo_gallery.show_image(2)
print("----------")
photo_gallery.show_image(2)
print("----------")
photo_gallery.show_image(2)
photo_gallery.show_image(3)