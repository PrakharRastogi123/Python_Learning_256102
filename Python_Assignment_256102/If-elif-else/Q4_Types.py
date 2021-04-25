from ast import literal_eval

def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str

print(get_type("1"))        # <class 'int'>
print(get_type("1.2354"))   # <class 'float'>
print(get_type("True"))     # <class 'bool'>
print(get_type("abcd")) 
print(get_type("2+3j")) 
