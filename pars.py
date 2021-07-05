from selenium import webdriver
import time
from product_pars import Product_pars

DRIVER_PATH = '/Users/admin/Desktop/products-parser/macos_driver/geckodriver'

def main():
    driver = webdriver.Firefox(executable_path=DRIVER_PATH)
    input_number = -1
    while input_number != 0:
        print_menu()
        input_number = int(input("Ввод:"))
        if input_number == 1: 
            product = input("Введите название продукта:")
            parser = Product_pars(driver, product)
            parser.parse_product_5ka()
            parser.print_table()
            parser.clear_all()
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