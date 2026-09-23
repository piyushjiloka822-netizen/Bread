#Functon to replace the first charcater  of a string with 'x'
def change_string(s):
    #Validate input type

    if len(s) == 0:
        return s #Return unchanged if empty string
    #Strings are immutable,so we create a new string
    new_s = 'x' + s[1:]
    print("Inside function:",new_s)
    return new_s
# Original string
original = "Hello"
modified = change_string(original)
print("Original string after function call:",original)    