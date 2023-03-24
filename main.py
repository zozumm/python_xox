import sys
from PyQt5.QtWidgets import QApplication
from xox_oyun import Oynama

uygulama=QApplication(sys.argv)

xox_oyun=Oynama()
sys.exit(uygulama.exec_())