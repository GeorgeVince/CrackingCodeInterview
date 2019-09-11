MAGIC_SQUARES = [[8, 1, 6, 3, 5, 7, 4, 9, 2],
				 [6, 1, 8, 7, 5, 3, 2, 9, 4],
				 [2, 7, 6, 9, 5, 1, 4, 3, 8],
				 [4, 3, 8, 9, 5, 1, 2, 7, 6],
				 [2, 9, 4, 7, 5, 3, 6, 1, 8],
				 [4, 9, 2, 3, 5, 7, 8, 1, 6],
				 [6, 7, 2, 1, 5, 9, 8, 3, 4],
				 [8, 3, 4, 1, 5, 9, 6, 7, 2]]


def formingMagicSquare(s):
	s_ = [i for row in s for i in row]
	totals = []
	for square in MAGIC_SQUARES:
		total = 0
		for i in range(0, len(s_)):
			total += abs(s_[i] - square[i])
		totals.append(total)
	
	return min(totals)

if __name__ == "__main__":
	print(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))