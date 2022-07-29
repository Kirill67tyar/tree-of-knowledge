import socket, select

s = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM
)
s.bind(('127.0.0.1', 8080))
s.listen(10)
while True:
    conn, addr = s.accept()
    path = conn.recv(512).decode('utf8').rstrip(r'\r\n')
    with open('/www' + str(path), 'r') as file:
        data = file.read().encode('utf8')
    conn.sendall(data)
    file.close()
    conn.close()

# пример мультиплексирования:

readsocks = []  # список сокетов на которых мы ожидаем чтение
writesocks = []  # список сокетов на которых мы ожидаем запись

while True:
    readables, writeables, exceptions = select(readsocks, writesocks, [])
    # readables - список сокетов, у которых уже есть данные
    #             из которых можно читать и не быть заблокированым
    #             это и есть список сокетов, у которых уже появились данные
    # writeables - список сокетов, которые можно писать
    #             достаточно места в буффере, чтобы записать данные
    # exceptions - список сокетов с ошибкой
    # ниде будем рассматривать только список readables
    for sockjob in readables:
        # для каждого элемента из списка readables делаем чтение
        data = sockjob.recv(512)
        if not data:
            # если данных нет, а так будет, если:
            #     пришёл tcp сегмент с флагом фин (fin?)
            #     пришёл tcp сегмент с флагом reset (fin?)
            # это значит что соединение закрыто
            # мы закрываем сокет и удаляем его из списка на проверку
            sockjob.close()
            readsocks.remove(sockjob)
        else:
            # иначе, если мы получили данные - мы их обрабатывааем
            # в данном случае просто вывод на экран
            print('\tgot', data, 'on', id(sockjob))
#     после чего цикл повторяется

# Вся логика сервера здесь - print('\tgot', data, 'on', id(sockjob))
# разумеется не печать)
# в той строчке мы получаем какой-то кусочек данных из сетевого соединения
# мы из этого кусочка данных можем восстановить запрос, вызвать функцию обработки запроса и т.д.



