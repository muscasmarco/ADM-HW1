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
            
