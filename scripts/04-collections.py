''' Collections '''

# collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
num_shoes = int(input())
shoes = [int(x) for x in input().split()]
num_customers = int(input())
total = 0

counter = Counter(shoes)


for i in range(num_customers):
    shoe_info = input().split()
    shoe_size = int(shoe_info[0])
    shoe_price = int(float(shoe_info[1]))
    
    if shoe_size in counter.keys() and counter[shoe_size] > 0:
        total += shoe_price
        counter[shoe_size] -= 1

print(total)

#Collections.namedtuple()
from collections import namedtuple

n = int(input())
cols = input()

Student = namedtuple('Student', cols)

tot = 0

for _ in range(n):
    row = input().split()
    student = Student(row[0], row[1], row[2], row[3])

    tot += float(student.MARKS)

avg = tot / float(n)




print('%.2f' % avg)

#Collections.OrderedDict()
from collections import OrderedDict

n = int(input())

ordered_dict = OrderedDict()

for _ in range(n):
    elements = input().split()
    str_elements = elements[:(len(elements)-1)]
    prod_name = ' '.join(str_elements)
    prod_net_price = int(elements[-1])

    if prod_name not in ordered_dict.keys():
        ordered_dict[prod_name] = prod_net_price
    else:
        ordered_dict[prod_name] += prod_net_price

[print('%s %d' %(k, ordered_dict[k])) for k in ordered_dict.keys()]

#Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())

od = OrderedDict()

for _ in range(n):
    word = input()

    if word not in od.keys():
        od[word] = 1
    else: 
        od[word] += 1
    

print(len(od.keys()))
list_occ = [od[key] for key in od.keys()]
occ_str = ''

for k in od.keys():
    occ_str += str(od[k])
    occ_str += ' '

print(occ_str)

#Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()

for _ in range(n):
    comm_args = input().split()

    command = comm_args[0]

    if command == 'append':
        num = int(comm_args[1])
        d.append(num)

    if command == 'appendleft':
        num = int(comm_args[1])
        d.appendleft(num)
    
    if command == 'pop':
        d.pop()
    
    if command == 'popleft':
        d.popleft()

s = ' '.join([str(e) for e in d])
print(s)
