# (a) Function to add a new key-value pair to an existing dictionary
def add_entry(d):
    d['new_key'] = 'new_value'

# (b) Function to reassign the dictionary variable to a new dictionary
def reassign_dict(d):
    d = {'completely': 'new_data'}

# --- Testing both functions ---

# Initial dictionary
my_dict = {'initial_key': 'initial_value'}
print("Original dictionary:", my_dict)

# Testing add_entry(d)
add_entry(my_dict)
print("After add_entry():  ", my_dict)

# Resetting dictionary to its original state for a clean test
my_dict = {'initial_key': 'initial_value'}

# Testing reassign_dict(d)
reassign_dict(my_dict)
print("After reassign_dict():", my_dict)