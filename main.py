# Import needed libraries
import sys
# QtWidgets to work with widgets
from PyQt5 import QtWidgets
# QPixmap to work with images
from PyQt5.QtGui import QPixmap

import design_gui
from objectDetectionImg import object_detection


class MainApp(QtWidgets.QMainWindow, design_gui.Ui_MainWindow):
    # Constructor of the class
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnLoadImg.clicked.connect(self.image_process)
        
    def image_process(self):

        self.lblImage.setText('Processing ...')
	# Limit the file dialog only .png,.jpg,.bmp
        image_path = \
            QtWidgets.QFileDialog.getOpenFileName(self, 'Choose Image to Open',
                                                  '.',
                                                  '*.png *.jpg *.bmp')



        image_path = image_path[0]  

        # Calling in other method
        object_detection(image_path)
	#self.lbl_path.setText(image_path)
        
        pixmap_image = QPixmap('detected.jpg')

        # Passing opened image to the Label object
        self.lblImage.setPixmap(pixmap_image)

        # Getting opened image width and height
        # And resizing Label object according to these values
        self.lblImage.resize(pixmap_image.width(), pixmap_image.height())


def main():
    
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

