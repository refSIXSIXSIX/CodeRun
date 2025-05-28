
"""Даны нам клетки. Очевидно, что минимальный прямоугольник, который их покрывает должен покрыть самые дальние клетки(слева сверху и справа снизу). Т.е. - ищем минимальные
и максимальные координаты"""

import sys


def main():
    "Считали в строку"
    lines = sys.stdin.readlines()
    K = int(lines[0])
    points = []
    for line in lines[1:K+1]:
        x, y = map(int, line.strip().split())
        points.append((x, y))
    "Нашли мин и макс"
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    print(min_x, min_y, max_x, max_y)
    
    pass


if __name__ == '__main__':
    main()
    "Я забыл почти весь синтаксис"