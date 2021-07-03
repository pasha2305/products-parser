from selenium import webdriver
 
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
        print(list_items)




def main():
    driver = webdriver.Firefox(executable_path='/home/admin/Документы/parser/geckodriver')
    input_number = -1
    while input_number != 0:
        print_menu()
        input_number = int(input("Enter your choice here:"))
        if input_number == 1: 
            product = input("Enter product name:")
            parser = Product_parser(driver, product)
            parser.parse_product()
        elif input_number == 2:
            print('\nВыберите интересующий магазин:\n' +
            '1. Пятерочка\n'+
            '2. Карусель\n'+
            '3. Перекресток\n')
            shop = input('Введите номер:')
            ##parser1 = Parser(driver, shop)
            ##parser1.shop()
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