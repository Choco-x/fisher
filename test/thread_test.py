import threading


def worker():
    print(1)


t = threading.current_thread()
# 获取当前线程
print(t.getName())
# 获取线程名字
new_t = threading.Thread(target=worker)
# 开启新线程
new_t.start()
# 运行新线程
