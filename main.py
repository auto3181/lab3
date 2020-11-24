import math
from math import sin

WIDTH = 600
HEIGHT = 600
C = 2
step = 1/10*C
x_offset = WIDTH/(-2 * 10*C)  # смещения по осям Х и У
y_offset = HEIGHT/(-2 * 10*C)  # делением на 200 находим центр
t = 0
all_values = []
pixel = []
print(x_offset)
print(y_offset)

while t <= 2 * math.pi:
    x = round(sin(t + math.pi / 2), C)
    y = round(sin(2 * t), C)
    pixel.append(x)
    pixel.append(y)
    all_values.append(tuple(pixel))  # добавляем в список всех знач. кортеж пиксель, сост. из 2х элементов
    pixel.clear()
    t += step

with open('result.bmp', 'wb+') as f:  # Открываю файл на запись в двоичном режиме
    f.write(b'BM')
    f.write((154).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(2, byteorder='little'))
    f.write((0).to_bytes(2, byteorder='little'))
    f.write((122).to_bytes(4, byteorder='little'))
    f.write((108).to_bytes(4, byteorder='little'))
    f.write(WIDTH.to_bytes(4, byteorder='little'))
    f.write(HEIGHT.to_bytes(4, byteorder='little'))
    f.write((1).to_bytes(2, byteorder='little'))
    f.write((32).to_bytes(2, byteorder='little'))
    f.write((3).to_bytes(4, byteorder='little'))
    f.write((32).to_bytes(4, byteorder='little'))
    f.write((2835).to_bytes(4, byteorder='little'))
    f.write((2835).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write(b'\xFF\x00\x00\x00')
    f.write(b'\x00\xFF\x00\x00')
    f.write(b'\x00\x00\xFF\x00')
    f.write(b'\x00\x00\x00\xFF')
    f.write(b' niW')
    f.write((0).to_bytes(36, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))

    for y_counter in range(HEIGHT):  # красим пиксели черным,если их занчение есть в списке всех значений
        x_offset = WIDTH/(-2 * 10*C)
        for x_counter in range(WIDTH):
            if (x_offset, y_offset) in all_values:
                f.write(b'\x00\x00\x00\xFF')
            else:
                f.write(b'\xFF\xFF\xFF\xFF')
            x_offset = round(x_offset + step, C)
        y_offset = round(y_offset + step, C)
    f.close()
