def list_operations():
    List = []
    while True:
        print("\nList Operations: ")
        print("1.Insert")
        print("2.Update")
        print("3.Delete")
        print("4.Display")
        print("5.Search")
        print("6.Sort")
        print("7.Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = input("Enter an element to insert: ")
            List.append(element)
        elif choice == 2:
            index = int(input("Enter the index of the element to be updated: "))
            element = input("Enter new element: ")
            if 0 <= index <len(List):
                List[index] = element
            else:
                print("Index out of range: ")
        elif choice == 3:
            element = input("Enter the element to be deleted: ")
            if element in List:
                List.remove(element)
                print("Element deleted!!")
            else:
                print("Element not found")
        elif choice == 4:
            print("List: ", List)
        elif choice == 5:
            element = input("Enter the element to be searched: ")
            if element in List:
                print("Element found at index: ", List.index(element))
            else:
                print("Element not found")
        elif choice == 6:
            List.sort()
            print("Sorted list: ", List)
        elif choice == 7:
            break
        else:
            print("Invalid choice...Please try again")
            
def tuple_operations():
    tpl = ("apple", "mango", "banana")
    while True:
        print("\nTuple operations: ")
        print("1.Display")
        print("2.Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Tuple: ", tpl)
        elif choice == 2:
            break
        else:
            print("Invalid choice...Please try again!!") 

def set_operations():
    st = set()
    while True:
        print("\nSet operations: ")
        print("1.Insert")
        print("2.Delete")
        print("3.Display")
        print("4.Search")
        print("5.Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = input("Enter the element to insert: ")
            st.add(element)
        elif choice == 2:
            element = input("Enter the element to be deleted: ")
            if element in st:
                st.discard(element)
                print("Element deleted!!")
            else: 
                print("Element not found")
        elif choice == 3:
            print("Set: ", st)
        elif choice == 4:
            element = input("Enter the element to be searched: ")
            if element in st:
                print("Element found")
            else:
                print("Element not found!!")
        elif choice == 5:
            break
        else:
            print("Invalid choice...Please try again!!")

def dict_operations():
    dct = {}
    while True:
        print("\nDictionary operations: ")
        print("1.Insert/Update")
        print("2.Delete")
        print("3.Display")
        print("4.Search")
        print("5.Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = input("Enter key: ")
            value = input("Enter value: ")
            dct[key] = value
        elif choice == 2:
            key = input("Enter the key to delete it: ")
            if key in dct:
                del dct[key]
                print("Key and corresponding value deleted!!")
            else:
                print("Key not found!!")
        elif choice == 3:
            print("Dictionary: ", dct)
        elif choice == 4:
            key = input("Enter the key to search: ")
            if key in dct:
                print("key is found. Value: ", dct[key])
            else:
                print("Key not found!!")
        elif choice == 5:
            break
        else:
            print("Invalid choice...Please try again!!")

def main():
    while True:
        print("\nMain Menu: ")
        print("1.List operations")
        print("2.Tuple operations")
        print("3.Set Operations")
        print("4.Dictionary operations")
        print("5.Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            list_operations()
        elif choice == 2:
            tuple_operations()
        elif choice == 3:
            set_operations()
        elif choice == 4:
            dict_operations()
        elif choice == 5:
            break
        else:
            print("Invalid choice entered. Please try again!!")


if __name__ == "__main__":
    main()