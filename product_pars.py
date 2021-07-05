from re import T
import prettytable
from selenium import webdriver
import time
from prettytable import PrettyTable

class Product_pars(object):

    result_list = []
    URL1 = 'https://5ka.ru/special_offers/'
    
    def __init__(self, driver, product_name):
        self.driver = driver
        self.product_name = product_name

    def parse_product_5ka(self):
        self.driver.get(self.URL1)
        self.driver.find_element_by_class_name('search_input').send_keys(self.product_name)
        self.driver.find_element_by_class_name('search_btn').click() 
        time.sleep(1)
        
        #accept cockies
        self.accept_cockies_5ka()
        #click on more special-offers btn
        while 1:
            try:
                self.driver.find_element_by_class_name('special-offers__more-btn').click()
                time.sleep(1)
            except:
                break
        #items_list
        list_items = self.driver.find_elements_by_class_name('sale-card')
        #create list of product items
        for item in list_items:
            try:
                info = []
                info.append(item.find_element_by_class_name('sale-card__title').text)
                info.append(item.find_element_by_class_name('sale-card__price--old').text)
                info.append(item.find_element_by_class_name('sale-card__price--new').find_element_by_class_name('sale-card__price--new').text)
                info.append('5ka')
                self.result_list.append(info)
            except:
                break

    #method for accept cockies 5ka
    def accept_cockies_5ka(self):
        try:
            self.driver.find_element_by_class_name('message__button').click()
        except:
            return False
        return True

    def print_table(self):
        table = PrettyTable()
        table.field_names = ["PRODUCT_NAME", "OLD_PRICE", "NEW_PRICE", "SHOP"]
        for element in self.result_list:
            table.add_row(element)
        print(table)
        table.clear()

    def clear_all(self):
        self.result_list.clear()

    


