###############################################################################################
## CSCI 8480 Project- Multi-agent Rendezvous problem solution using stochastic game algorithm #
## Program Name: paygen.py                                                                      #
## Written by: Mohan Ambati, Venkat Garlapati                                                 #
## Description: 	                                                                          #
## This program generates the payoffs needed for multi agent rendezvous problem using 
##	valueiteration method in markov decision process.
###############################################################################################
#####################################################################################
## Import statements
###################################################################################3#
import numpy as numpy
#####################################################################################
## Global variables
###################################################################################3#
rewards = [10]*400
action = [[0]*5]*400
table = []
payoffs = []
k = 0
#####################################################################################
## Initialize process that forms a table of actions possible for every position in grid.
###################################################################################3#
while k < 400:
	if (k-20) < 0 :
		if (k%20) == 0 :
			table.append([k,k+20,-20,k+1,-1])
		elif ((k+1)%20) == 0 :
			table.append([k,k+20,-20,-1,k-1])
		else :
			table.append([k,k+20,-20,k+1,k-1])
	elif (k+20) > 399:
		if (k%20) == 0 :
			table.append([k,-20,k-20,k+1,-1])
		elif ((k+1)%20) == 0 :
			table.append([k,-20,k-20,-1,k-1])
		else :
			table.append([k,-20,k-20,k+1,k-1])
	else :
		if (k%20) == 0 :
			table.append([k,k+20,k-20,k+1,-1])
		elif ((k+1)%20) == 0 :
			table.append([k,k+20,k-20,-1,k-1])
		else :
			table.append([k,k+20,k-20,k+1,k-1])
	k = k + 1

#####################################################################################
## This function generates the payoffs for a player
###################################################################################3#
def gen_payoffs(k,qvalues,action):
	if action == 0:
		return qvalues[k]
	elif action == 1:
		if (k+20) > 399:
			return -200
		else:
			return qvalues[k+20]
	elif action == 2:
		if (k-20) < 0:
			return -200
		else :
			return qvalues[k-20]
	elif action == 3:
		if ((k+1)%20) == 0:
			return -200
		else :
			return qvalues[k+1]
	elif action == 4:
		if (k%20) == 0:
			return -200
		else :
			return qvalues[k-1]
			

#####################################################################################
## This function is part of the value iteration, that caliculates maximum rewarded action.
###################################################################################3#
def caliculatemaxaction(qvalues,state):
	val = [-1]*5
	k = 0
	#print('state')
	#print(state)
	while k < 4:
		#print('table[state][k]')
		#print(qvalues[table[state][k]])
		if table[state][k] >= 0 and table[state][k] <= 399:
			val[k] = qvalues[table[state][k]] 
		k = k + 1
	#print('max_val')
	max_value = max(val)
	#print(max_value)
	max_index = val.index(max_value)
	return max_value
	
def compute_payoff(qvalues,pits,pos):
	counter = [0]*len(pits)
	total_qval = []
	actions = []
	row = []
	cpy_pits = pits
	'''if(len(pits) == 3):
		k = 0
		while k < 5:
			while counter[0] < 5 :
				while counter[1] < 5:
					while counter[2] < 5:
						#while counter[3] < 5:
						pits = cpy_pits
						y = 0
						while y < len(pits):
							if counter[y] == 0 :
								pits[y] = pits[y] 
							elif counter[y] == 1:
								pits[y] = pits[y] + 20
							elif counter[y] == 2:
								pits[y] = pits[y] - 20
							elif counter[y] == 3:
								pits[y] = pits[y] + 1
							elif counter[y] == 4:
								pits[y] = pits[y] - 1
							y = y + 1
						cvalues = []
						payoff_vals = []
						cvalues = qvalues
						if table[pos][k] >= 0 and table[pos][k] <= 399 :
							if table[pos][k] != 399:
								if table[pos][k] not in pits:
									cvalues[table[pos][k]] = qvalues[table[pos][k]] + 10
								else :
									cvalues[table[pos][k]] = qvalues[table[pos][k]] -500
							else :
								cvalues[table[pos][k]] = qvalues[table[pos][k]] + 200
						row.append(gen_payoffs(pos,cvalues,k))
								
							#counter[3] = counter[3] + 1
						#counter[3] = 0
						counter[2] = counter[2] + 1
					counter[2] = 0
					counter[1] = counter[1] + 1
				counter[1] = 0
				counter[0] = counter[0] + 1
			counter[0] = 0
			total_qval.append(row)
			row = []
			k = k + 1
'''
	if(len(pits) == 3):

		while counter[0] < 5 :
			while counter[1] < 5:
				while counter[2] < 5:
					pits = cpy_pits
					y = 0
					while y < len(pits):
						if counter[y] == 0 :
							pits[y] = pits[y] 
						elif counter[y] == 1:
							pits[y] = pits[y] + 20
						elif counter[y] == 2:
							pits[y] = pits[y] - 20
						elif counter[y] == 3:
							pits[y] = pits[y] + 1
						elif counter[y] == 4:
							pits[y] = pits[y] - 1
						y = y + 1
					cvalues = []
					cvalues = qvalues
					k = 0
					row = []
					while k < 5:
						if table[pos][k] >= 0 and table[pos][k] <= 399 :
							if table[pos][k] != 399:
								if table[pos][k] not in pits:
									cvalues[table[pos][k]] = qvalues[table[pos][k]] 
								else :
									cvalues[table[pos][k]] =qvalues[table[pos][k]]-1500
							else :
								cvalues[table[pos][k]] = qvalues[table[pos][k]] + 500
						row.append(gen_payoffs(pos,cvalues,k))
						k = k + 1

					total_qval.append(row)
					best = max(row)
					#print(best)
					move = row.index(best)
					actions.append(move)

					counter[2] = counter[2] + 1
				counter[2] = 0
				counter[1] = counter[1] + 1
			counter[1] = 0
			counter[0] = counter[0] + 1
		counter[0] = 0
		
		
	

	elif(len(pits) == 2):

		while counter[0] < 5 :
			while counter[1] < 5:
				pits = cpy_pits
				y = 0
				while y < len(pits):
					if counter[y] == 0 :
						pits[y] = pits[y] 
					elif counter[y] == 1:
						pits[y] = pits[y] + 20
					elif counter[y] == 2:
						pits[y] = pits[y] - 20
					elif counter[y] == 3:
						pits[y] = pits[y] + 1
					elif counter[y] == 4:
						pits[y] = pits[y] - 1
					y = y + 1
				cvalues = []
				cvalues = qvalues
				row = []
				k = 0
				while k < 5:
					if table[pos][k] >= 0 and table[pos][k] <= 399 :
						if table[pos][k] != 399:
							if table[pos][k] not in pits:
								cvalues[table[pos][k]] = qvalues[table[pos][k]] 
							else :
								cvalues[table[pos][k]] = qvalues[table[pos][k]]-1500
						else :
							cvalues[table[pos][k]] = qvalues[table[pos][k]] + 500
					row.append(gen_payoffs(pos,cvalues,k))
					k = k + 1

					total_qval.append(row)
					best = max(row)
					#print(best)
					move = row.index(best)
					actions.append(move)
			
				counter[1] = counter[1] + 1
			counter[1] = 0
			counter[0] = counter[0] + 1
		counter[0] = 0

		
			

	elif(len(pits) == 1):

		while counter[0] < 5 :
			pits = cpy_pits
			y = 0
			while y < len(pits):
				if counter[y] == 0 :
					pits[y] = pits[y] 
				elif counter[y] == 1:
					pits[y] = pits[y] + 20
				elif counter[y] == 2:
					pits[y] = pits[y] - 20
				elif counter[y] == 3:
					pits[y] = pits[y] + 1
				elif counter[y] == 4:
					pits[y] = pits[y] - 1
				y = y + 1
			cvalues = []
			cvalues = qvalues
			row = []
			k = 0
			row = []
			while k < 5:
				if table[pos][k] >= 0 and table[pos][k] <= 399 :
					if table[pos][k] != 399:
						if table[pos][k] not in pits:
							cvalues[table[pos][k]] = qvalues[table[pos][k]] 
						else :
							cvalues[table[pos][k]] = qvalues[table[pos][k]]-1500
					else :
						cvalues[table[pos][k]] = qvalues[table[pos][k]] + 500
				row.append(gen_payoffs(pos,cvalues,k))
				k = k + 1
				total_qval.append(row)
				best = max(row)
				#print(best)
				move = row.index(best)
				actions.append(move)
			counter[0] = counter[0] + 1
		counter[0] = 0

		
	
	elif(len(pits) == 0):

		pits = cpy_pits
		y = 0
		while y < len(pits):
			if counter[y] == 0 :
				pits[y] = pits[y] 
			elif counter[y] == 1:
				pits[y] = pits[y] + 20
			elif counter[y] == 2:
				pits[y] = pits[y] - 20
			elif counter[y] == 3:
				pits[y] = pits[y] + 1
			elif counter[y] == 4:
				pits[y] = pits[y] - 1
			y = y + 1
		cvalues = []
		cvalues = qvalues
		row = []
		k = 0
		while k < 5:
			if table[pos][k] >= 0 and table[pos][k] <= 399 :
				if table[pos][k] != 399:
					if table[pos][k] not in pits:
						cvalues[table[pos][k]] = qvalues[table[pos][k]] 
					else :
						cvalues[table[pos][k]] =qvalues[table[pos][k]] -1500
				else :
					cvalues[table[pos][k]] = qvalues[table[pos][k]] + 500
			row.append(gen_payoffs(pos,cvalues,k))
			k = k + 1
		total_qval.append(row)
		best = max(row)
		#print(best)
		move = row.index(best)
		actions.append(move)
		
		
	return actions	
		
	
#####################################################################################
## This function performs valueiteration on the grid asumming other players as pits.
###################################################################################3#
def valueiteration(pos,pits):
	qvalues = [0]*400
	stop = 0
	count = 0
	k = 0
	while stop != 1 :
		#print(qvalues)
		count = count + 1
		while k < 400:
			if k != 399:
				qvalues[k] = caliculatemaxaction(qvalues,k) + 1
			else :
				qvalues[k] = caliculatemaxaction(qvalues,k) + 1000
			k = k + 1									## end of reward function
		k = 0
		if count == 50 :
			stop = 1

	return(compute_payoff(qvalues,pits,pos))


#print(numpy.array(valueiteration(0,[])))
