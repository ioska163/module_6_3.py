# Задача "Мифическое наследование":

# Пункты задачи:
# 1 Создайте классы родители: Horse и Eagle с методами из описания.
# 2 Создайте класс наследник Pegasus с методами из описания.
# 3 Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.

# Необходимо написать 3 класса:
class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()