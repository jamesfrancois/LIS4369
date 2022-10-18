def get_requirements():
   
    print("Developer: James S. Francois")
    print("Python Loops")
    print("\nProgram Requirements:\n"
    +"1. Sets (Python data structure): mutable, heterogeneous, unordered sequence of elements, *but* cannot hold duplicate values\n"
    +"2. Sets are mutable/changeable that is, can insert, update, delete.\n"
    +"3. While sets are mutable/changeable, they *cannot* contain other mutable items like list, set, or dictionary that is, elements contained in set must be immutable.\n"
    +"4. Also, since sets are unordered, cannot use indexing (or, slicing) to access, update, or delete elements. "
    +"5. Two methods to create sets:"
        +"a. Create set using curly brackets {set}: my_set = {1, 3.14, 2.0, 'four', 'Five'}"
        +"b. Create set using set() function: my_set = set(<iterable>)"
    +"6. 6. Create a program that mirrors the following IPO (input/process/output) format.")
 
def print_type():
    # declare set using brackets
    my_set = {1, 'domino', 'domingo', 44.0, ('la', 'le', 'lo') }
    # declare set using built-in set method with brackets
    my_set1 = set([1, 2, 3, 'four', 'five'])
    # declare set using built in set() method using parenthasis
    my_set2 = set(('this', 'is', 'fun'))
    # printing sets to screen
    print(my_set)
    print(my_set1)
    print(my_set2)
    # printing set types to make sure they are sets
    print(type(my_set))
    print(type(my_set1))
    print(type(my_set2))
    #print length of set 1
    print(len(my_set))
    # deleting items in set using discard() and remove(). Discard does not raise a typeError if item is not found
    my_set.discard('domino')
    print(my_set)
    my_set.remove('domingo')
    print(my_set)
    print(len(my_set))
    # adding an element  to a set
    my_set.add('addition')
    # more deleting items in set
    my_set1.discard('four')
    my_set1.discard('five')
    print(len(my_set1))
    print(len(my_set))
    # python built in functions for comparing items in set. Must all be same datatype
    print(max(my_set1))
    print(min(my_set1))
    print(sum(my_set1))
    #using set function clear() to clear the set
    my_set1.clear()
    print(len(my_set1))
    
def main():
    get_requirements()
    print_type()

if __name__ == "__main__":
    main()