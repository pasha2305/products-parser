from selenium import webdriver

DRIVER_PATH = '/home/admin/Документы/parser/geckodriver'

class Product_parser(object):

    URL1 = 'https://5ka.ru/special_offers/'
    
    def __init__(self, driver, product_name):
        self.driver = driver
        self.product_name = product_name

    def parse_product(self):
        self.driver.get(self.URL1)
        self.driver.find_element_by_class_name('search_input').send_keys(self.product_name)
        self.driver.find_element_by_class_name('search_btn').click()
        list_items = self.driver.find_elements_by_class_name('sale-card')
        for item in list_items:
            print(item.find_element_by_css_selector('p.sale-card__title').text)

def main():
    driver = webdriver.Firefox(executable_path=DRIVER_PATH)
    input_number = -1
    while input_number != 0:
        print_menu()
        input_number = int(input("Ввод:"))
        if input_number == 1: 
            product = input("Введите название продукта:")
            parser = Product_parser(driver, product)
            parser.parse_product()
        elif input_number == 2:
            print('\nВыберите интересующий магазин:\n' +
            '1. Пятерочка\n'+
            '2. Карусель\n'+
            '3. Перекресток\n')      
            shop = input('Введите номер:')
        elif input_number != 0:
            print('Указан некорректный номер.')
            driver.close()
            driver.quit()

def print_menu():
    print('1. Find element by name')
    print('2. Download all special offers')
    print('0. Quit')

if __name__ == "__main__":
    main()