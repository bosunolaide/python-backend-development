import string

# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

filename = input("Please input filename: ")

def read_file_content(filename):
    # Open text file in read mode
    text_file = open(filename, "r")
 
    # Read whole file to a string
    data = text_file.read()
 
    # Close file
    text_file.close()
 
    return data


def count_words():
    # Read text file
    text = read_file_content(filename)

    # Remove all punctuations from text
    new_text = text.translate(str.maketrans('', '', string.punctuation))

    # Convert text to lowercase to avoid case mismatch
    lower_case_text = new_text.lower()

    # Split text into words, and add to iterable list
    text_words = lower_case_text.split()

    # Create an empty dictionary
    count = {}

    # Iterate over each word in the list
    for word in text_words:
        # Check if the word is already in dictionary
        if word in count:
            # Increment count of word by 1
            count[word] +=1
        else:
            # Add the word to dictionary with count 1
            count[word] = 1
    return count

# Print the contents of dictionary
print(count_words())