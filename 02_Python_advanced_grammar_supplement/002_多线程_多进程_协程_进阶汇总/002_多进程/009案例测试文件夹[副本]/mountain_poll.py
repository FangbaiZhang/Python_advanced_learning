# coding=utf-8
# ����whileѭ��������һ�������б����Ҵ洢���ֵ���
# ��ϸ˵������P112

responses = {}

# ����һ����־��ָ�������Ƿ����
polling_active = True

while polling_active:
    # ��ʾ���뱻�����ߵ����ֺͻش�
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # �����洢���ֵ���
    responses[name] = response
    
    # �����Ƿ�����Ҫ�������
    repeat = input("Would you like to let anothor person respond? (Yes/No) ")
    if repeat == 'No':
        polling_active = False

# �����������ʾ������
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")
