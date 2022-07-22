"""

---------------------------- Часть 1 ----------------------------
Для этого нам понадобится реализовать несколько классов и связать их между собой.
Первый класс, который мы реализуем, будет Product. Это класс, описывающий товар.
В нем должно быть реализовано:

метод __init__, принимающий на вход имя товара и его стоимость. Эти значения необходимо сохранить в атрибутах name и price
Пример работы с классом Product

carrot = Product('carrot', 30)
print(carrot.name, carrot.price)




---------------------------- Часть 2 ----------------------------
Далее для оформления заказа нам нужен пользователь. Для этого создадим класс User, который содержит:

метод __init__, принимающий на вход логин пользователя и необязательный аргумент баланс его счета(по умолчанию 0).
Логин необходимо сохранить в атрибуте login , а баланс необходимо присвоить сеттеру   balance  (см. пункт 4)
метод __str__, возвращающий строку вида «Пользователь {login}, баланс - {balance}»
Cвойство геттер balance, которое возвращает значение self.__balance;
Свойство сеттер balance, принимает новое значение баланса и устанавливает его в атрибут self.__balance ;
метод deposit  принимает числовое значение и прибавляет его к атрибуту self.__balance ;
метод payment  принимает числовое значение, которое должно списаться с баланса пользователя.
Если на счете у пользователя не хватает средств, то необходимо вывести фразу  «Не хватает средств на балансе.
Пополните счет» и вернуть False. Если средств хватает, списываем с баланса у пользователя указанную сумму и возвращаем True
Пример работы с классом User

billy = User('billy@rambler.ru')
print(billy) # Пользователь billy@rambler.ru, баланс - 0
billy.deposit(100)
billy.deposit(300)
print(billy) # Пользователь billy@rambler.ru, баланс - 400
billy.payment(500) # Не хватает средств на балансе. Пополните счет
billy.payment(150)
print(billy) # Пользователь billy@rambler.ru, баланс - 250
Необходимо только написать определение класса User



---------------------------- Часть 3 ----------------------------
Последний штрих - создание класса корзины, куда наш пользователь будет складывать товары.
Для этого нам понадобятся ранее созданные классы User и Product

И так, создаем класс Cart, который содержит:

метод __init__, принимающий на вход экземпляр класса User . Его необходимо сохранить в атрибуте user .
Помимо этого метод  должен создать атрибут goods - пустой словарь (лучше использовать defaultdict).
Он нужен будет для хранения наших товаров и их количества(ключ словаря - товар, значение - количество).
И еще нам понадобится создать защищенный атрибут .__total со значением 0. В нем будет хранится итоговая сумма заказа

метод add принимает на вход экземпляр класса Product и необязательный аргумент количество товаров (по умолчанию 1).
Метод add  должен увеличить в корзине (атрибут goods) количество указанного товара
на переданное значение количество и пересчитать атрибут self.__total

метод remove  принимает на вход экземпляр класса Product и необязательный аргумент количество товаров (по умолчанию 1).
Метод remove  должен уменьшить в корзине (атрибут goods) количество указанного товара
на переданное значение количество и пересчитать атрибут self.__total.
Обратите внимание на то, что количество товара в корзине не может стать отрицательным как и итоговая сумма

Cвойство геттер total  , которое возвращает значение self.__total;

метод order  должен использовать метод payment  из класса User и передать в него итоговую сумму корзины.
В случае, если средств пользователю хватило, вывести сообщение «Заказ оплачен», в противном случае - «Проблема с оплатой»;

метод print_check  печатающий на экран чек. Он должен начинаться со строки
---Yor check---
Затем выводится состав корзины в алфавитном порядке по названию товара в виде
{Имя товара} {Цена товара} {Количество товара} {Сумма}
И заканчивается чек строкой
---Total: {self.total}---


Пример использования класса Cart

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20
"""


# part 1
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


# part 2
class User:

    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.balance += value

    def payment(self, value):
        if value > self.balance:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.balance -= value
            return True


if __name__ == '__main__':
    # billy = User('billy@rambler.ru')
    # print(billy)  # Пользователь billy@rambler.ru, баланс - 0
    # billy.deposit(100)
    # billy.deposit(300)
    # print(billy)  # Пользователь billy@rambler.ru, баланс - 400
    # billy.payment(500)  # Не хватает средств на балансе. Пополните счет
    # billy.payment(150)
    # print(billy)  # Пользователь billy@rambler.ru, баланс - 250
    pass

# part 3
class Cart:

    def __init__(self, user):
        self.user = user
        self.goods = {}
        self.__total = 0

    def add(self, product, quantity=1):
        self.goods.setdefault(product, 0)
        self.goods[product] += quantity
        self.__total += (product.price * quantity)

    def remove(self, product, quantity=1):
        if product in self.goods:
            if self.goods[product] >= quantity:
                self.goods[product] -= quantity
                self.__total -= (product.price * quantity)
            else:
                self.__total -= (product.price * self.goods[product])
                self.goods[product] = 0
        if not self.goods[product]:
            del self.goods[product]


    def order(self):
        if self.user.payment(self.total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    @property
    def total(self):
        return self.__total

    def print_check(self):
        goods_ls = list(self.goods.keys())
        goods_ls.sort(key=lambda x: x.name)
        print('---Yor check---')
        for product in goods_ls:
            price = product.price * self.goods[product]
            print(f'{product.name} {product.price} {self.goods[product]} {price}')
        print(f'---Total: {self.total}---')

if __name__ == '__main__':
    billy = User('billy@rambler.ru')

    lemon = Product('lemon', 20)
    carrot = Product('carrot', 30)

    cart_billy = Cart(billy)
    print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0
    cart_billy.add(lemon, 2)
    cart_billy.add(carrot)
    cart_billy.print_check()
    ''' Печатает текст ниже
    ---Yor check---
    carrot 30 1 30
    lemon 20 2 40
    ---Total: 70---'''
    cart_billy.add(lemon, 3)
    cart_billy.print_check()
    ''' Печатает текст ниже
    ---Yor check---
    carrot 30 1 30
    lemon 20 5 100
    ---Total: 130---'''
    cart_billy.remove(lemon, 6)
    cart_billy.print_check()
    ''' Печатает текст ниже
    ---Yor check---
    carrot 30 1 30
    ---Total: 30---'''
    print(cart_billy.total)  # 30
    cart_billy.add(lemon, 5)
    cart_billy.print_check()
    ''' Печатает текст ниже
    ---Yor check---
    carrot 30 1 30
    lemon 20 5 100
    ---Total: 130---'''
    cart_billy.order()
    ''' Печатает текст ниже
    Не хватает средств на балансе. Пополните счет
    Проблема с оплатой'''
    cart_billy.user.deposit(150)
    cart_billy.order()  # Заказ оплачен
    print(cart_billy.user.balance)  # 20