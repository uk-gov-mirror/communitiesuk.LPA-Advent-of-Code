import re

with open('input_jac.txt') as f:
    data = f.read()
    
negatives = sum([int(n) for n in re.findall('-[0-9]+', data)])
positives = sum([int(n) for n in re.findall('[^-|0-9]([0-9]+)', data)])
pt1 = negatives + positives
print(pt1)

red_indexes = [match.start() for match in re.finditer(':"red"', data)]
open_indexes = []
close_indexes = []
for i in red_indexes:
    j = i
    opened_brackets = 0
    closed_brackets = 0
    while opened_brackets - closed_brackets != 1:
        j -= 1
        # print(f'{opened_brackets=}, {closed_brackets=}')
        if data[j] == "}":
            closed_brackets += 1
        elif data[j] == "{":
            opened_brackets += 1
    open_indexes.append(j)
    j = i
    opened_brackets = 0
    closed_brackets = 0
    while closed_brackets - opened_brackets != 1:
        j += 1
        if data[j] == "}":
            closed_brackets += 1
        elif data[j] == "{":
            opened_brackets += 1
    close_indexes.append(j)
    
ignored = sorted(set([(start, end) for start, end in zip(open_indexes, close_indexes)]))
ignored_no_repeats = []
for i, (start_i, end_i) in enumerate(ignored):
    subset = False
    for j, (start_j, end_j) in enumerate(ignored):
        if i != j:
            start_gt = start_i > start_j
            end_lt = end_i < end_j
            if start_gt and end_lt:
                subset = True
    if not subset:
        ignored_no_repeats.append((start_i, end_i))
         
for start, end in ignored_no_repeats:
    negatives = sum([int(n) for n in re.findall('-[0-9]+', data[start:end])])
    positives = sum([int(n) for n in re.findall('[^-|0-9]([0-9]+)', data[start:end])])
    total = negatives + positives
    pt1 -= total
   
print(pt1)

        

  