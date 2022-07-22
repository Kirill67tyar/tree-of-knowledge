# help(dict(a=1).items())
# print(*dir(dict(a=1).items()), sep='\n')
# print(type())
#

import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создаём новый сокет
# *
print(1)
sock.bind(('127.0.0.1', 1234)) # данный сокет связывается с адресом (bind - связывать)
print(2)
sock.listen(10) # необходимо начать принимать сетевые соединения на данном адресе
# ****
# bind и listen вызываются вместо метода connect
# 10 - длина очереди клиентов, которые могут ожидать сервера
print(3)

while True:
    conn, addr = sock.accept()
    # **
    # ***
    # conn - сокет для работы с конкретным клиентом
    # addr - информация о подключении, ip адрес клиента
    print(4)
    while True:
        # ****
        data = conn.recv(1024) # читаем данные
        # *****
        print(5)
        if not data:
            break
        conn.send(data) # отправляем данные назад
    conn.close() # соединение закрывается
    print(6)



































