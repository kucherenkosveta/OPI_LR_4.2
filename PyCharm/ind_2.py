#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
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

    # Возвращаем код товара
    def get_code(self):
        return self.code

    # Устанавливаем новый код товара
    def set_code(self, code):
        self.code = code

    # Вовзращаем название товара
    def get_name(self):
        return self.name

    # Новое название товара
    def set_name(self, name):
        self.name = name

    # Цена за ед. товара
    def get_price(self):
        return self.price

    # Новая цена за ед. товара
    def set_price(self, price):
        self.price = price

    # Количество товара, который купили
    def get_quantity(self):
        return self.quantity

    # Новое количество товара, который купили
    def set_quantity(self, quantity):
        self.quantity = quantity

    # Общая стоимость покупки
    def calculate_total_price(self):
        return self.price * self.quantity

class Receipt:
    def __init__(self, receipt_number, date_time):
        self.receipt_number = receipt_number
        self.date_time = date_time
        self.items = []

    # Добавляем покупку в чек
    def add_item(self, goods):
        self.items.append(goods)

    def update_item(self, code, new_goods):
        for i in range(len(self.items)):
            if self.items[i].get_code() == code:
                self.items[i] = new_goods
                return True
        return False

    # Удаляем товар из чека по коду
    def remove_item(self, code):
        for i in range(len(self.items)):
            if self.items[i].get_code() == code:
                del self.items[i]
                return True
        return False

    # Поиск товара по коду
    def find_item_by_code(self, code):
        for item in self.items:
            if item.get_code() == code:
                return item
        return None

    # Общая сумма покупок
    def calculate_total_amount(self):
        total_amount = 0
        for item in self.items:
            total_amount += item.calculate_total_price()
        return total_amount

if __name__ == "__main__":

    item1 = Goods("001", "Хлеб", 10, 2)
    item2 = Goods("002", "Молоко", 5, 3)

    receipt = Receipt("0001", "20.05.2023 22:00")
    print("Номер чека:", receipt.receipt_number)
    print("Дата и время создания:", receipt.date_time)

    # Добавление товаров в чек
    receipt.add_item(item1)
    receipt.add_item(item2)

    # Изменение количества товара в чеке
    updated_item = Goods("001", "Хлеб", 10, 5)
    receipt.update_item("001", updated_item)

    # Удаление товара из чека
    receipt.remove_item("001")

    # Поиск информации о товаре по его коду
    found_item = receipt.find_item_by_code("002")
    if found_item:
        print("Найден товар:", found_item.get_name())
    else:
        print("Товар не найден.")

    # Подсчет общей суммы покупок
    total_amount = receipt.calculate_total_amount()
    print("Общая сумма покупок:", total_amount)



