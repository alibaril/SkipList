# SkipList
A python skip list

To Run in terminal:
python SkipList.py 

Sample main test code:

#main function, opens 2cities.txt and calls sort function to sort
#file into two skip lists (one for capitals, and one for not)
def main():
  caps = SkipList()
  mins = SkipList()
  word = []
  with open('2cities.txt') as inputfile:
    for line in inputfile:
      word = line.split()
      for i in word:
        if i[0].isupper():
          caps.insert(i)
        else:
          mins.insert(i)

