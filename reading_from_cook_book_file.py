cook_book = {}
cook_book_new = {}

with open('cook_book.txt') as dishes_list:  # Добавляем название блюда в словарь и читаем ингридиенты
    for line in dishes_list:
        dish_name = line.strip()
        cook_book[dish_name] = []
        ingridients_quantity = int(dishes_list.readline().strip())
        for ingridient in range(ingridients_quantity):
            cook_book[dish_name].append(ingridient_name)
            ingridient = dishes_list.readline().split(' | ')
            cook_book_new['ingridient_name'] = ingridient[0]
            cook_book_new['quantity'] = ingridient[1]
            cook_book_new['measure'] = ingridient[2]

            cook_book[dish_name].append(cook_book_new.copy())


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            # print(new_shop_list_item['quantity'])
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()