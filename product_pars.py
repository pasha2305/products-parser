from selenium import webdriver
import time

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
        self.accept_cockies()
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
                info = {}
                info['name'] = item.find_element_by_class_name('sale-card__title').text
                info['old cost'] = item.find_element_by_class_name('sale-card__price--old').text
                info['new cost'] = item.find_element_by_class_name('sale-card__price--new')
                info['name_shop'] = '5ka'
                self.result_list.append(info)
            except:
                break

    #method for accept cockies
    def accept_cockies(self):
        try:
            self.driver.find_element_by_class_name('message__button').click()
        except:
            return False
        return True

    def print_table(self):
        print(' __________________________________________________________________ ')
        print('|       product_name       |     old price     |     new price     |')
        print(' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ')
        for element in self.result_list:
            for name, old_price, new_price in element.items():
                print(f"| {name.title()}")
