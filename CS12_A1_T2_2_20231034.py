def input_list():
    my_list = []
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        element = int(input("Enter element " + str(i + 1) + " of the list: "))
        my_list.append(element)
    return my_list

def are_lists_equal(list1, list2):

    if len(list1) != len(list2):
        return False

    for item in list1:
        if item not in list2:
            return False

    for item in list2:
        if item not in list1:
            return False

    return True

def main():

    list1 = input_list()
    list2 = input_list()

    print("List 1:", list1)
    print("List 2:", list2)

    if are_lists_equal(list1, list2):
        print("lists = True")
    else:
        print("lists = False")

if __name__ == "__main__":
    main()
