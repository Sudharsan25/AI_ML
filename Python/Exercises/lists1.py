def list_tuple_exercise():
    '''
    Create a list of five numbers: 10, 20, 30, 40, 50.
    Then:
    Convert the list into a tuple.
    Access and print the third element of the tuple.
    Output expected: Just the value of the third element.
    '''

    lst = [10,20,30,40,50]

    tuple_list = tuple(lst)

    print(tuple_list)

    third_element = tuple_list[2]

    return third_element

if __name__ == "__main__":
    result = list_tuple_exercise()
    print("---------------------")
    print(result)
    print("---------------------")