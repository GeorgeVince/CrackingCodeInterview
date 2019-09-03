def twoStrings(s1, s2):
	return "YES" if (bool(set(s1) & set(s2))) else "NO"


if __name__ == '__main__':
	print(twoStrings("z","worllhellold"))