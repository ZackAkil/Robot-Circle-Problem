def run(command, pos,mov):
	for l in command:
		if(l == 'R'):
			mov = turn(True,mov)
		elif(l == 'L'):
			mov = turn(False,mov)
		else:
			# print("lam", pos,mov)
			pos = map(lambda a,b: a+b, pos,mov)
			# print("lam", pos,mov)
	# print("position after one run",pos)
	return [pos,mov];

def turn(turnRight, mov):
	up = [0,1]
	down = [0,-1]
	right = [1,0]
	left = [-1,0]
	# t = mov
	if(turnRight):
		if(mov == up):
			mov = right
		elif(mov == right):
			mov = down
		elif(mov == down):
			mov = left
		elif(mov == left):
			mov = up
	else:
		if(mov == up):
			mov = left
		elif(mov == left):
			mov = down
		elif(mov == down):
			mov = right
		elif(mov == right):
			mov = up
	# print("turned","right" if turnRight else "left", t,"-->",mov)
	return mov

def isCirle(command):
	pos = [0,0]
	mov = [0,1]
	for i in range(4):
		[pos,mov] = run(command,pos,mov)
		if(pos == [0,0]):
			return "YES"
	return "NO"

print("Test case GGRLLGRL ",isCirle("GGRLLGRL"));
