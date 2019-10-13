''' Built ins '''
# Enter your code here. Read input from STDIN. Print output to STDOUT

in_str = input().split()
n, x = int(in_str[0]), int(in_str[1])

res = []

for _ in range(x):
    l = list(map(float, input().split()))
    res.append(l)

for z in zip(*res):
    print(float(sum(z)) / x)

