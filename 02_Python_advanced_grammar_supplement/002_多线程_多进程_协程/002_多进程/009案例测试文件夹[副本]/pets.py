# coding=utf-8
# ����whileѭ����remove������ɾ���б������е�cat
# ��cat����pets�б���ʱ��while����ΪTrue���ͻ᲻��ѭ������

pets = ['dog', 'cat', 'snake', 'pig', 'cat', 'goldfish', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
