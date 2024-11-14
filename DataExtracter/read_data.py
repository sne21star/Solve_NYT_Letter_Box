import csv

def read_text(filename): 
    input_lines = []
    with open(filename, 'r') as file: 
        input_lines = [line.strip() for line in file]
    return input_lines

'''
Data is given in terms of string "ABC,DEF,GHI,JKL,WORD,WORD"
where the first 4 strings are the letters on the side of the box and the last to strings are the solution words
'''
def create_inputs(input_lines, number_of_sides): 
    letters_solutions = []
    for line in input_lines: 
        line = line.split(',')
        print(line)
        letters, solution = line[:number_of_sides], line[number_of_sides:]
        letters_solutions.append([letters, solution])
    return letters_solutions

'''
This will be assuming types csv
'''
def get_word_bank(filename):
    set_bank = set()
    with open(filename, mode ='r')as file:
        csvFile = csv.reader(file)
        #line = ['word', freq]
        for lines in csvFile:
            set_bank.add(lines[0])
    return set_bank

def get_data_examples(filename, number_of_sides): 
    input_lines = read_text(filename)
    return create_inputs(input_lines, number_of_sides)

