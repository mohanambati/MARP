###############################################################################################
## CSCI 8480 Project- Multi-agent Rendezvous problem solution using stochastic game algorithm #
## Program Name: marp.py                                                                      #
## Written by: Mohan Ambati, Venkat Garlapati                                                 #
## Description: 	                                                                          #
## In this project, we are concerned with the collective behavior of a group of n>1 mobile    #
## agents, which can all move in a plane. The action set of each agent is {N, W, S, E}.       #
## The multi-agent rendezvous problem is to devise strategies for each agent to cause         #
## all the agents to eventually rendezvous at a single specified location. The approach is    #
## to use stochastic game where the agents repeatedly play games from the collection of       #
## normal form games, and the particular game played at any given iteration depends           #
## probabilistically on the previous game played and on the actions taken by all agents in    #
## that game. Here, each state is a normal form game played by n agents. The transition     # 
## probability is the probability of transitioning from one state to other state after joint  #
## action. Payoff matrix is generated for each player based on the real valued payoff function. 
## The objective of the project is to plan a collision free path for each player so that      #
## all the players in the game reach common goal location by minimizing the length of the path.
###############################################################################################

#####################################################################################
## Import statements
###################################################################################3#
import Tkinter as tk
import numpy as numpy
from project import *

#####################################################################################
## This function initializes the grid.
###################################################################################3#
def initialize():
	grid = creategrid()
	grid[19][19].configure(text = 'End')
	grid[19][19].configure(background = '#d4ac0d')

	grid[init_pos[0][0]][init_pos[0][1]].configure(background = 'blue')
	grid[init_pos[0][0]][init_pos[0][1]].configure(text = '1')

	grid[init_pos[1][0]][init_pos[1][1]].configure(background = 'red')
	grid[init_pos[1][0]][init_pos[1][1]].configure(text = '2')

	grid[init_pos[2][0]][init_pos[2][1]].configure(background = 'green')
	grid[init_pos[2][0]][init_pos[2][1]].configure(text = '3')

	grid[init_pos[3][0]][init_pos[3][1]].configure(background = 'yellow')
	grid[init_pos[3][0]][init_pos[3][1]].configure(text = '4')
	
	#grid[init_pos[4][0]][init_pos[4][1]].configure(background = '#641e16')
	#grid[init_pos[4][0]][init_pos[4][1]].configure(text = '5')
	#grid[3][1].configure(background = '#17202a')
	#grid[1][3].configure(background = '#424949')
	#grid[0][2].configure(background = '#0b5345')
	return grid
	
#####################################################################################
## This function resets the grid colour to white
###################################################################################3#
def resetcolours(grid):
	i = 0
	j = 0
	while i < 20:
		while j < 20:
			grid[i][j].configure(background = 'white')
			j = j + 1
		i = i + 1
		j = 0
#####################################################################################
## This function creates the grid.
###################################################################################3#
def creategrid():
	grid = []
	i = 0
	while i < 20:
		grid.append([])
		i = i + 1
	k = 0
	x_axis = 845
	y_axis = 40
	j = 0
	while j < 20:
		while k < 20:
			grid[k].append(tk.Label(screen,bg="white", width = 5, height = 2))
			k = k + 1
		j = j + 1
		k = 0
	grid = numpy.array(grid)
	i = 19
	j = 19
	while i >= 0 :
		while j >= 0:
			grid[i][j].place(x = x_axis, y = y_axis)
			y_axis = y_axis + 38			
			j = j - 1
		x_axis = x_axis - 42
		i = i - 1
		j = 19
		y_axis = 40
	return grid


#####################################################################################
## Reset the environment...This is callback function when we press reset button.
###################################################################################3#	
def resetenvironment():
	screen.poll = False
	global b
	b = 1
	k = 0
	global init_pos
	init_pos = [[],[],[],[]]
	while k < 4:
		print("player %s"%(k+1))
		init_pos[k].append(input("x:"))
		init_pos[k].append(input("y:"))
		k=k+1

	print(init_pos)
	grid = initialize()
	screen.poll = True

	
	

#####################################################################################
## ##TEMP function###This function adds grid number..(used for error checking)
###################################################################################3#
def countgrid():
	k = 0
	i = 0
	j = 0
	while j < 20 :
		while i < 20:
			grid[i][j].configure(text = k)
			k = k + 1
			i = i + 1
		j = j + 1
		i = 0
#####################################################################################
## This function adds delay to the program.
###################################################################################3#
def delay():
	k = 0
	while k <= 10000000/2:
		k = k + 1

#####################################################################################
## This function selects the player.
###################################################################################3#
def select_player(player):
	if player == 1:
		colour = 'blue'
		bg_colour = '#d6eaf8'
	if player == 2:
		colour = 'red'
		bg_colour = '#f5b7b1'
	if player == 3:
		colour = 'green'
		bg_colour = '#abebc6'
	if player == 4:
		colour = 'yellow'
		bg_colour = '#fcf3cf'
	if player == 5:
		colour = '#641e16'
		bg_colour = '#f2d7d5'
	#if player == 6:
	#	colour = '#17202a'
	#	bg_colour = '#abb2b9'
	#if player == 7:
	#	colour = '#424949'
	#	bg_colour = '#ccd1d1'
	#if player == 8:
	#	colour = '#0b5345'
#		bg_colour = '#d0ece7'
	return colour,bg_colour
#####################################################################################
## This function moves robot in upward direction.
###################################################################################3#
def moveup(player,ls,grid):
	y_ax = ls[1]
	if y_ax < 19 :
		y_ax = y_ax + 1
		colour,bg_colour = select_player(player)
		grid[ls[0]][ls[1]].configure(background = bg_colour)
		grid[ls[0]][ls[1]].configure(text = '')
		grid[ls[0]][y_ax].configure(background = colour)
		grid[ls[0]][y_ax].configure(text = player)
	return [ls[0],y_ax]

	
#####################################################################################
## This function moves robot in downward direction.
###################################################################################3#
def movedown(player,ls,grid):
	y_ax = ls[1] 
	if y_ax > 0:
		y_ax = y_ax - 1
		colour,bg_colour = select_player(player)
		grid[ls[0]][ls[1]].configure(background = bg_colour)
		grid[ls[0]][ls[1]].configure(text = '')
		grid[ls[0]][y_ax].configure(background = colour)
		grid[ls[0]][y_ax].configure(text = player)	
	return [ls[0], y_ax]

#####################################################################################
## This function moves robot in rightside.
###################################################################################3#
def moveright(player,ls,grid):
	x_ax = ls[0]
	if x_ax < 19:
		x_ax = x_ax + 1
		colour,bg_colour = select_player(player)
		grid[ls[0]][ls[1]].configure(background = bg_colour)
		grid[ls[0]][ls[1]].configure(text = '')
		grid[x_ax][ls[1]].configure(background = colour)
		grid[x_ax][ls[1]].configure(text = player)		
	return [x_ax, ls[1]]

#####################################################################################
## This function moves robot in leftside.
###################################################################################3#
def moveleft(player,ls,grid):
	x_ax = ls[0]
	if x_ax > 0:
		x_ax = x_ax - 1
		colour,bg_colour = select_player(player)
		grid[ls[0]][ls[1]].configure(background = bg_colour)
		grid[ls[0]][ls[1]].configure(text = '')
		grid[x_ax][ls[1]].configure(background = colour)
		grid[x_ax][ls[1]].configure(text = player)		
	return x_ax, ls[1]
	
#####################################################################################
## This function identifies and lists pits for each player.
###################################################################################3
def identify_pits(pos,pits):
	k = 0
	i = 0
	while k < 4:
		while i < 4:
			if i != k:
				pits[k].append(pos[i])
			i = i + 1
		i = 0
		k = k + 1
	return pits

#####################################################################################
## This function captire the route travveled by each player.
###################################################################################3
def capture_route(routes,init_pos):
	k = 0
	while k < 4:
		if init_pos[k] not in routes[k]:
			routes[k].append(init_pos[k])
		k = k + 1
	return routes

def convert_pits(player,pits):
	a = (pits[player-1][0][0])+(pits[player-1][0][1]*20)
	b = (pits[player-1][1][0])+(pits[player-1][1][1]*20)
	c = (pits[player-1][2][0])+(pits[player-1][2][1]*20)
	#d = (pits[player-1][3][0])+(pits[player-1][3][1]*20)
	#e = (pits[player-1][4][0])+(pits[player-1][4][1]*20)
	#f = (pits[player-1][5][0])+(pits[player-1][5][1]*20)
	#g = (pits[player-1][6][0])+(pits[player-1][6][1]*20)
	return [a,b,c]
	
def convert_position(player,init_pos):
	return init_pos[player-1][0]+(init_pos[player-1][1])*20
#####################################################################################
## Call back function when we press start button. process starts from here.
###################################################################################3#
def callback():
	if screen.poll :
		grid = initialize()
		global b
		b= 0
		payoff = [[],[],[],[],[]]
		
		while b == 0:
			pits = [[],[],[],[]]
			nash = []
			nash_action = []
			latest_pos = []
			sdc = [-1,-1,-1,-1]
			acts = [[],[],[],[]]
			player_actions = [[],[],[],[]]
			pits = identify_pits(init_pos,pits)
			delay()
			#routes = capture_route(routes,init_pos)
			#compute Payoff
	#####################################################################################
	## Caliculate the Nash Equillibirum.
	###################################################################################3#		
			i = 0
			while i < 4:
				best = 0
				move = 0
				print_move = ""
				nash = []
				dominent =[-1,-1,-1,-1,-1]
				if convert_position(i+1,init_pos) != 399:
					payoff[i] = valueiteration(convert_position(i+1,init_pos),convert_pits(i+1,pits))
					#print(payoff[i])
					#print(len(payoff[i]))
					acts[i].append(list(set(payoff[i])))
					player_actions[i] = acts[i][0]

				else :
					pits[i] = 0
				i = i + 1
			#	print("from marp:")		
			#print("Nash Equilibirum is: %s" %(nash_action))
			#print(player_actions)

			i = 0
			#while j < 3:
			while i < len(player_actions):
				#print(len(player_actions[i]))
				k = 0
				while ( k < len(player_actions[i])):
					move = player_actions[i][k]
					
					if move == 1:
						aadds = [init_pos[i][0],init_pos[i][1] + 1]
					elif move == 2:
						aadds = [init_pos[i][0],init_pos[i][1] - 1]
					elif move == 3:
						aadds = [init_pos[i][0]+1,init_pos[i][1]]
					elif move == 4:
						aadds = [init_pos[i][0]-1,init_pos[i][1]]
					else:
						aadds = [init_pos[i][0],init_pos[i][1]]
				
					if aadds not in latest_pos:
						latest_pos.append(aadds)
					else:
						player_actions[i].remove(move)
					k = k + 1
				i = i + 1
				#j = j + 1

			#print(player_actions)
			#print(latest_pos)

			i = 0
			while i < 4:
				
				if(len(player_actions[i]) == 1):
					move = player_actions[i][0]
				elif (len(player_actions[i]) == 2):
					move = player_actions[i][1]
				elif (len(player_actions[i]) == 3):
					move = player_actions[i][2]
				elif (len(player_actions[i]) == 4):
					move = player_actions[i][3]

				if move == 1:
					init_pos[i] = moveup(i+1,init_pos[i],grid)
					print_move = "Up"
				elif move == 2:
					init_pos[i] = movedown(i+1,init_pos[i],grid)
					print_move = "Down"
				elif move == 3:
					init_pos[i] = moveright(i+1,init_pos[i],grid)
					print_move = "Right"
				elif move == 4:
					init_pos[i] = moveleft(i+1,init_pos[i],grid)
					print_move = "Left"
				else:
					print_move = "Stay"
				
				nash_action.append(print_move)

				i = i + 1
			print("Nash Equilibirum is: %s" %(nash_action))

			if(not nash_action):
				b = 1
				break
			#print(numpy.array(payoff))
			screen.update()


		

		
#####################################################################################
## Program starts here...
###################################################################################3#
screen = tk.Tk()
screen.configure(background = "#85929e")
screen.minsize(940,900)
screen.title('Multi-agent Rendezvous problem solution using stochastic game algorithm')
screen.poll = True
stop = 0
#T = tk.Text(screen, height=1, width=100)
#T.pack()
#T.insert(tk.END, "				1-Blue, 2-Red, 3-Green, 4-Yellow, 5-Brown	")


print('Enter the intial locations of players: \n')
init_pos = [[],[],[],[]]
b = 0
k = 0
while k < 4:
	print("player %s"%(k+1))
	init_pos[k].append(input("x:"))
	init_pos[k].append(input("y:"))
	k=k+1

print(init_pos)

start_button = tk.Button(screen, text="Start", command=callback, height= 2, width= 10)
start_button.place(x = 300,y = 830)

reset_button = tk.Button(screen, text="Reset", command=resetenvironment, height= 2, width= 10)
reset_button.place(x = 500,y = 830)


grid = initialize()
#countgrid()

tk.mainloop()