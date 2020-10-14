from more_itertools import locate
import random 
import sys


lst = ['arbitrary' ,'bald','hello' , 'difficult' , 'dictionary' , 'music','breathren' , 'genre' , 'ambition' , 'python' , 'snake' , 'game','guitar']

word = lst[random.randint(0 , len(lst) - 1)]
out = '_'*len(word)
i = 0
chances = 6
w = ''.join(word)

print('Hello....Welcome to HANGMAN.. \nThe rules here are simple...\nu are given a random word...\nu have to guess the word by guessing a alphabet in the word... \nFailing 6 times will result the game to be over \nLets begin \n ')

def printHangman(n):
	
	face = '             O'
	belly='             |'
	leg1='            / '
	leg2='\ '
	hand1='            \|'
	hand2='/'
	
	
	
	str = '-----------------\n|{face}\n|{h1}{h2}\n|{b}\n|{l1}{l2}\n|\n|\n|'.format(
	face= face if n <6 else  '',h1=hand1 if n<5 else '',h2=hand2 if n<4 else '' ,b = belly if n<3 else '',l1 = leg1 if n<2 else '',l2 = leg2 if n<1 else ''
	)
	print(str)
	




def hangman():
	global word
	global out
	global chances
	if chances ==  0:
		printHangman(chances)								
		print(f'You lose..... \nThr word was {word}\nBetter luck next time....')
		sys.exit()
		
	out = list(out)
	
	if '_' not in out:
		
		printHangman(chances)
		print('\n\nYou won!!! 😎😎😎... Thanks for playing...')
		sys.exit()
		
	word = list(word)
	print(' '.join(out))
		
	userChar = input('guess a word')
	
	if len(userChar) > 1 or userChar.isalpha() == False:
		print('invalid user input..u can only enter a single alphabet as input')
		hangman()
		
	elif userChar not in word or userChar in out:
		print('wrong guess😑')
		chances -=1
		printHangman(chances)
		print(f'total chances remaining {chances}')
	else:
		a = list(locate(word,  lambda x: x == userChar))
		for i in a:
			out[i] = userChar
		print(' '.join(out))
		print('right guess😁')
		printHangman(chances)
		print(f'total chances remaining {chances}')
		
while i  ==  0: 
	hangman()
	


