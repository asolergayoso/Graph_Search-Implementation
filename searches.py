#!/usr/bin/python
import sys

nodesDic = {}
explored = []
stack = []
queue = []


class Link:
	def __init__ (self, N2, cost):
		#self.N1 = N1
		self.N2 = N2
		self.cost = cost

class Node:
	def __init__ (self, name):
		self.name = name
		self.heur_cost = 0
		self.links = []

class Path:
	def __init__ (self):
		self.path = []
		self.cost = 0


def output_print(input):
	print "  " + explored[len(explored) - 1].name + "      " + "[",
	for row in stack:
		if (input == 0):
			print "<",
		elif (input == 1):
			print str(row[0].heur_cost) + "<",
		elif (input == 2):
			sm = row.cost + row.path[0].heur_cost
			print str(sm) + "<",
		for n in row:
			print n.name,
		print ">",
	print "]"



def hill_climb(current_path):

	current_node = current_path[0]
	explored.append(current_node)

	output_print(1)

	if (current_node == nodesDic['G']):
		print "Goal reached!"
		return True
	else:
		costs = []
		if not current_node.links:
			print "Goal not reached"
			return False

		for l in current_node.links:
			if l.N2 not in current_path:
				costs.append(l.N2.heur_cost)

		tempVal = min(costs)

		#for i in costs:
		path = []
		for p in current_node.links:
			if tempVal == p.N2.heur_cost:
				path.append(p.N2)
				path.extend(current_path)
		stack.pop(0)
		stack.append(path)
		hill_climb(stack[0])



def greedy (current_path):

	current_node = current_path[0]
	explored.append(current_node)

	output_print(1)

	if (current_node == nodesDic['G']):
		print "Goal reached!"
		return True
	else: 
		costs = []
		for l in current_node.links:
			if l.N2 not in explored:
				costs.append(l.N2.heur_cost)			
		costs.sort()
		stack.pop(0)
		for i in reversed(costs):
			path = []
			for p in current_node.links:
				if i == p.N2.heur_cost:
					path.append(p.N2)
					path.extend(current_path)
			stack.insert(0, path)
		greedy(stack[0])	



def dfs (current_path): #current_node

	current_node = current_path[0]
	explored.append(current_node)  #current_node

	output_print(0)

	if (current_node == nodesDic['G']):
		print "Goal reached!"
		return True
	else: 
		letters = []
		for l in current_node.links:
			if l.N2 not in current_path:
				letters.append(l.N2.name)			
		letters.sort()
		stack.pop(0)
		for i in reversed(letters):
			path = []
			for p in current_node.links:
				if i == p.N2.name:
					path.append(p.N2)
					path.extend(current_path)
			stack.insert(0, path)
		dfs(stack[0])




def bfs (current_path): #current_node

	current_node = current_path[0]
	explored.append(current_node)  #current_node

	output_print(0)

	if (current_node == nodesDic['G']):
		print "Goal reached!"
		return True
	else:
		letters = []
		for l in current_node.links:
			if l.N2 not in current_path:
				letters.append(l.N2.name)
		letters.sort()
		stack.pop(0)
		for i in letters:
			path = []
			for p in current_node.links:
				if i == p.N2.name:
					path.append(p.N2)
					path.extend(current_path)
			stack.append(path)
		bfs(stack[0])

def beam (current_path):

	current_node = current_path[0]
	explored.append(current_node)

	output_print(1)

	if (current_node == nodesDic['G']):
		print "Goal reached!"
		return True
	else:
		costs = []
		for l in current_node.links:
			if l.N2 not in current_path:# and l.N2 not in stack:
				costs.append(l.N2.heur_cost)
				#stack.append(l.N2)
		costs.sort()
		stack.pop(0)
		for i in costs:
			path = []
			for p in current_node.links:
				if i == p.N2.heur_cost:
					path.append(p.N2)
					path.extend(current_path)
			stack.append(path)
		#if len(current_path) == len(stack):
			#stack.sort(key = lambda x:x.heur_cost)
			#stack.pop(0)
		#	stack = stack[:2]
		#	print stack
		beam(stack[0])


def dls(current_path, cnt):  # current_node

	current_node = current_path[0]
	explored.append(current_node)  # current_node

	output_print(0)

	if (len(current_path) >= cnt):
		stack.pop(0)
		if not stack:
			print "Depth reached!"
			return False
	else:
		if (current_node == nodesDic['G']):
			print "Goal reached!"
			return True
		else:
			letters = []
			for l in current_node.links:
				if l.N2 not in current_path:
					letters.append(l.N2.name)
			letters.sort()
			stack.pop(0)
			for i in reversed(letters):
				path = []
				for p in current_node.links:
					if i == p.N2.name:
						path.append(p.N2)
						path.extend(current_path)
				stack.insert(0, path)
	dls(stack[0], cnt)


def ids(current_path, cnt):

	if (dls(current_path, cnt)):
		quit()
	else:
		cnt = cnt + 1
		global stack
		stack = [[nodesDic['S']]]
		current_path = []
		current_path.append(nodesDic['S'])
		ids (current_path, cnt)


def ucost (current_path):

	current_node = current_path.path[0]
	explored.append(current_node)

	#cat = sorted(stack, key=lambda x: x.cost)
	print "  " + explored[len(explored) - 1].name + "      " + "[",
	for row in stack:
		sm = row.cost
		print str(sm) + "<",
		for l in row.path:
			print l.name,
		print ">",
	print "]"

	if (current_node == nodesDic['G']):
		print "Goal reached!"
		return True
	else:
		cost = current_path.cost
		total_costs = []
		for l in current_node.links:
			if l.N2 not in current_path.path:
				tc = l.cost + cost
				total_costs.append((l.N2.name,tc))
		stack.pop(0)
		total_costs.sort()
		for i in reversed(total_costs):
			path = []
			a = Path()
			for p in current_node.links:
				if i[1] == (p.cost + cost) and i[0] == p.N2.name:
					path.append(p.N2)
					path.extend(current_path.path)
					a.path = path
					a.cost = p.cost + cost
					stack.insert(0, a)

		#stack.sort(key = attrgetter('cost'))
		stack.sort(key = lambda x: (x.cost,x.path[0].name))
		ucost(stack[0])


def astar (current_path):

	current_node = current_path.path[0]
	explored.append(current_node)

	cat = sorted(stack, key=lambda x: x.cost)
	print "  " + explored[len(explored) - 1].name + "      " + "[",
	for row in stack:
		sm = row.cost + row.path[0].heur_cost
		print str(sm) + "<",
		for l in row.path:
			print l.name,
		print ">",
	print "]"

	if (current_node == nodesDic['G']):
		print "Goal reached!"
		return True
	else:
		cost = current_path.cost
		total_costs = []
		for l in current_node.links:
			if l.N2 not in current_path.path:
				tc = l.N2.heur_cost + l.cost + cost
				total_costs.append(( tc))
		stack.pop(0)
		total_costs.sort()
		for i in reversed(total_costs):
			path = []
			a = Path()
			for p in current_node.links:
				if i == (p.N2.heur_cost + p.cost + cost): #and i[0] == p.N2.name:
					path.append(p.N2)
					path.extend(current_path.path)
					a.path = path
					a.cost = p.cost + cost
					stack.insert(0, a)
		for m in stack:
			for n in stack:
				if n.path[0] == m.path[0]:
					if n.cost > m.cost:
						stack.remove(n)
					elif n.cost < m.cost:
						stack.remove(m)

		#stack.sort(key = lambda x: (x.cost,x.path[0].name))

		astar(stack[0])











def main():		

	flag = 0
	f =  sys.argv[1]
	file = open(f, "r")
	count = 0

	for line in file:
		wordlist = line.split()   #splits line into words
		if '#####' in wordlist:       #to detect the heuristic costs list
			flag = 1
		else:
			if flag == 0:
				if wordlist[0] not in nodesDic:
					nodesDic[wordlist[0]] = Node(wordlist[0])
				if wordlist[1] not in nodesDic:
					nodesDic[wordlist[1]] = Node(wordlist[1])
				a = Link(nodesDic[wordlist[1]], float(wordlist[2]))
				b = Link(nodesDic[wordlist[0]], float(wordlist[2]))

				nodesDic[wordlist[0]].links.append(a)
				nodesDic[wordlist[1]].links.append(b)
	
				for i in nodesDic:
					nodesDic[i].links.sort()
			else:
				nodesDic[wordlist[0]].heur_cost = float(wordlist[1])

	nodesDic['G'].heur_cost = 0
	root = []
	root.append(nodesDic['S'])





	print ""
	print "************* Please, select an algorithm **************"
	print "1. Depth First Search"
	print "2. Breath First Search"
	print "3. Depth-limited Search"
	print "4. Iterative Deepening Search"
	print "5. Uniform Search"
	print "6. Greedy Search"
	print "7. A*"
	print "8. Beam Search"
	print "9. Hill-Climbing Search"
	print ""
	choice = input("Your choice:")
	print ""

	
	if (choice == 1):
		print "Depth First Search"
		print "Expanded" + " " + "Queue"
		stack.append(root)
		dfs(root)  #root
	elif (choice == 2):
		print "Breath First Search"
		print "Expanded" + " " + "Queue"
		#queue.append(root)
		stack.append(root)
		bfs(root)
	elif (choice == 3):
		num = int(input("Please enter limit: "))
		print "Depth-Limited Search, L = " + str(num)
		print "Expanded" + " " + "Queue"
		cnt = num + 1
		stack.append(root)
		dls(root, cnt)
	elif (choice == 4)	:
		print "Iterative Deepening Search"
		print "Expanded" + " " + "Queue"
		stack.append(root)
		ids(root, 0)
	elif (choice == 5)	:
		print "Uniform Cost Search"
		print "Expanded" + " " + "Queue"
		a = Path()
		a.path.append(nodesDic['S'])
		stack.append(a)
		ucost(a)
	elif (choice == 6):
		print "Greedy Search"
		print "Expanded" + " " + "Queue"
		stack.append(root)
		greedy(root)
	elif (choice == 7):
		print "A* Search"
		print "Expanded" + " " + "Queue"
		a = Path()
		a.path.append(nodesDic['S'])
		stack.append(a)
		astar(a)
	elif (choice == 8):
		print "Beam Search"
		print "Expanded" + " " + "Queue"
		stack.append(root)
		beam(root)
	elif (choice == 9):
		print "Hill-Climbing Search"
		print "Expanded" + " " + "Queue"
		stack.append(root)
		hill_climb(root)

	#for n in explored:
	#	print n.name
	
if __name__ == "__main__": main()
