
def minimumBribes(q):
	initial_pos = {x:q.index(x) for x in q}
	print(initial_pos)

if __name__ == "__main__":
	q = [2, 1, 5, 3, 4]
	print (minimumBribes(q))