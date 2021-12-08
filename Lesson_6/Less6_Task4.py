# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Go!')
    def stop(self):
        print('stop')
    def  turn(self, direction):
        print({direction})
    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed >60:
            print('Превышение скорости!')

class  SportCar(Car):
    print('')


class WorkCar(Car):
    def show_speed(self):
        if self.speed >40:
            print('Превышение скорости!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


TownCar_1=TownCar(90, 'red', 'Kia')
SportCar_1=SportCar(180, 'Black', 'Ferrari')
WorkCar_1=WorkCar(140, 'White', 'Gaz')
PoliceCar_1=PoliceCar(60, 'Blue', 'Toyota')


print(TownCar_1.name,TownCar_1.speed, TownCar_1.color,TownCar_1.is_police)
TownCar_1.show_speed()
TownCar_1.stop()

print(SportCar_1.name, SportCar_1.speed, SportCar_1.color, SportCar_1.is_police)
SportCar_1.turn('Прямо')

print(WorkCar_1.name, WorkCar_1.speed,WorkCar_1.color, WorkCar_1.is_police)
WorkCar_1.show_speed()
WorkCar_1.turn('Направо')

print(PoliceCar_1.name, PoliceCar_1.speed,PoliceCar_1.color, PoliceCar_1.is_police)
PoliceCar_1.turn('Налево')
