import random
import copy
import sys
chosen = ''
session = 0
user = 0
dev = 0
coin = ['head' , 'tail']
choices = ['bat' , 'bowl' , 'bat']

print('Welcome to HANDCRICKET....\nThr program replicates the classic handcricket game....\nRules:\nFirst a toss is held .. if u win u are given the chance to bowl or bat..\nIf ur score is greater than that of computer..u lose\n')

def get_int(prompt):
	while True:
		try:
			value = int(input(prompt))
			break
		except ValueError:
			print("\nSorry, I didn't understand that.\n")
			continue
            
	return value

while True:
	val = get_int('How many wickets u want in the game')
	if  val <= 0:
		print('Enter either 1 or 0')
	else:
		break

wicket = copy.deepcopy(val)
while True:
	
	ov = get_int('How many overs U want in the game')
	if ov <= 0:
		print('Over must be greater than 0')
	else:
		break
		
overs = copy.deepcopy(ov)
i = 0
j = 0


picked = get_int('Would You Pick Head or Tails \n [0] for heads , [1] for tails')

def toss():
	global chosen
	global compchoice
	result = coin[random.randint(0 , 1)]
	print(result)
	if coin.index(result) == picked:
		print('\nYou Won The Toss')
		chosen = choices[get_int('Would U Like To Bat Or Bowl , [0] for bat , [1] for bowl\n')]
		print(f'\nYou chose to {chosen}\n')
		
	else:
		print('\nYou Lost The Toss...Computer Won')
		chosen = choices[random.randint(0 , 1)]
		
		print(f'\nComputer chose to { choices[choices.index(chosen)+1]}')
		print(f'You Will {chosen}\n')
	print()
	

def checkSession():
	global session
	global user
	global dev
	if session == 1:
		if chosen == 'bat':
			if user > dev:
				print(f'overs remaining {overs}\n')
				print(f'You won ... Your end score was {user} ... Congrats..\nThanks for playing\n')
				sys.exit()
		else:
			if dev > user:
				print(f'overs remaining {overs}\n')
				print(f'You Lost ... Computer Won....Your end score was {user}\n')
				sys.exit()
				
	if session == 2:
		if user > dev:
			print(f'overs remaining {overs}\n')
			print(f'You won ... Your end score was {user} ... Congrats..\nThanks for playing\n')
			sys.exit()
		elif user < dev:
			print(f'overs remaining {overs}\n')
			print(f'You Lost ... Computer Won....Your end score was {user}\n')
			sys.exit()





def handcricket():
	global i
	global wicket
	global user
	global dev
	global session
	global chosen
	global overs
	global j
	global val
	global ov
	j+=1
	if overs < ov or j!=1:
		i+=1
	checkSession()
	if overs == 0  :
		
		i = -1
		session += 1
		if session == 2:
				checkSession()
		overs = copy.deepcopy(ov)
		wicket = copy.deepcopy(val)
		if chosen == 'bat':
			chosen = 'bowl'
			print('\n\nEnd of Innings\n\nEnd of Batting...Get ready to bowl\n\n')
					
			print(f'Your Score is {user}\nComputers score is {dev}\n')
		elif chosen == 'bowl':
			chosen = 'bat'
			print('\n\nEnd of innings\n\nEnd of Bowling...Get ready to bat\n\n')
			print(f'Your score is {user}\nComputers score is {dev}\n')
		
		handcricket()
		
	if i // 6 == 1:
		overs -= 1
		i = -1
		print(f'End of one over , remaining {overs}\n') 
		handcricket()
		
		
			
	if wicket == 0:
			session += 1
			print(f'All wickets are gone\n{overs} overs were remaining\n')
			if session == 2:
				checkSession()
				
			overs = copy.deepcopy(ov)
			i=-1
			wicket = copy.deepcopy(val)
			if chosen == 'bat' :
				print('\n\nEnd of innings\n\nEnd of Batting...Get ready to bowl\n\n')
					
				print(f'Your Score is {user}\nComputers score is {dev}\n')
				chosen = 'bowl'
				handcricket()
					
					
			elif chosen == 'bowl':
				print('\n\nEnd of innings\n\nEnd of Bowling...Get ready to bat\n\n')
				print(f'Your score is {user}\nComputers score is {dev}\n')
				chosen = 'bat'
				handcricket()
			
					
					
		
	player = get_int('Chose a number from 1 to 6\n')
	if player > 6 or player < 1:
		print('number must be greater than one and smaller than 6 \n')
		i -= 1
		handcricket()
	print(f'You Chose {player}\n')
	comp = random.randint(1 , 6)
	print(f'Computer Chose {comp}\n')
			
			
			
	if player == comp:
		wicket -= 1
		print('wicket\n')
		if chosen == 'bat':
			print(f'You lost a wicket , remaining wickets = {wicket} \n Ur Score is {user}\n')
			handcricket()
		else:
			print(f'Computer Lost a wicket , remaining {wicket}\n')
		handcricket()
				
	else:
				
				
		if chosen == 'bat':
			user += player
			print(f'Players score is {user}\n')
			handcricket()
		else:
			dev += comp
			print(f'Computers score is {dev}\n')
			handcricket()
					
			
		
toss()	
handcricket()