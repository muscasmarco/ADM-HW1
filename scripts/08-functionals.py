cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
        
    l = [0, 1]
    prev_n, curr_n = 0, 1

    for i in range(n-2):
        ind = i + 2
        l.append(prev_n + curr_n)
        prev_n = l[ind-1]
        curr_n = l[ind]

    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
