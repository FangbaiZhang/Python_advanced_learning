# coding=utf-8
# ��δ��֤���û�����֤���ƶ�������֤�б�

# ���ȣ�����һ������֤���û��б�
# �ٴ���һ�����ڴ洢����֤�û��Ŀ��б�


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# ��֤ÿһ���û���ֱ��û��δ��֤���û�Ϊֹ����ÿһ����֤�����б��ƶ�������֤�б���
# ��δ��֤�б����һ����ʼ��δ��֤�б�ɾ��һ��������֤�б����һ��
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# ��ʾ��������֤���û�
print("\nThe following users have been confimed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print(confirmed_users)
