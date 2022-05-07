#   4. Реализуйте базовый класс Car.
#   у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
#   которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#   опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#   добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#   для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
#   должно выводиться сообщение о превышении скорости.
#   Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def police_car(self):
        if self.is_police:
            return "\nПолицейская машина"
        else:
            return '\nГражданская машина'

    def go(self):
        return f'\n{self.name} едет'

    def stop(self):
        return f'\n{self.name} остановилась'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f' - cкорость машины {self.speed} км/ч'

class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            return f'\n{self.name} едет со скоростью {self.speed}. Превышена максимально разрешенноя скорость на {int(self.speed) - 60} км/ч!'
        else:
            return f'- cкорость машины {self.speed} км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            return f'\n{self.name} едет со скоростью {self.speed}. Превышена максимально разрешенноя скорость на {int(self.speed) - 40} км/ч!!'
        else:
            return f'- cкорость машины {self.speed} км/ч'


class PoliceCar(Car):
    pass


uaz = TownCar(85, 'зеленый', 'UAZ', False)
print(uaz.go(), uaz.show_speed(), uaz.turn('направо'), uaz.turn('за угол'), uaz.stop())

uaz_2 = TownCar(55, 'синий', 'UAZ', False)
print(uaz.police_car(), uaz_2.go(), uaz_2.show_speed(), uaz_2.turn('направо'), uaz_2.turn('за угол'), uaz_2.stop())

ferari = SportCar(200, 'красный', 'Ferari', False)
print(ferari.go(), ferari.show_speed(), ferari.turn('направо'), ferari.turn('налево'), ferari.stop())

police_ferari = PoliceCar(200, 'синий', 'Ferari', True)
print(police_ferari.police_car(), ferari.go(), police_ferari.show_speed(), police_ferari.turn('направо'), police_ferari.turn('налево'), police_ferari.stop())

