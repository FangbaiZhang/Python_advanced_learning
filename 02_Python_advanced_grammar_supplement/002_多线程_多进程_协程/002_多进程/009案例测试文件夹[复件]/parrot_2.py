# coding=utf-8
# ����һ���ֵΪTrue(True �� False ����Ҫ��д��������ȷʶ��),�������ֵΪTrue�ͼ������У����ΪFalse��ֹͣwhileѭ��
# ��ϸ˵���ο��̲�P1057

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        avtive = False
    else:
        print(message)


