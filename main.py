import json

with open('newsafr.json') as f:
  temp_dict = {}
  top_10_words_list = []
  values_list = []
  data = json.load(f)
  for text in data:
    text = data['rss']['channel']['items']
    for dict_ in text:
      description = dict_['description']
      description = description.split()
      for word in description:
        if len(word) > 6:
          if word in temp_dict.keys():
            temp_dict[word] = temp_dict[word] + 1
          else:
            temp_dict[word] = 1
  for i in temp_dict:
    values_list.append([temp_dict[i], i])
  values_list.sort(reverse=True)
  for i in range(10):
    top_10_words_list.append(values_list[i])
  list_for_print = []
  for word in top_10_words_list:
    word_in_top = (f'{word[1]} - {word[0]}')
    list_for_print.append(word_in_top)

  print(f'Топ 10 слов:')
  for word in list_for_print:
    print(f'\t{word}')




print()
print()



import xml.etree.ElementTree as ET

top_10_words_list = []
values_list = []
temp_dict = {}
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
xml_descriptions = root.findall('channel/item')
for description in xml_descriptions:
  description = description.find('description').text
  description = description.split()
  for word in description:
    if len(word) > 6:
      if word in temp_dict.keys():
        temp_dict[word] = temp_dict[word] + 1
      else:
        temp_dict[word] = 1
for i in temp_dict:
  values_list.append([temp_dict[i], i])
values_list.sort(reverse=True)
for i in range(10):
  top_10_words_list.append(values_list[i])
list_for_print = []
for word in top_10_words_list:
  word_in_top = (f'{word[1]} - {word[0]}')
  list_for_print.append(word_in_top)

print('Топ 10 слов:')
for word in list_for_print:
  print(f'\t{word}')