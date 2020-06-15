import csv


fileName = input()
word_count = {} # count number of word occurences


with open(fileName, 'r') as csvfile: # read the file
   csvreader = csv.reader(csvfile)

   for row in csvreader: # iterates through each row
       for word in row: # analyzes words in each row
           if word not in word_count.keys():
               word_count[word] = 1
           else:
               word_count[word] += 1

for x in word_count.keys():
   print(x + " " + str(word_count[x]))
