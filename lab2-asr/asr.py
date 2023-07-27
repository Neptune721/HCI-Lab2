from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import Ui_MainWindow
import sys
import threading
import webbrowser
import os
import speech_recognition as sr

import win32api

class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.recognize_btn.clicked.connect(self.listen_thread)
        self.ui.text_btn.clicked.connect(self.text_thread)


    def text_thread(self):
        t2 = threading.Thread(target=self.text_changed)
        t2.setDaemon(True)
        t2.start()


    def text_changed(self):
        text = self.ui.textbox.text()
        print(text)
        if "music" in text:
            self.ui.label.setText("You said: \" " + text + "\"")
            win32api.ShellExecute(0, 'open', 'music.mp3', '', '', 1)
        elif "text" in text:
            self.ui.label.setText("You said: \"" + text + "\"")
            win32api.ShellExecute(0, 'open', 'text.txt', '', '', 0)
        elif "search" in text:
            text = text.replace('search', '')
            url = 'https://www.google.com/search?q=' + text
            webbrowser.open(url)
        else:
            self.ui.label.setText("You means: \" " + text + "\"\nThis is not a valid command.")

    def listen_thread(self):
        self.ui.label.setText("I'm listening...... ")
        t1 = threading.Thread(target=self.listen)
        t1.setDaemon(True)
        t1.start()

    #声音识别及处理函数
    def listen(self):
        # Working with Microphones
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Please say what you want to do：")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if "music" in text:
                self.ui.label.setText("You said: \" " + text + "\"")
                win32api.ShellExecute(0, 'open', 'music.mp3', '', '', 1)
            elif "text" in text:
                self.ui.label.setText("You said: \"" + text + "\"")
                win32api.ShellExecute(0, 'open', 'text.txt', '', '', 0)
            elif "search" in text:
                text = text.replace('search', '')
                url = 'https://www.google.com/search?q=' + text
                webbrowser.open(url)
            else:
                self.ui.label.setText("You said: \" " + text + "\"\nThis is not a valid command.")
        except sr.UnknownValueError:
            self.ui.label.setText("Can't recognize your voice")
        except sr.RequestError as e:
            self.ui.label.setText("无法从Google Speech Recognition服务请求结果；{0}".format(e))



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = myWindow()
    application.show()
    sys.exit(app.exec_())


