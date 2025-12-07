def word_count_dictionary(sentance: str):
    '''
    Docstring for word_count_dictionary
    :param lst: Description
    :type lst: list

    Your tasks:
    Split the sentence into words.
    Create a dictionary that counts how many times each word appears.
    Print the dictionary sorted by frequency (highest first).
    Sorting can be done however you prefer (list of tuples, sorted dict, etc.)
    '''

    words = sentance.split()

    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] = 1

    print(sorted(word_dict.items(), key=lambda x:x[1], reverse=True))

if __name__ == "__main__":
    word_count_dictionary("the quick brown fox jumps over the lazy dog the fox is quick")
