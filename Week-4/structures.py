'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''
import string
# Lists

# write a function that returns a list containing the first and the last element
# of "the_list". 
def first_and_last(the_list):
    ''' returns a list containing the first and lasts elements of a given list, the_list'''
    first = the_list[0]
    last = the_list[-1]
    new_list = []
    new_list.append(first) #function that adds variables to the end of the list
    new_list.append(last)
    print(new_list)
    return new_list



# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    if beginning >= end or end >= len(the_list) or beginning < 0:
        raise ValueError
    else:
        new_list = the_list[beginning:end] #the new_list is the part of the_list from beginning to one before the end
        new_list.reverse() #calls the function to reverse new_list
        return new_list


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    new_list = the_list[0: index+1] + [the_list[index]] + the_list[index: len(the_list)]
    print(new_list)
    return new_list
    

# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    if word[::-1] == word: # word[::-1] means the word read backwards
        print("palindrome!!!")
    else:
        print("not a palindrome")
    return


# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    new_sentence = sentence.replace("!", "").replace(",", "").replace(" ", "").lower()
    #new_sentence = sentence.replace(string.punctuation, "")
    print(new_sentence)
    checking = palindrome_word(new_sentence)
    
    # if new_sentence[::-1] == new_sentence:
    #         print("palindrome")
    # else:
    #         print("not a palindrome")
    return checking

#palindrome_sentence("han ,Nah")

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and there must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2):
    # sentence1[0] = sentence1[0].upper()
    sentence1 = sentence1.strip().capitalize()
   
    # if sentence1[-1] or sentence2[-1] != "." or "!" or "?":
    #     print("invalid sentence")
    
    # sentence1 = sentence1 + " "
    if sentence1[-1] or sentence2[-1] != "." or "!" or "?":
        print("invalid sentence")
    sentence1 = sentence1 + " "
    new_sentence = sentence1 + sentence2
    print(new_sentence)
    return

#concatenate_sentences("   hello!  ", "Leilaa.") #doesn't work if there are multiple whitespaces...and it says sentence1 is undefined'''


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary:
        print(True)
        return True
        
    else:
        print(False)
        return False 


# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False


dictionary = {"brand": "Ford", "model": "Mustang", "year": 1964}

value_exists(dictionary, 1964)


# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    dictionary1.update(dictionary2)
    return(dictionary1)

