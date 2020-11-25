from View.gui import Ui_MainWindow
from PyQt5 import QtWidgets
import datetime
from Model.model import request, request_img
from PyQt5.QtGui import QPixmap
import os


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dateEdit.setDate(datetime.date.today())
        self.ui.pushButton.setFocus()
        self.ui.explanation.setWordWrap(True)

        self.ui.pushButton.clicked.connect(self.push_btn)
        self.ui.download.clicked.connect(self.download)

    def push_btn(self):
        resp = request('https://api.nasa.gov/planetary/apod', self.ui.dateEdit.date().toString('yyyy-M-d'))
        self.ui.title.setText(resp.json()['title'])

        if resp.json()['media_type'] == 'image':
            if not os.path.isdir('cache'):
                os.mkdir('cache')

            cache_img_name = resp.json()['url'].split('/')[-1]

            with open('cache/{}'.format(cache_img_name), 'wb') as img:
                img.write(request_img(resp.json()['url']))

            pixmap = QPixmap('cache/{}'.format(cache_img_name))
            pixmap.setDevicePixelRatio(1.5)
            self.ui.image.setPixmap(pixmap)
        else:
            self.ui.image.setText(resp.json()['url'])

        self.ui.date.setText(resp.json()['date'])
        if 'copyright' in resp.json():
            self.ui.copyright.setText(resp.json()['copyright'])
        else:
            self.ui.copyright.setText('None')
        self.ui.explanation.setText(resp.json()['explanation'])

    def download(self):
        resp = request('https://api.nasa.gov/planetary/apod', self.ui.dateEdit.date().toString('yyyy-M-d'))

        if resp.json()['media_type'] == 'image':
            if not os.path.isdir('Download'):
                os.mkdir('Download')

            download_img_name = resp.json()['hdurl'].split('/')[-1]

            with open('Download/{}'.format(download_img_name), 'wb') as img:
                img.write(request_img(resp.json()['hdurl']))
