# coding=utf-8
# ��������ȷ��Ʊ��,��סʹ��int���������ַ��������ֵ

prompt = "\nHow old are you? "
prompt += "\nEnter 'quit' to end the program. "

age = " "
while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("You are free ticket.")
    elif age < 12:
        print("Your ticket price is 10 dollors.")
    else:
        print("Your ticket price is 15 dollors.")

