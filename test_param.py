import pytest

# @pytest.mark.parametrize("numerator, output", [(25, 0), (5, 0), (33, 0), (40, 0)])
# def test_divisible_by_five(numerator, output):
#     assert numerator % 5 == output
#	The first number in each tuple will be used as the value for numerator in each test. 
#	The second number in each tuple will be used as the value for output in each test. 

#	Each time it runs, it will use a different tuple, starting with the first in the list, and ending with the last. 
#	It will use the first number in the tuple as the value for numerator, and the second number in the tuple as the value for output.

# The assert statement is checking if the numerator divided by 5 has a remainder of 0.

# To run the test - command pallet - Python: Select Interpretor -- the one with testenv in the file name.
# re-open the terminal
# pytest test_param.py -v


# 

class Numerator:
    def __init__(self, num_list=[0, 0]):
        self.num_list = num_list
# constructor initializes a single instance attribute, num_list, with a default value of [0, 0] to be used if no value is passed in.

@pytest.fixture(params=[[1, 2], [2, 5], [6, 8]])
def divisible_by_two(request):
    return Numerator(request.param)
# •	 the fixture function has a parameter named request.
# •	When the function is run, pytest will run once for each item in the params list. So in this case, it would run 3 times.
# •	At each of these iterations, pytest will pass in a special request object.
# •	Pytest will ensure that this request object will have a param attribute that holds the current item from the params list.
#  It then returns an object of the Numerator class.

def test_divisible_by_two(divisible_by_two):
    for num in divisible_by_two.num_list:
        assert num % 2 == 0

# •	It will test each number in each list to see if it is divisible by 2. 

