import queue

# 后进先出
q = queue.LifoQueue()

for i in range(5):
    q.put(i)
    print(i)

print(q)

while not q.empty():
    print(q.get())