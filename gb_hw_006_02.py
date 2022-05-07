#   2. Реализовать класс Road (дорога).
#   определить атрибуты: length (длина), width (ширина);
#   значения атрибутов должны передаваться при создании экземпляра класса;
#   атрибуты сделать защищёнными;
#   определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#   использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
#   проверить работу метода.
#   Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    def __init__(self, _length, _width, mass_of_asp_1_cm, depth):
        self._length = _length
        self._width = _width
        self.mass_of_asp_1_cm = mass_of_asp_1_cm
        self.depth = depth

    def mass_of_asphalt(self):
        total_asp_mass = self._length * self._width * self.mass_of_asp_1_cm * self.depth / 1000
        print(f'Для покрытия дороги требуется: {int(total_asp_mass)} т асфальтной массы')

asphalt_mass = Road(5000, 20, 25, 5)
asphalt_mass.mass_of_asphalt()

