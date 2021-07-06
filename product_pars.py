from selenium import webdriver
import time
from prettytable import PrettyTable
from selenium.webdriver.common.by import By

class Product_pars(object):

    result_list = []
    URL1 = 'https://5ka.ru/special_offers/'
    URL2 = 'https://www.perekrestok.ru/'
    
    def __init__(self, driver, product_name):
        self.driver = driver
        self.product_name = product_name

    ###
    ### Перекресток
    ###
    def parse_product_perekrestok(self):
        self.driver.get(self.URL2)
        time.sleep(2)
        self.driver.find_element_by_class_name('Input__InputStyled-sc-1kqlv3u-0').send_keys(self.product_name)
        self.click_on_element('search-form__button-submit')
        self.click_on_element('cookie-btn')
        while 1:          
            if self.click_on_element('sc-jSgupP.cEbLHv') == False:
                break

    def click_on_element(self, el_name):
        try:
            self.driver.find_element_by_class_name(el_name).click()
        except:
            return False
        return True

    ###
    ### Пятерочка   
    ### 
    def parse_product_5ka(self):
        self.driver.get(self.URL1)
        self.driver.find_element_by_class_name('search_input').send_keys(self.product_name)
        self.click_on_element('search_btn')
        #self.driver.find_element_by_class_name('search_btn').click() 
        time.sleep(1)
        #accept cockies
        self.click_on_element('message__button')
        #click on more special-offers btn
        while 1:
            if self.click_on_element('special-offers__more-btn') == False:
                break
        #items_list
        list_items = self.driver.find_elements_by_class_name('sale-card')
        #create list of product items
        for item in list_items:
            try:
                self.result_list.append(self.get_item_info_5ka(item))
            except:
                break

    def get_item_info_5ka(self, item):
        info = []
        info.append(item.find_element_by_class_name('sale-card__title').text)
        info.append(item.find_element_by_class_name('sale-card__price--old').text)
        info.append(item.find_element_by_class_name('sale-card__price--new').find_element_by_class_name('sale-card__price--new').text)
        info.append('5ka')
        return info      

    def print_table(self):
        table = PrettyTable()
        table.field_names = ["PRODUCT_NAME", "OLD_PRICE", "NEW_PRICE", "SHOP"]
        for element in self.result_list:
            table.add_row(element)
        print(table)
        table.clear()

    def clear_all(self):
        self.result_list.clear()

    


