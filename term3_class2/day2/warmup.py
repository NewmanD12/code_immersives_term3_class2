import re

# 1)
# For a given sentence, return the average word length. Note: Remember to remove punctuation first.
sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"
# Output

# 4.2
# 4.08

import re

def find_average_word_len(sentence= 'Hello'):
    sentence = re.sub(r'[^\w\s]', ' ', sentence)
    split_sentence = sentence.split()
    print(split_sentence)
    lengths_of_words = []
    for i in split_sentence:
        lengths_of_words.append(len(i))

    avg = round(sum(lengths_of_words) / len(lengths_of_words), 1)
    return avg

#######################################################

# 2)
# Given an array of integers, determine whether the array is monotonic or not.
A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]
# Output:
# True
# False
# True    

def is_monotonic(lst):
	if sorted(lst) == lst or sorted(lst, reverse=True) == lst:
		return True
	return False

def create_g(num):
    half_point = round(num / 2) - 1
    for i in range(num):
        if i == half_point:
            print('*' + ' ' * half_point + '***')
        if i == 0 or i == num - 1:
            print(' ' + '*' * (half_point + 2) + ' ')
        elif i < half_point:
            print('*')
        elif i > half_point:
            print('*' + ' ' * (half_point+2) + '*')



if __name__ == '__main__':
    create_g(7)
    # create_g(9)
    # create_g(11)

