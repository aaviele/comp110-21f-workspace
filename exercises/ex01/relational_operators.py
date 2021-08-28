"""relational operators."""

__author__ = "730322189"

left: int = int(input("What is the number on the left? "))
right: int = int(input("What is the number on the right? "))
less_than: bool = left < right
greater_than: bool = left >= right
equal_to: bool = left == right
not_equal: bool = left != right

left_num: str = str(left)
right_num: str = str(right)

less_than_text: str = str(less_than)
greater_than_text: str = str(greater_than)
equal_to_text: str = str(equal_to)
not_equal_text: str = str(not_equal)

print(left_num + " < " + right_num + " is " + less_than_text)
print(left_num + " >= " + right_num + " is " + greater_than_text)
print(left_num + " == " + right_num + " is " + equal_to_text)
print(left_num + " != " + right_num + " is " + not_equal_text)