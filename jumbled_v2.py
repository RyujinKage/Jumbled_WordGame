# Python program for jumbled words game. 

import random 


# Choose random word
def choose():  
	words = ['database', 'engineering', 'computer', 'science', 'programming', 
			'mathematics', 'player', 'condition', 'reverse', 
			'water'] 
     
	pick = random.choice(words) 

	return pick 


#jumble
def jumble(word):  
	random_word = random.sample(word, len(word)) 
. 
	jumbled = ''.join(random_word) 
	return jumbled 


# Score
def thank(p1n, p2n, p1, p2): 
	print(p1n, 'Your score is :', p1) 
	print(p2n, 'Your score is :', p2) 

	# check_win
	check_win(p1n, p2n, p1, p2) 

	print('Thanks!') 


# Function for declaring winner 
def check_win(player1, player2, p1score, p2score): 
	if p1score > p2score: 
		print("winner is :", player1) 
	elif p2score > p1score: 
		print("winner is :", player2) 
	else: 
		print("Draw..Well Played guys..") 


# Function for playing the game. 
def play(): 
	p1name = input("player 1, Please enter your name :") 
	p2name = input("Player 2 , Please enter your name: ") 
	pp1 = 0
	pp2 = 0
	turn = 0
  
	while True: 
 
		picked_word = choose()  
		qn = jumble(picked_word) 
		print("jumbled word is :", qn) 

		if turn % 2 == 0: 
    
			print(p1name, 'Your Turn.') 

			ans = input("Pick a word ") 

			if ans == picked_word: 1 
				pp1 += 1

				print('Your score is :', pp1) 
				turn += 1

			else: 
				print("Better luck next time ..") 

				print(p2name, 'Your turn.') 

				ans = input('Pick your word ') 

				if ans == picked_word: 
					pp2 += 1
					print("Your Score is :", pp2) 

				else: 
					print("Better luck next time...correct word is :", picked_word) 

				c = int(input("press 1 to continue and 0 to quit :")) 
				if c == 0: 
					thank(p1name, p2name, pp1, pp2) 
					break

		else: 

			print(p2name, 'Your turn.') 
			ans = input('Pick your word ') 

			if ans == picked_word: 
				pp2 += 1
				print("Your Score is :", pp2) 
				turn += 1

			else: 
				print("Better luck next time.. :") 
				print(p1name, 'Your turn.') 
				ans = input('Pick your word ') 

				if ans == picked_word: 
					pp1 += 1
					print("Your Score is :", pp1) 

				else: 
					print("Better luck next time...correct word is :", picked_word) 

					c = int(input("press 1 to continue and 0 to quit :")) 

					if c == 0: 
						thank(p1name, p2name, pp1, pp2) 
						break

			c = int(input("press 1 to continue and 0 to quit :")) 
			if c == 0:
				thank(p1name, p2name, pp1, pp2) 
				break

if __name__ == '__main__': 
	
	# play() function calling 
	play() 
