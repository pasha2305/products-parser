import time
from prettytable import PrettyTable

class Product_pars(object):

    result_list = []
    URL1 = 'https://5ka.ru/special_offers/'
    URL2 = 'https://www.perekrestok.ru/'
    URL3 = 'https://karusel.ru/catalog/'
    
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
        time.sleep(1)
        self.show_all_items('sc-jSgupP.cEbLHv')
        list_items = self.driver.find_elements_by_class_name('sc-fybufo.hKavdd')
        print(len(list_items))
        for item in list_items:
            self.result_list.append(self.get_item_info_perekrestok(item))

    def get_item_info_perekrestok(self, item):
        info = []
        info.append(item.find_element_by_class_name('product-card__link-text').text)
        try:
            info.append(item.find_element_by_class_name('price-old').text)
        except:
            info.append('')
        info.append(item.find_element_by_class_name('price-new').text)
        info.append('perekrestok')
        return info

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
        time.sleep(1)
        self.show_all_items('special-offers__more-btn')
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

    ###
    ### Карусель 
    ###     
    def parse_product_karusel(self):
        self.driver.get(self.URL3)
        self.driver.find_element_by_class_name('karusel-form-input.karusel-form-search__input').send_keys(self.product_name)
        self.scroll_to_down_page()
        list_items = self.driver.find_elements_by_class_name('card.card--none.promo-catalog-product.card--with-hover.card--fit-content')
        for item in list_items:   
            self.result_list.append(self.get_item_info_karusel(item))
                
    def get_item_info_karusel(self, item):
        info = []
        info.append(item.find_element_by_class_name('promo-catalog-product__name').text)
        info.append(item.find_element_by_class_name('promo-catalog-product__price').find_element_by_css_selector('s').text)
        info.append(item.find_element_by_class_name('promo-catalog-product__price').find_element_by_css_selector('b').text)
        info.append('karusel')
        return info

    def scroll_to_down_page(self):
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            SCROLL_PAUSE_TIME = 1
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    ###
    ### Вспомогательные методы
    ###
    def show_all_items(self, el_class):
        while 1:        
            time.sleep(1)
            if self.click_on_element(el_class) == False:
                break

    def click_on_element(self, el_class):
        try:
            self.driver.find_element_by_class_name(el_class).click()
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

    


