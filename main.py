#import required libraries
import pyqrcode
import png
from pyqrcode import QRCode

Qrstring="https://codestarshub.blogspot.com/2020/12/generate-qr-code-using-python.html" #variable to store our link
url=pyqrcode.create(Qrstring)#function to create the qr-code
url.png('C:/Users/hp/Desktop/qr.png',scale=8)#create and save the png file at the location

var=644
