#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выполнить индивидуальное задание 1 лабораторной работы 4.1,
максимально задействовав имеющиеся в Python средства перегрузки операторов.

Поле first — целое положительное число, часы; поле second — целое положительное
число, минуты. Реализовать метод minutes() — приведение времени в минуты.
"""


class Conversion:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    # строковое представление времени
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    # сумма времен
    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        carry_hours = total_minutes // 60
        total_minutes %= 60
        total_hours = self.hours + other.hours + carry_hours
        return Conversion(total_hours, total_minutes)

    # разность времен
    def __sub__(self, other):
        total_minutes = (self.hours * 60 + self.minutes) - (other.hours * 60 + other.minutes)
        if total_minutes < 0:
            raise ValueError("Результат отрицательный")
        total_hours = total_minutes // 60
        total_minutes %= 60
        return Conversion(total_hours, total_minutes)

    # сравнение времен
    def __lt__(self, other):
        return self.minutes + self.hours * 60 < other.minutes + other.hours * 60

    # время в минутах
    def get_minutes(self):
        return self.hours * 60 + self.minutes


if __name__ == "__main__":
    time1 = Conversion(2, 30)
    time2 = Conversion(1, 45)

    print(time1)
    print(time2)

    sum_time = time1 + time2
    print(sum_time)

    diff_time = time1 - time2
    print(diff_time)

    print(time1 < time2)

    print(time1.get_minutes())
    print(time2.get_minutes())
