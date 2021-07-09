from selenium import webdriver
import time
from product_pars import Product_pars

DRIVER_PATH = '/Users/admin/Desktop/products-parser/macos_driver/geckodriver'

def main():
    driver = webdriver.Firefox(executable_path=DRIVER_PATH)
    input_number = -1
    while input_number != 0:
        print_menu()
        try:
            input_number = int(input("Ввод:"))
        except:
            print('Некорректный ввод. Повторите попытку.')
            continue
        if input_number == 1: 
            product = input("Введите название продукта:")
            parser = Product_pars(driver, product)
            parser.parse_product_karusel()
            parser.parse_product_5ka()
            parser.parse_product_perekrestok()
            parser.print_table()
            parser.clear_all()
        elif input_number == 2:
            print('\nВыберите интересующий магазин:\n' +
            '1. Перекресток\n'+
            '2. Карусель\n'+
            '3. Пятерочка\n'+
            '0. Назад')
            try:      
                shop = int(input('Введите номер:'))
            except:
                print("Некорректный ввод. Повторите попытку.")
            if shop == 1:
                parser = Product_pars(driver, ' ')
                parser.parse_all_products_perekrestok()
                continue
            elif shop == 2:
                parser = Product_pars(driver, ' ')
                parser.parse_all_products_karusel()
                continue
            elif shop == 3:
                parser = Product_pars(driver, ' ')
                parser.parse_all_products_5ka()
                continue              
            elif shop == 0:
                continue 
            else:
                print('Такой функции нет.')
                continue   
            
        elif input_number != 0:
            print('Указан некорректный номер.')
    driver.close()
    driver.quit()

def print_menu():
    print('1. Поиск товара по названию')
    print('2. Скачать все акции из каталога')
    print('0. Выход')

if __name__ == "__main__":
    main()