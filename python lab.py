# Function to remove the last element from a list
def remove_last(lst):
    """
    Removes the last element from the given list.
    Modifies the list in place.
    """
    
    if len(lst) == 0:
        print("List is already empty. Nothing to remove.")
        return
    lst.pop()  # Removes last element in place

# Demonstration
if __name__ == "__main__":
    # Original list
    my_list = [10, 20, 30, 40]
    print("Before calling remove_last:", my_list)

    # Call the function
    remove_last(my_list)

    # Check if original list changed
    print("After calling remove_last:", my_list)
