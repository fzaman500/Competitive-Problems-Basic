def fib(n):
    first = 0
    second = 1
    if n > 1:
        for i in range(2, n + 1):
            result = first + second
            first = second
            second = result
        return second
    elif n == 1:
        return second
    elif n == 0:
        return first
    elif n < 0:
            return
for i in range(0, int(input())):
    n = int(input())
    computer = str(n)
    copies = fib(n)
    print("Inquiry #" + str(i + 1) + ": computer " + computer + " has " +  str(copies) + " copies")
