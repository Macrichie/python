>>> def fib(end):
	previous, next = 0, 1
	fibList = []
	while next < end:
		fibList.append(next)
		previous, next = next, next + previous
	return fibList

>>> fib(20)
[1, 1, 2, 3, 5, 8, 13]
>>> fib(10)
[1, 1, 2, 3, 5, 8]
>>> fib(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fib(200)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
>>> fib(2000)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
>>> fib(20000)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
