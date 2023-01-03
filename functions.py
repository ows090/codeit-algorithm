def hello_world():
	print("hello world")


def consecutive_sum(start, end):
	if start == end:
		return start
	median = (start + end) // 2
	return consecutive_sum(start, median) + consecutive_sum(median + 1, end)
