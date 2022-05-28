# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

user_input1 = input("Enter first word: ")
user_input2 = input("Enter second word: ")

def find_anagram(word, anagram):
    # convert both the strings into lowercase
    word = user_input1.lower()
    anagram = user_input2.lower()

    # check if length is same
    if(len(word) == len(anagram)):
        # sort the strings
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)

        # if sorted char arrays are same
        if(sorted_word == sorted_anagram):
            print (True)
        else:
            print (False)

    else:
        print (False)

find_anagram("Deer", "Reed")