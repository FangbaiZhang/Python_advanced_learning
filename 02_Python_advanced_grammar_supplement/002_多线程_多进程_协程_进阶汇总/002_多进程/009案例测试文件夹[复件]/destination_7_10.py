# coding=utf-8
# �����б��������˵����֣���ȥ������Ŀ�ĵ�
# ��ϸ˵������P113

# ���ȴ���һ�����ֵ����ڴ洢������
responses = {}

prompt_1 = "What's your name? "
prompt_2 = "Where would you want to go? "

active = True
while active:
    name = input(prompt_1)
    destination = input(prompt_2)
    responses[name] = destination
    repeat = input("Would you like to let anothor person respond? (Yes/No) ")
    if repeat == 'No':
        active = False
        
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to go to " + response.title() + ".")

