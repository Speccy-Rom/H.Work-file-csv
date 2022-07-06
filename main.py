import csv
import re

flats_list = []

with open('output.csv', newline='', encoding = "utf-8") as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

# #можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
# # print (flats_list)

# # TODO 1:
# # 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки и их порядковые номера в файле.

# #удалим заголовок из нашего файла
# header = flats_list.pop(0)
# # теперь найдем все новостройки в списке и выведем их порядковые номера в файле
# for i, flat in enumerate(flats_list):
#   if flat[2] == 'новостройка':
#     print('{} - квартира с этим порядковым номером - новостройка, ее ID:{}'.format(i+1, flat[0]))

# # или

# for i in range(len(flats_list)):
#   flat = flats_list[i]
#   if flat[2] == 'новостройка':
#     print('{} - квартира с этим порядковым номером - новостройка, ее ID:{}'.format(i+1, flat[0]))

# #2) добавьте в код подсчет количества новостроек

# new_flat = 0
# for flat in flats_list:
#   if flat[2] == 'новостройка':
#     new_flat = new_flat + 1
# print('Всего новостроек в списке:', new_flat)

# #TODO 2:
# # 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID, Количество комнат;Новостройка/вторичка, Цена (руб).

# flat = flats_list[0]
# flat_info = {"id": flat[0], "rooms": flat[1], "type": flat[2], "price": flat[11]}

# # 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1 
subway_dict = {}
for flat in flats_list:
	subway = flat[3].replace("м.", "")
	if subway not in subway_dict.keys():
		subway_dict[subway] = []
	flat_info = {"id": flat[0], "rooms": flat[1], "type": flat[2], "price": flat[11]}
	subway_dict[subway].append(flat_info)
# print(subway_dict)

# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.
# дополняем предыдущий кусочек кода вот этим:
# но комментим в предыдущем куске print

for key, value in subway_dict.items():
  gap_subway_station = re.sub(r"(\w)([А-Я])", r"\1 \2", key)
  if key == '':
    print(f'Количество квартир без указания станции метро{gap_subway_station}: {len(value)}')
  else:
    print(f'Количество квартир у станции метро {gap_subway_station}: {len(value)}')