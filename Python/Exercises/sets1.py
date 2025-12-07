def remove_duplicate(lst: list):
    '''
    You are given the following list with duplicates:

    Your tasks:
    Convert this list into a set to remove duplicates.
    Convert it back into a list.
    Sort the resulting list alphabetically.
    Print the final list
    '''

    converted_set = set(lst)

    converted_list = list(converted_set)
    sorted_lst = sorted(converted_list)
    print(sorted_lst)

if __name__ == "__main__":
    remove_duplicate(["apple", "banana", "apple", "orange", "banana", "kiwi"]
)