from bs4 import BeautifulSoup
import re
import os

def main():
    path = '../domains/all-recipes/'
    for domain in os.listdir(path):
        domain_path = os.path.join(path, domain+'/')
        for filename in os.listdir(domain_path):
            full_path = os.path.join(domain_path, filename)
            if full_path.endswith('.html'):
                f = open(full_path)
                soup = BeautifulSoup(f, 'html.parser')
                name = soup.title.string
                ingredients = None
                steps = None
                divs = soup.find_all('div')
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
                        # go from ingredients to step
                        ingredients = div
                        print(div)
                        print(div.prettify())
                    elif ingredients_div and not found_ingredients:
                        found_ingredients = True
                        ingredients = div
                    elif steps_div and not found_steps:
                        found_steps = True
                        steps = div
                if found_ingredients and found_steps:
                    continue
                    print(name)
                    print(ingredients)
                    print(steps)
                    print('\n\n')
    print('main')

if __name__ == '__main__':
    main()