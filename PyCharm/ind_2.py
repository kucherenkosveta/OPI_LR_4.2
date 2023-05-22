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

Карточка иностранного слова представляет собой словарейу, содержащую иностранное
слово и его перевод. Для моделирования электронного словаря иностранных слов
реализовать класс Dictionary. Данный класс имеет поле-название словаря и содержит
список словарей WordCard, представляющих собой карточки иностранного слова. Название
словаря задается при создании нового словаря, но должна быть предоставлена
возможность его изменения во время работы. Карточки добавляются в словарь и удаляются
из него. Реализовать поиск определенного слова как отдельный метод. Аргументом
операции индексирования должно быть иностранное слово. В словаре не должно быть
карточек-дублей. Реализовать операции объединения, пересечения и вычитания словарей.
При реализации должен создаваться новый словарь, а исходные словари не должны
изменяться. При объединении новый словарь должен содержать без повторений все слова,
содержащиеся в обоих словарях-операндах. При пересечении новый словарь должен
состоять только из тех слов, которые имеются в обоих словарях-операндах. При вычитании
новый словарь должен содержать слова первого словаря-операнда, отсутствующие во
втором.
"""


class WordCard:
    def __init__(self, foreign_word, translation):
        self.foreign_word = foreign_word
        self.translation = translation

    def __str__(self):
        return f"{self.foreign_word}: {self.translation}"


class Dictionary:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return f"Dictionary: {self.name}"

    # перегрузка оператора индексирования []
    def __getitem__(self, foreign_word):
        for card in self.cards:
            if card.foreign_word == foreign_word:
                return card
        raise KeyError(f"Word '{foreign_word}' not found in the dictionary.")

    # метод для добавления новой карточки в словарь
    def add_card(self, card):
        if card.foreign_word not in [c.foreign_word for c in self.cards]:
            self.cards.append(card)

    # метод для удаления карточки из словаря по иностранному слову
    def remove_card(self, foreign_word):
        self.cards = [card for card in self.cards if card.foreign_word != foreign_word]

    # метод для поиска определенного слова в словаре
    def search_word(self, foreign_word):
        for card in self.cards:
            if card.foreign_word == foreign_word:
                return card
        return None

    # метод для объединения словарей
    def union(self, other_dict):
        new_dict = Dictionary(f"{self.name} + {other_dict.name}")
        new_dict.cards = self.cards.copy()
        for card in other_dict.cards:
            if card.foreign_word not in [c.foreign_word for c in new_dict.cards]:
                new_dict.cards.append(card)
        return new_dict

    # метод добавления совпадающих слов из 1 словаря во 2
    def intersection(self, other_dict):
        new_dict = Dictionary(f"{self.name} ∩ {other_dict.name}")
        for card in self.cards:
            if card.foreign_word in [c.foreign_word for c in other_dict.cards]:
                new_dict.cards.append(card)
        return new_dict

    # метод добавления несовпадающих слов из 1 словаря во 2
    def difference(self, other_dict):
        new_dict = Dictionary(f"{self.name} - {other_dict.name}")
        for card in self.cards:
            if card.foreign_word not in [c.foreign_word for c in other_dict.cards]:
                new_dict.cards.append(card)
        return new_dict

if __name__ == "__main__":
    card1 = WordCard("hello", "привет")
    card2 = WordCard("goodbye", "пока")
    card3 = WordCard("cat", "кошка")
    card4 = WordCard("dog", "собака")

    dict1 = Dictionary("English-Russian Dictionary")
    dict1.add_card(card1)
    dict1.add_card(card2)

    dict2 = Dictionary("Russian-English Dictionary")
    dict2.add_card(WordCard("привет", "hello"))
    dict2.add_card(WordCard("пока", "goodbye"))

    print(dict1["hello"])

    dict1.remove_card("goodbye")

    print(dict1.search_word("goodbye"))

    dict3 = dict1.union(dict2)
    for card in dict3.cards:
        print(card)

    dict4 = dict1.intersection(dict2)
    for card in dict4.cards:
        print(card)

    dict5 = dict1.difference(dict2)
    for card in dict5.cards:
        print(card)


