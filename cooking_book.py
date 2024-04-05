cook_book = {}
with open('recipies.txt', encoding='utf-8') as recipie:
    all_recipies = recipie.read().splitlines()
    for i in range(len(all_recipies)):
        if all_recipies[i].isdigit():
            cook_book[all_recipies[i-1]] = []
            for j in range(int(all_recipies[i])):
                list_of_ingridients = {}
                ingridient, count, mesure = all_recipies[i+j+1].split(' | ')
                list_of_ingridients.update({'ingredient_name': ingridient})
                list_of_ingridients.update({'quantity': int(count)})
                list_of_ingridients.update({'measure': mesure})

                cook_book[all_recipies[i-1]] += [list_of_ingridients]

for key, value in cook_book.items():
    print(key, ':')
    for i in value:
        print(i)
    print()


def get_shop_list_by_dishes(dishes, person_count):
    new_dict = {}
    for dish in dishes:
        for key, value in cook_book.items():
            if dish == key:
                for i in value:
                    if i['ingredient_name'] not in new_dict.keys():
                        new_dict[i['ingredient_name']] = {'measure': i['measure'], 'quantity': [i['quantity']]}
                    else:
                        new_dict[i['ingredient_name']]['quantity'] += [i['quantity']]

    for key, value in new_dict.items():
        value['quantity'] = int(sum(value['quantity'])*person_count)
    print(new_dict)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
