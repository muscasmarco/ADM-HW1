
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


