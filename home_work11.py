#  Task 1

class Product:
    def __init__(self, name, shop, price):
        self.__name = name
        self.__shop = shop
        self.__price = price

    def info(self):
        return f'Товар: {self.__name}, магазин: {self.__shop}, стоимость: {self.__price}'


class Stock:
    def __init__(self):
        self.__products = []

    def add_products(self, products):
        self.__products.append(products)

    def index(self, index):
        if 0 <= index <= len(self.__products):
            return self.__products[index].info()
        else:
            return 'товар по вашему индексу не найден'

    def name(self, name):
        for product in self.__products:
            if product._Product__name == name:
                return product.info()
        return f'товар по вашему названию не был найден'

    def sort_name(self):
        self.__products.sort(key=lambda product: product._Product__name)

    def sort_shop(self):
        self.__products.sort(key=lambda product: product._Product__shop)

    def sort_price(self):
        self.__products.sort(key=lambda product: product._Product__price)


product1 = Product('наушники', 'электронника', 456)
product2 = Product('кофта', 'одежда', 20)
product3 = Product('крем', 'косметика', 50)

stock1 = Stock()
stock1.add_products(product1)
stock1.add_products(product2)

stock2 = Stock()
stock2.add_products(product2)
stock2.add_products(product3)

stock1.sort_price()
stock2.sort_shop()
print(stock1.index(1))
print(stock2.name('крем'))


#  Task 2

class BeeElephant:
    def __init__(self, bee, elephant):
        self.__bee = max(0, min(100, bee))
        self.__elephant = max(0, min(100, elephant))

    def get_bee(self):
        return self.__bee

    def get_elephant(self):
        return self.__elephant

    def fly(self):
        return self.__bee >= self.__elephant

    def trumpet(self):
        if self.__elephant >= self.__bee:
            return 'tu-tu-doo-doo'
        else:
            return 'wzzzz'

    def eat(self, meal, value):
        if meal == 'nectar':
            self.__bee = min(100, self.__bee + value)
            self.__elephant = max(0, self.__elephant - value)
        elif meal == 'grass':
            self.__elephant = min(100, self.__elephant + value)
            self.__bee = max(0, self.__bee - value)
        else:
            raise ValueError('введите "nectar" или "grass"')


bee_elephant = BeeElephant(34, 56)

print(bee_elephant.fly())
print(bee_elephant.trumpet())

bee_elephant.eat('nectar', 45)
print(bee_elephant.get_bee())
print(bee_elephant.get_elephant())


#  Task 3

class Bus:
    def __init__(self, max_seats, max_speed):
        self.speed = 0
        self.max_speed = max_speed
        self.max_seats = max_seats
        self.passenger_names = []
        self.available_seats = max_seats
        self.seat_map = {i: None for i in range(1, max_seats + 1)}

    def start(self, *passenger_names):
        for name in passenger_names:
            if self.available_seats > 0:
                empty_seat = next(seat for seat, occupant in self.seat_map.items() if occupant is None)
                self.seat_map[empty_seat] = name
                self.passenger_names.append(name)
                self.available_seats -= 1
            else:
                print(f'Все места в автобусе заняты. {name} не может сесть')

    def stop(self, *passenger_names):
        for name in passenger_names:
            if name in self.passenger_names:
                seat = next(seat for seat, occupant in self.seat_map.items() if occupant == name)
                self.seat_map[seat] = None
                self.passenger_names.remove(name)
                self.available_seats += 1
            else:
                print(f'Пассажира {name} нет в списке пассажиров')

    def increase_speed(self, value):
        if self.speed + value <= self.max_speed:
            self.speed += value
            print(f'Скорость увеличена. Текущая скорость: {self.speed}')
        else:
            print(f'Превышена максимальная скорость. Скорость остается на уровне {self.speed}')

    def decrease_speed(self, value):
        if self.speed - value >= 0:
            self.speed -= value
            print(f'Скорость уменьшена. Текущая скорость: {self.speed}')
        else:
            print('Скорость не может быть отрицательной.')

    def __contains__(self, passenger_name):
        return passenger_name in self.passenger_names

    def __iadd__(self, passenger_name):
        self.start(passenger_name)
        return self

    def __isub__(self, passenger_name):
        self.stop(passenger_name)
        return self


bus = Bus(max_speed=80, max_seats=10)

bus.start('Иванов', 'Петров', 'Сидоров')

bus.increase_speed(10)

bus += 'НовыйПассажир'
bus -= 'Иванов'

print(f'Текущая скорость: {bus.speed}')
print(f'Свободные места: {bus.available_seats}')
print(f'Список пассажиров: {bus.passenger_names}')
print(f'Распределение мест: {bus.seat_map}')
