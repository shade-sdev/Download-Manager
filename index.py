from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import os
import os.path
from PyQt5.uic import loadUiType
import urllib.request

ui,_ = loadUiType('main.ui')

class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        self.Handle_Buttons()
       
    def InitUI(self):
        ## Contain all ui changes in loading
        pass

    def Handle_Buttons(self):
        ## Handle all buttons in the app
        self.pushButton.clicked.connect(self.Download)
        self.pushButton_2.clicked.connect(self.Handle_Browse)
        pass

    def Handle_Progress(self, blocknum, blocksize, totalsize):
        # Calculate progress in the app
        readed_data = blocknum * blocksize
        if totalsize > 0 :
            download_percentage = readed_data * 100 / totalsize
            self.progressBar.setValue(download_percentage)
            QApplication.processEvents()


    def Handle_Browse(self):
        ## Enable browsing to our os, choose save location
        save_location  = QFileDialog.getSaveFileName(self, caption="Save As ", directory=".", filter="All Files(*.*)")
        print(save_location)
        self.lineEdit_2.setText(str(save_location[0]))

    def Download(self):
        ## Downloading any file
        print('Starting Download')

        download_url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        
        if download_url == '' or save_location == '':
            QMessageBox.warning(self, "Data Error!", "Provide valid URL or Save Location")
        else:
            try:
                urllib.request.urlretrieve(download_url, save_location, self.Handle_Progress)
                QMessageBox.information(self, "Download Complete!", "Download has completed.")
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.progessBar.setValue(0)
            except Exception:
                 QMessageBox.warning(self, "Download Error!", "Provide valid URL or Save Location")
                 return

        

    def Save_Browse(self):
        ## Save location in the line edit
        pass


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()



