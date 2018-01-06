import time
import random
"""1 = rock 
2 = paper
3 = scissor"""
def winlose(userHand,botHand):
	try:
		if(userHand != 1 and userHand != 2 and userHand != 3):
			print("invalid input")
			main()
		elif(userHand == 1 and botHand == 3):
			print("you win")
		elif(userHand == 1 and botHand == 2):
			print("you lost")
		elif(userHand == 1 and botHand == 1):
			print("you draw")
		elif(userHand == 2 and botHand == 2):
			print("you draw")
		elif(userHand == 2 and botHand == 1):
			print(" you win ")
		elif(userHand == 2 and botHand == 3):
			print("you lost")
		elif(userHand == 3 and botHand == 1):
			print("you lost")
		elif(userHand == 3 and botHand == 2):
			print("you win")
		else:
			print("you draw")
		time.sleep(2)
	except:
		print("unknown error 2")

def replay():
	while (10 == 10):
		
			retry = input("do you want to rerun? (y and n):  ")
			if(retry == "y"):
				main()
			elif(retry == 'n'):
				quit()
			else:
				print("invalid input")
				continue
		



def main():
	while (1 == 1):
		try:
			botHand = random.randint(1, 3)
			userHand = int(input("insert 1 for rock, 2 for paper and 3 for scissor:  "))
			print("bot inserted:  " + str(botHand))
			print("and you inserted:  " + str(userHand))
			print("result are:")
			winlose(userHand, botHand)
			replay()
		except ValueError:
			print("invalid input, try again")
			continue
		except:
			if(retry == "n"):
				quit()
			else:
				print("unknown error 1")
				continue
			


main()
