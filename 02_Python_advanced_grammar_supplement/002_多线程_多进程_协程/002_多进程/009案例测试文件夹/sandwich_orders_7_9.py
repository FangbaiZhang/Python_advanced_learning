# coding=utf-8
# ����һ���������б�,�������Ѭţ�ⶼ������
# ��ϸ˵������P113

sandwish_orders = ['beef', 'pastrami', 'banana', 'pastrami', 'apple', 
    'pastrami',]
print("Pastrami has been sale out.")

# ѭ��ɾ�����е�partrami
while 'pastrami' in sandwish_orders:
    sandwish_orders.remove('pastrami')

print(sandwish_orders)
