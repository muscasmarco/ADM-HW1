
''' Introduction '''
#Say "Hello, World!" With Python
print("Hello, World!")

# Python If-Else 

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n >= 1 and n <= 100:    
        if n % 2 != 0:
            print("Weird")
        else:
            if (n >= 2 and n <= 5) or (n > 20):
                print("Not Weird")
            else:
                print("Weird")

# Arithmetic Operators 

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)

#Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)

# Loops

if __name__ == '__main__':
    n = int(input())

    if n >= 0 and n <= 20:
        for n in range(0, n):
            print(n**2)

# Write a function

def is_leap(year):
    leap = False
    
    # Write your logic here

    if year >= 1900 and year <= 10**5:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                leap = False
            else:
                leap = True

    return leap

# Print function

if __name__ == '__main__':
    n = int(input())

def count_digits(num):
    
    if num < 10:
        return 1
    else:
        return 1 + count_digits(num/10)
    

max_exp = 0
for i in range(1,n+1):
    num_digits = count_digits(i)
    max_exp += num_digits


''' Basic data types ''' 

# List comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list_comp = [[i,j,k] for i in range(0, x+1) for j in range(0,y+1) for k in range(0, z+1) if ((i+j+k) != n)]

    print(list_comp)

# Find the runner-up score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    score_list = list()

    if n >= 2 and n <= 10:
        tmp_score_list = list(arr)
        score_list = (entry for entry in tmp_score_list if (entry < max(tmp_score_list)))
        print(max(score_list))

# Nested lists
if __name__ == '__main__':
    student_grades = []
    # Pre compute the minimum grade
    min_grade = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if(len(student_grades) == 0):
            min_grade = score
        else: 
            if score <= min_grade:
                min_grade = score

        student_grades.append([name, score]) # Add to list

    removed_worst_students = [entry for entry in student_grades if entry[1] != min_grade]
    second_lowest_grade = min([entry[1] for entry in removed_worst_students])
    second_lowest_grade_students = [entry[0] for entry in removed_worst_students if entry[1] == second_lowest_grade]
    

    second_lowest_grade_students.sort()
    
    for student_name in second_lowest_grade_students:
        print(student_name)

# Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Get average
    avg_score = float(sum(student_marks[query_name])/len(student_marks[query_name]))
    # Trim string or extend
    avg_score_as_str = str(avg_score)
    
    # Split the string to separate the decimal digits from the rest
    int_str, sep, dec_str = avg_score_as_str.partition('.')
    
    int_str = str(int_str)
    sep = str(sep)
    dec_str = str(dec_str)
    
    if len(dec_str) > 2: # Has more than 2 decimal digits, get the first 2 chars ([0], [1])
        dec_str = dec_str[:2]
    if len(dec_str) == 1: # Number is like k.0 : just add a trailing 0
        dec_str = dec_str + '0'
    
    avg_score_as_str =  int_str+sep+dec_str # Reassemble the string
    print(avg_score_as_str)


# Lists
if __name__ == '__main__':
    N = int(input())
    op_list = []

    for _ in range(N):
        command_name, *values = input().split()            

        if command_name == 'insert':
            at_index = int(values[0])
            value = int(values[1])
            op_list.insert(at_index, value)
            
        if command_name == 'print':
            print(op_list)
        
        if command_name == 'remove':
            op_list.remove(int(values[0]))

        if command_name == 'append':
            op_list.append(int(values[0]))

        if command_name == 'sort':
            op_list.sort()
        
        if command_name == 'pop':
            op_list.pop()

        if command_name == 'reverse':
            op_list.reverse()

#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = tuple((x for x in integer_list))
    print(t.__hash__())


''' Strings '''
#sWAP cASE
def swap_case(s):
    s = str(s).swapcase()
    return s

# Capitalize!
def split_and_join(line):
    # write your code here
    #line = str(line)
    line = '-'.join(line.split(' '))
    return line

# What's your name?
def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." % (a, b))

# Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string
# Find a string 
def count_substring(string, sub_string):
    num_occurrences = 0
    string = str(string)
    for _ in range(len(string)):
        index_substr = string.find(sub_string)
        if(index_substr != -1):
            string = string[index_substr+1:]
            num_occurrences += 1

    return num_occurrences

# String Validators
if __name__ == '__main__':
    s = input()
    s = str(s)

    has_alphanum = False
    has_alpha = False
    has_digits = False
    has_lower = False
    has_upper = False

    
    for char in s:
        if str(char).isalnum():
            has_alphanum = True
        if str(char).isalpha():
            has_alpha = True
        if str(char).isdigit():
            has_digits = True
        if str(char).islower():
            has_lower = True
        if str(char).isupper():
            has_upper = True

    print(has_alphanum)
    print(has_alpha)
    print(has_digits)
    print(has_lower)
    print(has_upper)

#Text Alignment
	#Replace all ______ with rjust, ljust or center. 

	thickness = int(input()) #This must be an odd number
	c = 'H'

	#Top Cone
	for i in range(thickness):
	    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

	#Top Pillars
	for i in range(thickness+1):
	    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

	#Middle Belt
	for i in range((thickness+1)//2):
	    print((c*thickness*5).center(thickness*6))    

	#Bottom Pillars
	for i in range(thickness+1):
	    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

	#Bottom Cone
	for i in range(thickness):
	    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text wrap
def wrap(string, max_width):
    wrap_string = ""
    tokens = textwrap.wrap(string, max_width)
    for line in tokens:
        wrap_string = wrap_string + line + "\n"

    return wrap_string
    

# Designer Door Mat
	# Enter your code here. Read input from STDIN. Print output to STDOUT
	n, m = map(int, input().split())

	dash = '-'
	dec = '.|.' # Decoration

	welcome_line = dash*(m // 2 - len('welcome')//2) + 'WELCOME' + dash*(m // 2 - len('welcome')//2)

	row_l = list()

	for row_i in range(n // 2):
	    dec_str = dec * (row_i * 2 + 1)
	    dash_str = dash * (m // 2 - (len(dec_str)//2))
	    row_str = dash_str + dec_str + dash_str
	    row_l.extend([row_str])
	    print(row_str)

	print(welcome_line)

	row_l.reverse()

	for row in row_l:
	    print(row)

# String Formatting
def print_formatted(number):
    # your code goes here

    # Must remove prefixes
    max_space = len(str(bin(number))[2:])
    s= ' ' #Space character
    for num in range(1, number+1):
        dec = str(num)
        octal = str(oct(num))[2:]
        hexa = (str(hex(num)).upper())[2:]
        binary = str(bin(num))[2:]

        dec_s = max_space - len(dec)
        oct_s = max_space - len(octal) + 1
        hexa_s = max_space - len(hexa) + 1
        binary_s = max_space - len(binary) + 1

        string = s * dec_s + dec + s * oct_s + octal + s * hexa_s + hexa + s * binary_s + binary
        print(string)

#Alphabet Rangoli
def get_letter(num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet[num]

def gen_row(start, end):
    if start == end:
        return get_letter(end)
    else:
        return get_letter(end) + '-' + gen_row(start, end-1) + '-' + get_letter(end)

def print_rangoli(size):
    size -= 1
    dash = '-'
    n_cols = len(gen_row(0, size))
    bottom = ''

    for i in range(size + 1):
        centr_str = gen_row(size-i, size)
        dash_str = ((n_cols - len(centr_str))//2) * dash
        print(dash_str + centr_str + dash_str)
        if i != size:
            bottom =  dash_str + centr_str + dash_str + '\n' + bottom
            
    print(bottom)

# The Minion Game
def minion_game(string):
    # stuart starts with consonants 
    # kevin with vowel
    kevin_sl = ""

    # Build first letters list
    i = 0

    while(i < len(string)):
        l = string[i]
        if (l in ['A','E','I','O','U'] 
            and l not in kevin_sl):
            kevin_sl += l
        if len(kevin_sl) == 5:
            break

        ''' Not needed
        else:
            if (l not in stuart_sl
                and l not in ['A','E','I','O','U']): 
                    stuart_sl += l

        if len(stuart_sl) == 5 and len(stuart_sl) == 21:
            keep_building = False
        '''
        i += 1

    stuart_score, kevin_score = 0, 0

# As I clicked in the discussions board for this excercise I found the solution to make all the tests pass.
# Before that, some tests were not passed due to performance issues (non-optimized code).
    for i in range(len(string)):
        if string[i] in kevin_sl:
            kevin_score += len(string) - i
        else: # This means that the found letter is a consonant, which must be in the word, therefore in stuart's letters
            stuart_score += (len(string) - i)
    
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        if kevin_score > stuart_score:
            print("Kevin", kevin_score)
        else:
            print("Draw")
            
    

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


''' Date and Time '''

# Calendar Module

import calendar

s = input().split()

month = int(s[0])
day = int(s[1])
year = int(s[2])

week_i = calendar.weekday(year, month, day)
day = str(calendar.day_name[week_i])
print(day.upper())


#Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
import datetime
import calendar

def get_utc_timestamp(t1):
    tokens = t1.split()
    year = int(tokens[3])
    month = list(calendar.month_abbr).index(tokens[2])
    day = int(tokens[1])

    timestamp = tokens[4].split(':')
    hours = int(timestamp[0])
    minutes = int(timestamp[1])
    seconds = int(timestamp[2])

    a = datetime.datetime(year, month, day, hours, minutes, seconds, 0)
    
    tz = tokens[5]
    sign = tz[0]
    h_tz = int(tz[1]+tz[2])
    m_tz = int(tz[3]+tz[4])

    conversion_fact = h_tz * 3600 + m_tz * 60
    if sign == '+':
        conversion_fact *= -1


    return a.timestamp() + conversion_fact

def time_delta(t1, t2):
    t1_ts = get_utc_timestamp(t1)
    t2_ts = get_utc_timestamp(t2)

    delta = abs(t1_ts - t2_ts)
    return str('%d' % delta)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


''' Exceptions '''

t = int(input())

for _ in range(t):
    req = input().split()
    

    try:
        a = int(req[0])

        try:
            b = int(req[1])

            if b == 0:
                print('Error Code: integer division or modulo by zero')
            else: 
                print(a // b)
        
        except:
            print("Error Code: invalid literal for int() with base 10: '%s'" % req[1])
        
        
    except:
        print("Error Code: invalid literal for int() with base 10: '%s'" % req[0])

    
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

''' Python functionals '''
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

''' Problem 2 '''

# Birthday Cake Candles

def birthdayCakeCandles(ar):

    count = 0
    max_height = max(ar)
    for i in range(len(ar)):
        if ar[i] == max_height:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# kangaroo

def kangaroo(x1, v1, x2, v2):
    x1, v1, x2, v2 = float(x1), float(v1), float(x2), float(v2)

    if v2 == v1 and x1 != x2:
        return 'NO'
    if v2 == v1 and x1 == x2:
        return 'YES'
        
    int_part = (x1 - x2)//(v2 - v1)

    if (x1 - x2)/(v2 - v1) < 0.0:
        return 'NO'

    if ((x1 - x2)/(v2 - v1) - float(int_part)) == 0.0:
        return 'YES'

    return 'NO'


# recursive digit sum

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    
    if k != 0:
        s = sum(map(int, list(n)))
        s *= k
        k = 0
        return superDigit(str(s), 0)

    s = sum(map(int, list(n)))
    if len(str(s)) > 1:
        return superDigit(str(s), 0)
    else:
        return sum(map(int, list(n)))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()










































