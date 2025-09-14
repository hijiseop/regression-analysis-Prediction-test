import sys
import PreProcessing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Prediction.ui")[0]
p = PreProcessing.PreProcess()
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #LearningRate PredictionData Null textedit conect
        self.StartButton.clicked.connect(self.TextFunction)
        self.checkBox.stateChanged.connect(self.chkFunction)
        self.checkBox_2.stateChanged.connect(self.chkFunction)
        self.checkBox_3.stateChanged.connect(self.chkFunction)
        self.UploadButton.clicked.connect(self.upbtFunction)
        self.StopButton.clicked.connect(self.stbtFunction)
        self.CancelButton.clicked.connect(self.cabtFunction)  
        
        

    #ceckbox read
    def chkFunction(self) :
        if self.checkBox.isChecked() : print("c1")
        if self.checkBox_2.isChecked() : print("c2")
        if self.checkBox_3.isChecked() : print("c3")

    #learning function read
    def TextFunction(self) :
        print(self.plainTextEdit.toPlainText())
        print(self.plainTextEdit_2.toPlainText())
        print(self.plainTextEdit_3.toPlainText())

    #upload file
    def upbtFunction(self) :
        fname = QFileDialog.getOpenFileName(self)
        self.plainTextEdit_5.setPlainText(fname[0])
        graph = p.csvFileRead(fname[0])
        graph.savefig('12d.png')
        
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("12d.png")
        self.qPixmapVar = self.qPixmapVar.scaled(551,371)
        self.label.setPixmap(self.qPixmapVar)
        
        

    def stbtFunction(self) :
        print("st")
    def cabtFunction(self) :
        print("ca")

    

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()