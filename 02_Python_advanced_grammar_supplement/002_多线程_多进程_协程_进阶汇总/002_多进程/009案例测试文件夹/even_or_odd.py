# coding=utf-8
# �ж�һ��������������ż��

number = input("How tall are you, in inches? ")
number = int(number)
print(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
