# test is as follows:
# sort the characters in the following string:

# abcdefghijklmnopqrstuvwxyz_

# by the number of times the character appears in the following text (descending):

# Note: the text scrolls.

# so the best option take the characters and add them to a text file, and get python to do the rest. 

letters = {}
word=[]

def parse_text():
    with open('textfile.txt', 'r') as f:
        for line in f:
            char_list= list(line.strip('\n')) 
            for char in char_list: 
                if not char in letters:
                    letters[char]=1
                else:
                    letters[char]+=1

def print_word():
    print "sorted letters:\n"
    for char in sorted(letters, key=letters.get, reverse=True):
        print(char, letters[char])
        if(char != '_'):
            word.append(char)
        else:
           result = ''.join(word)
           continue 

    print "\nThe word I am looking for is: \n"+result

parse_text()
print_word()
