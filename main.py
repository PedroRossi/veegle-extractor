from extractor import Extractor
import os

def main():
    path = '../domains/all-recipes/'
    recipes = []
    for domain in os.listdir(path):
        domain_path = os.path.join(path, domain+'/')
        for filename in os.listdir(domain_path):
            full_path = os.path.join(domain_path, filename)
            if full_path.endswith('.html'):
                try:
                    e = Extractor(full_path)
                    recipes.append(e)
                except:
                    print('error in\ndomain: ' + domain + '\nfile: ' + filename + '\n')

if __name__ == '__main__':
    main()