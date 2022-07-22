# help(dict(a=1).items())
# print(*dir(dict(a=1).items()), sep='\n')
# print(type())
#

import socket




request = 'Hello TCP'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаётся новый объект socket
    # *
    # AF_INET - показывает что мы работаем с сетевыми сокетами
    # SOCK_STREAM - что мы используем сокет для работы с TCP

sock.connect(('127.0.0.1', 1234))  # подключаемся к удалённой машине
    # **
    # ***
    # ****
    # '127.0.0.1' - ip адрес машины (наш компьютер)
    # 1234 - порт машины к которой мы подключаемся

sock.send(request.encode())  # отправляем данные (строчку по протоколу TCP)

response = sock.recv(1024)  # здесь мы получаем данные (метод recv)
    # 1024 - размер буфера, не больше какого числа, данных мы хотим получить
print(response)

sock.close()  # соединение закрывается




































