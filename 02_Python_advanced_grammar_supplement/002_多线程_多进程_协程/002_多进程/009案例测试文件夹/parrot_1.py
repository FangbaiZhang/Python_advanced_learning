# coding=utf-8
# ����һ���˳�ֵ���������ֵ�˳����������ֵ����һֱѭ������
# while�״�����ʱ�Ϳ��ַ����Ƚϣ���quit����ȣ�Ȼ��message�͵���input����������ֵ��
# prompt�������֣���һ�����У��ȴ�ӡ������input���������ݣ���Ȼ������Ҫ�����ֵ
# message�͵��������ֵ��ͬʱ�����ֵ��ӡ���������ֵ�ֺ�quit�Ƚϣ��������Ⱦͼ����¸�ѭ����
# ��ϸ˵���ο��̲�P105

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
