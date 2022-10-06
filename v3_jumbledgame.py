# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Python ")

		# setting geometry
		self.setGeometry(100, 100, 320, 350)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

		# words
		self.words = ['red', 'cold', 'hot', 'geeks', 'rain',
						'black', 'snow', 'hills', 'code']

		# current word
		self.current_text = ""

	# method for components
	def UiComponents(self):

		# creating head label
		head = QLabel("Jumbled Word Game", self)

		# setting geometry to the head
		head.setGeometry(20, 10, 280, 60)

		# font
		font = QFont('Times', 15)
		font.setBold(True)
		font.setItalic(True)
		font.setUnderline(True)

		# setting font to the head
		head.setFont(font)

		# setting alignment of the head
		head.setAlignment(Qt.AlignCenter)

		# setting color effect to the head
		color = QGraphicsColorizeEffect(self)
		color.setColor(Qt.darkCyan)
		head.setGraphicsEffect(color)

		# creating label to show the jumbled word
		self.j_word = QLabel(self)

		# setting geometry
		self.j_word.setGeometry(30, 80, 260, 50)

		# setting style sheet
		self.j_word.setStyleSheet("border : 2px solid black; background : white;")

		# setting font
		self.j_word.setFont(QFont('Times', 12))

		# setting alignment
		self.j_word.setAlignment(Qt.AlignCenter)


		# creating a line edit widget to het the text
		self.input = QLineEdit(self)

		# setting geometry
		self.input.setGeometry(20, 150, 200, 40)

		# setting alignment
		self.input.setAlignment(Qt.AlignCenter)

		# creating push button to check the input
		self.check = QPushButton("Check", self)

		# setting geometry
		self.check.setGeometry(230, 155, 80, 30)

		# adding action to the check button
		self.check.clicked.connect(self.check_action)

		# result label
		self.result = QLabel(self)

		# setting geometry
		self.result.setGeometry(40, 210, 240, 50)

		# setting font
		self.result.setFont(QFont('Times', 13))

		# setting alignment
		self.result.setAlignment(Qt.AlignCenter)

		# setting style sheet
		self.result.setStyleSheet("border : 2px solid black; background : yellow;")

		# creating push buttons to start and reset the game
		start = QPushButton("Start", self)
		reset = QPushButton("Reset", self)

		# setting geometry to both the button
		start.setGeometry(15, 290, 140, 40)
		reset.setGeometry(165, 290, 140, 40)

		# adding action to both the buttons
		start.clicked.connect(self.start_action)
		reset.clicked.connect(self.reset_action)

	def check_action(self):

		# getting text from the line edit
		text = self.input.text()

		# checking if text is similar to the current text
		if text == self.current_text:
			self.result.setText("Correct Answer")

			# making result color green
			self.result.setStyleSheet("background : lightgreen;")

		else:
			self.result.setText("Wrong Answer")

			# making result color red
			self.result.setStyleSheet("background : red;")



	def start_action(self):

		# selecting one word
		self.current_text = random.choice(self.words)

		# sample() method shuffling the characters of the word
		random_word = random.sample(self.current_text, len(self.current_text))

		# join() method join the elements
		# of the iterator(e.g. list) with particular character .
		jumbled = ''.join(random_word)

		# setting text to the jumbled word
		self.j_word.setText(jumbled)

		# setting result text to blank
		self.result.setText("")

		# making result label color yellow
		self.result.setStyleSheet("border : 2px solid black; background : yellow;")

		# setting text of input to blank
		self.input.setText("")

	def reset_action(self):

		# setting current text blank
		self.current_text = ""

		# setting text of input to blank
		self.input.setText("")

		# clear the text of all the labels
		self.j_word.setText("")
		self.result.setText("")

		# making result label color yellow
		self.result.setStyleSheet("border : 2px solid black; background : yellow;")



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
