from bs4 import BeautifulSoup
import re
import json

class Extractor:
    
    def __init__(self, file_path):
        self.file = open(file_path, encoding='utf-8')
        self.soup = BeautifulSoup(self.file, 'html.parser')
        self.name = None
        self.ingredients = None
        self.steps = None
        self.__get_content()

    def __get_content(self):
        self.name = self.soup.title.string
        divs = self.soup.find_all('div')
        found_ingredients = False
        found_steps = False
        for div in divs:
            if found_ingredients and found_steps:
                break
            ingredients_div = div.find(text=re.compile('(Ingredientes)'))
            steps_div = div.find(text=re.compile('(Modo de preparo)|(Instruções)|(passos a seguir)'))
            if ingredients_div and steps_div:
                found_ingredients = True
                found_steps = True
                self.ingredients = div.text
            elif ingredients_div and not found_ingredients:
                found_ingredients = True
                self.ingredients = div.text
            elif steps_div and not found_steps:
                found_steps = True
                self.steps = div.text
        self.file.close()
        if not found_ingredients:
            raise Exception('ingredients not found')

    def to_dicitonary(self):
        data = {
            'name': self.name,
            'ingredients': self.ingredients,
            'steps': self.steps
        }
        return data

    def to_json(self):
        data = json.dumps(self.to_dicitonary, indent=True, ensure_ascii=False)
        return data