from bs4 import BeautifulSoup
import os
import json

def find_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

# call this function if you want to test the result:
def get_all_text(all_text_elements):
    with open('all_text.txt', 'w') as f:
        for i in all_text_elements:
            f.write(i)
            f.write('\n')


# Variables to configure:
path = './contractspecfs'
result = {
    'банковская гарантия на сумму аванса по договору': 0,
}


html_files = find_html_files(path)
all_text_elements = []

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        l = f.read()
        soup = BeautifulSoup(l, "html.parser")

    text_elements = [element.get_text() for element in soup.find_all() if element.get_text() != '']

    cleaned_text_elements = [' '.join(element.split()).lower() for element in text_elements]

    all_text_elements.extend(cleaned_text_elements)


for key, value in result.items():
    for text in all_text_elements:
        result[key] += text.count(key)

print(result)

with open('task_1_result.json', 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, ensure_ascii=False)