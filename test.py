from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    questions = ['jackdaw', 'side', 'boil', 'roast', 'torture']
    answers = [['пчела', 'воробей', 'галка'], 
            ['сторона', 'угол', 'поворот'], 
            ['варить', 'жарить', 'резать'], 
            ['варить', 'жарить', 'резать'], 
            ['бег', 'тополь', 'пытка']]
    right_ans = [2, 0, 0, 1, 2]
    counter = 0
    global_index = 0
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(390, 10, 75, 23))
        self.btnStart.setObjectName("btnStart")
        self.btnAns1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAns1.setGeometry(QtCore.QRect(40, 170, 131, 23))
        self.btnAns1.setText("")
        self.btnAns1.setObjectName("btnAns1")
        self.btnAns3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAns3.setGeometry(QtCore.QRect(410, 170, 131, 23))
        self.btnAns3.setText("")
        self.btnAns3.setObjectName("btnAns3")
        self.btnAns2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAns2.setGeometry(QtCore.QRect(220, 170, 131, 23))
        self.btnAns2.setText("")
        self.btnAns2.setObjectName("btnAns2")
        self.labelQuestion = QtWidgets.QLabel(self.centralwidget)
        self.labelQuestion.setGeometry(QtCore.QRect(20, 60, 551, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelQuestion.setFont(font)
        self.labelQuestion.setText("")
        self.labelQuestion.setObjectName("labelQuestion")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.btnAns1.setHidden(True)
        self.btnAns2.setHidden(True)
        self.btnAns3.setHidden(True)
        
        
        
        self.add_functions()
        
    
    def add_functions(self):
        self.btnStart.clicked.connect(self.start)
        self.btnAns1.clicked.connect(self.btnAnsFirstHandler)
        self.btnAns2.clicked.connect(self.btnAnsSecondHandler)
        self.btnAns3.clicked.connect(self.btnAnsThirdHandler)
        
    def btnAnsFirstHandler(self):
        if self.right_ans[self.global_index] == 0:
            self.counter += 1 
        self.global_index += 1
        self.start()
        
    def btnAnsSecondHandler(self):
        if self.right_ans[self.global_index] == 1:
            self.counter += 1 
        self.global_index += 1
        self.start()
    
    def btnAnsThirdHandler(self):
        if self.right_ans[self.global_index] == 2:
            self.counter += 1 
        self.global_index += 1
        self.start()
    
    def setQuestion(self, index):
        self.labelQuestion.setText(f'Как переводится {self.questions[index]}:')
        self.btnAns1.setText(self.answers[index][0])
        self.btnAns2.setText(self.answers[index][1])
        self.btnAns3.setText(self.answers[index][2])
    
    def showResult(self):
        self.labelQuestion.setText(f'Правильных ответов: {self.counter}')
        self.global_index = 0
        self.counter = 0
        self.btnStart.setHidden(False)
        self.btnAns1.setHidden(True)
        self.btnAns2.setHidden(True)
        self.btnAns3.setHidden(True)
        
        
    def start(self):
        self.btnAns1.setHidden(False)
        self.btnAns2.setHidden(False)
        self.btnAns3.setHidden(False)
        self.btnStart.setHidden(True)
        
        
        if self.global_index == 0:
            self.setQuestion(0)
            return
        if self.global_index == 1:
            self.setQuestion(1)
            return
        if self.global_index == 2:
            self.setQuestion(2)
            return
        if self.global_index == 3:
            self.setQuestion(3)
            return
        if self.global_index == 4:
            self.setQuestion(4)
            return
        if self.global_index == 5:
            self.showResult()
            return
                
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Тест по английскому"))
        self.btnStart.setText(_translate("MainWindow", "Начать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
