#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дополнительно к требуемым в заданиях операциям перегрузить операцию индексирования [].
Максимально возможный размер списка задать константой. В отдельном поле size должно
храниться максимальное для данного объекта количество элементов списка; реализовать метод
size(), возвращающий установленную длину. Если количество элементов списка изменяется во
время работы, определить в классе поле count. Первоначальные значения size и count
устанавливаются конструктором.
В тех задачах, где возможно, реализовать конструктор инициализации строкой.

Товарный чек содержит список товаров, купленных покупателем в магазине. Один элемент
списка представляет собой пару: товар-сумма. Товар — это класс Goods с полями кода и
наименования товара, цены за единицу товара, количества покупаемых единиц товара. В
классе должны быть реализованы методы доступа к полям для получения и изменения
информации, а также метод вычисления суммы оплаты за товар. Для моделирования
товарного чека реализовать класс Receipt, полями которого являются номер товарного чека,
дата и время его создания, список покупаемых товаров. В классе Receipt реализовать
методы добавления, изменения и удаления записи о покупаемом товаре, метод поиска
информации об определенном виде товара по его коду, а также метод подсчета общей
суммы, на которую были осуществлены покупки. Методы добавления и изменения
принимают в качестве аргумента объект класса Goods. Метод поиска возвращает объект
класса Goods в качестве результата.
"""


class Goods:
    def __init__(self, code, name, price, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Товар: {self.name}, Код: {self.code}, Цена: {self.price}, Количество: {self.quantity}"


class Receipt:
    MAX_SIZE = 10

    def __init__(self, receipt_number, date_time):
        self.receipt_number = receipt_number
        self.date_time = date_time
        self.items = []
        self.size = Receipt.MAX_SIZE
        self.count = 0

    def add_item(self, goods):
        if self.count < self.size:
            self.items.append(goods)
            self.count += 1
            return True
        else:
            return False

    def update_item(self, code, new_goods):
        for i in range(self.count):
            if self.items[i].get_code() == code:
                self.items[i] = new_goods
                return True
        return False

    def remove_item(self, code):
        for i in range(self.count):
            if self.items[i].get_code() == code:
                del self.items[i]
                self.count -= 1
                return True
        return False

    def find_item_by_code(self, code):
        for item in self.items:
            if item.get_code() == code:
                return item
        return None

    def calculate_total_amount(self):
        total_amount = 0
        for item in self.items:
            total_amount += item.calculate_total_price()
        return total_amount

    def __getitem__(self, index):
        return self.items[index]

    def size(self):
        return self.size


if __name__ == "__main__":
    item1 = Goods("001", "Хлеб", 10, 2)
    item2 = Goods("002", "Молоко", 5, 3)

    receipt = Receipt("0001", "20.05.2023 22:00")
    print("Номер чека:", receipt.receipt_number)
    print("Дата и время создания:", receipt.date_time)

    receipt.add_item(item1)
    receipt.add_item(item2)

    updated_item = Goods("001", "Хлеб", 10, 5)
    receipt.update_item("001", updated_item)

    receipt.remove_item("001")

    found_item = receipt.find_item_by_code("002")
    if found_item:
        print("Найден товар:", found_item.get_name())
    else:
        print("Товар не найден.")

    total_amount = receipt.calculate_total_amount()
    print("Общая сумма покупок:", total_amount)

    # Проверка операции индексирования
    print(receipt[0])
