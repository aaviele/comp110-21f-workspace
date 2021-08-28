"""numeric operators."""

__author__ = "730322189"

left: int = int(input("Enter the first number "))
right: int = int(input("Enter the second number "))

power: str = str(left ** right)
divide: str = str(left / right)
int_div: str = str(left // right)
remainder: str = str(left % right)

left_num: str = str(left)
right_num: str = str(right)

print("Left-hand side: " + left_num)
print("Right-hand side: " + right_num)
print(left_num + " ** " + right_num + " is " + power)
print(left_num + " / " + right_num + " is " + divide)
print(left_num + " // " + right_num + " is " + int_div)
print(left_num + " % " + right_num + " is " + remainder)