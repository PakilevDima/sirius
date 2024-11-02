from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
import string


def get_text_litrary(url: str, file_name: str):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    h1 = driver.find_element(By.ID, 'bnav')
    with open(f'{file_name}.txt', 'w', encoding="utf-8") as file:
        count_page = h1.text.split('\n')[0].split('/')[1]

        for i in range(1, int(count_page) + 1):
            driver.get(f"https://ilibrary.ru/text/436/p.{i}/index.html")
            h1 = driver.find_element(By.ID, 'pmt1')
            file.write(h1.text + '\n')
            time.sleep(1)


    driver.quit()


def get_authors(url: str, file_name: str):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    h1 = driver.find_element(By.CLASS_NAME, 'alst')
    urls = []
    for link in h1.find_elements(By.TAG_NAME, 'a'):
        urls.append([link.get_attribute('href'), link.text])

    with open(f'{file_name}.txt', 'w') as file:
        for i in urls:
            file.write(str(i[0]) + ' ' + str(i[1]) + '\n')



def get_text(url):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver2 = webdriver.Chrome(options=options)
    driver2.get(url)
    text_lit = ''
    title_lit = driver2.find_element(By.TAG_NAME, 'h1').text
    try:
        driver2.find_element(By.ID, 'bnav')
    except NoSuchElementException:
        try:
            text_lit += driver2.find_element(By.ID, 'pmt1').text
        except BaseException:
            pass
    else:
        pages = driver2.find_element(By.ID, 'bnav').text.split('\n')[0].split('/')[1]
        link = url.split('/')

        for i in range(2, int(pages) + 1):
            driver2.get(f'https://ilibrary.ru/{link[3]}/{link[4]}/p.{i}/{link[6]}')
            for j in driver2.find_elements(By.TAG_NAME, 'z'):
                text_lit += j.text + '\n'
    time.sleep(0.1)

    driver2.close()

    if title_lit == '* * *':
        title_lit = text_lit.split('\n')[0].translate(str.maketrans('', '',
                                    string.punctuation)).replace(' ', '_')

    return [title_lit, text_lit]


def write_author_files(file_author):
    with open(f'{file_author}', 'r') as file:
        for i in file.readlines():
            if os.path.isdir(f"{os.getcwd()}/authors/{'_'.join(i.split()[1:]).replace('.', '')}") is False:
                os.mkdir(f"{os.getcwd()}/authors/{'_'.join(i.split()[1:]).replace('.', '')}")
                os.mkdir(f"{os.getcwd()}/authors/{'_'.join(i.split()[1:]).replace('.', '')}/litraty")
            with open(f"{os.getcwd()}/authors/{'_'.join(i.split()[1:]).replace('.', '')}/link_litrary.txt", 'w', encoding="utf-8") as lit_file:
                options = Options()
                options.headless = True
                options.add_argument("--window-size=1920,1200")
                driver = webdriver.Chrome(options=options)
                driver.get(i.split()[0])
                try:
                    h1 = driver.find_element(By.ID, 'az')
                except NoSuchElementException:
                    h1 = driver.find_element(By.CLASS_NAME, 'list')
                    for litraty in h1.find_elements(By.TAG_NAME, 'a'):
                        lit_file.write(f'{litraty.get_attribute("href")} {litraty.text}\n')
                else:
                    driver.get(h1.find_elements(By.TAG_NAME, 'a')[-1].get_attribute('href'))
                    h2 = driver.find_element(By.CLASS_NAME, 'list')
                    for lit in h2.find_elements(By.TAG_NAME, 'a'):
                        lit_file.write(f"{lit.get_attribute('href')} {lit.text}\n")




def walk_txt_file():
    for i in os.listdir(os.path.join(os.getcwd(), 'authors')):
        with open(f'{os.path.join(os.getcwd(), "authors", i)}/link_litrary.txt', 'r', encoding='utf-8') as file:
            for lit in file.readlines():
                list_my = get_text(lit)
                print(list_my)





# write_author_files('urls_authors.txt')
# print(get_text('https://ilibrary.ru/text/4290/p.1/index.html'))
print(get_text('https://ilibrary.ru/text/436/p.1/index.html')[-1])