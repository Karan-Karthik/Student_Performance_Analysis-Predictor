
'''
Step-by-Step Explanation

1) Define a Function to Create Detailed Error Messages

2) CustomException Class:

Inheritance: CustomException inherits from Exception.
Initialization: The __init__ method initializes the custom exception with a detailed error message.

3) Calling super().__init__(error_message):

This calls the __init__ method of the built-in Exception class.
It ensures that the error_message is properly stored in the exception, just like any standard exception in Python.


4) Storing the Detailed Error Message:

After calling the parent class constructor, the CustomException class creates and stores a more detailed error message.
'''

import sys
from source.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exec_tb= error_detail.exc_info()

    file_name=exec_tb.tb_frame.f_code.co_filename

    line_number= exec_tb.tb_lineno

    error_message= "Error occured in python script name[{0}], line number [{1}], error message [(2)]".format(
        file_name, line_number, str(error))
    
    return error_message

#Custom exception class
## parameter class- Parent class
##Newly defined class- Child/Sub class
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):    

        #The Exception class's __init__ method expects a message parameter, which is used to store the error message.
        super().__init__(error_message)
        
        self.error_message= error_message_detail(error_message, error_detail= error_detail)

    def __str__(self):
        
        return self.error_message