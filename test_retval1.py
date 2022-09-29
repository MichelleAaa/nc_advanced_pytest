# If pytest finds a conftest.py file in a folder, it will automatically make the fixtures in it available to all tests in that same folder.
# This code defines a fixture function with the name input_value. When invoked, it returns the integer 10. 

def func_retval():
    some_int = 10
    return some_int

def test_func_retval(input_value):
    assert func_retval() == input_value

# The input_value fixture is used as a parameter in the test function here. (Note that input_value is in the conftest.py file.)
# This means in the test_func_retval function's body, the return value of the input_value() function is assigned to a variable that is also named input_value. 
# This input_value variable is compared for equality to the return value from invoking func_retval().
# The test passes if the values are the same, and fails if they are different. 
