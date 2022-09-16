# Functions with output
import re


def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return f"Your Name is : {first_name} {last_name}"


print(format_name("ash", "don"))
