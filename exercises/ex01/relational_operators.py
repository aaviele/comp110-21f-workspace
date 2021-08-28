"""relational operators"""

__author__ = "730322189"

left: int = int(input("What is the number on the left? "))
right: int = int(input("What is the number on the right? "))
less_than: bool = left < right
greater_than: bool = left >= right
equal_to: bool = left == right
not_equal: bool = left != right

left_num: str = str(left)
right_num: str = str(right)

one: str = str(less_than)
two: str = str(greater_than)
three: str = str(equal_to)
four: str = str(not_equal)

print(left_num + " < " + right_num + " is " + one)
print(left_num + " >= " + right_num + " is " + two)
print(left_num + " == " + right_num + " is " + three)
print(left_num + " != " + right_num + " is " + four)