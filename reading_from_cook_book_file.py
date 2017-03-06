cook_book = {}

with open('cook_book.txt') as dishes_list:  # Добавляем название блюда в словарь и читаем ингридиенты
    for line in dishes_list:
        dish_name = line.strip()
        cook_book[dish_name] = []
        ingridients_quantity = int(dishes_list.readline().strip())
        for ingridient in range(ingridients_quantity):
            ingridient_name = dishes_list.readline().split(' | ')
            # cook_book[dish_name] += ingridient_name
            cook_book[dish_name].append(ingridient_name)

print(cook_book)