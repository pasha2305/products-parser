import time
from prettytable import PrettyTable
import openpyxl

class Product_pars(object):

    result_list = []
    URL1 = 'https://5ka.ru/special_offers/'
    URL2 = 'https://www.perekrestok.ru/cat/promo/1'
    URL3 = 'https://karusel.ru/catalog/'
    
    def __init__(self, driver, product_name):
        self.driver = driver
        self.product_name = product_name
    
    def __init__(self, driver):
        self.driver = driver

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
        for item in list_items:
            self.result_list.append(self.get_item_info_perekrestok(item))

    def parse_all_products_perekrestok(self):
        self.driver.get(self.URL2)
        time.sleep(2)
        self.click_on_element('cookie-btn')
        time.sleep(2)
        self.show_all_items('catalog-content__load-more')
        list_items = self.driver.find_elements_by_class_name('sc-jrAGrp.kAEaPn')
        for item in list_items:
            self.result_list.append(self.get_item_info_perekrestok(item))
        self.print_elements_to_excel('perekrestok')
        
    def print_elements_to_excel(self, file_name):
        my_wb = openpyxl.Workbook() 
        my_sheet = my_wb.active 
        my_sheet['A1'].value = "PRODUCT NAME"
        my_sheet['B1'].value = "OLD PRICE"
        my_sheet['C1'].value = "CURRENT PRICE"
        my_sheet['D1'].value = "SHOP"
        print(len(self.result_list))
        for i in range(2, len(self.result_list)+2):
            cuurent_item = self.result_list[i - 2]
            my_sheet['A' + str(i)].value = cuurent_item[0]
            my_sheet['B' + str(i)].value = cuurent_item[1]
            my_sheet['C' + str(i)].value = cuurent_item[2]
            my_sheet['D' + str(i)].value = cuurent_item[3]
        
        my_wb.save(f'{file_name}.xlsx')

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

    def parse_all_products_karusel(self):
        for URL in self.URL_LIST_KARUSEL:
            self.driver.get(URL)
            self.click_on_element('app-button.app-button--primary.app-button--rounded.cookie-policy-tile__btn')
            self.scroll_to_down_page_1()
            list_items = self.driver.find_elements_by_class_name('card.card--none.promo-catalog-product.card--with-hover.card--fit-content')
            for item in list_items:   
                self.result_list.append(self.get_item_info_karusel(item))
        
        self.print_elements_to_excel('karusel')
                
    def get_item_info_karusel(self, item):
        info = []
        info.append(item.find_element_by_class_name('promo-catalog-product__name').text)
        info.append(item.find_element_by_class_name('promo-catalog-product__price').find_element_by_css_selector('s').text)
        info.append(item.find_element_by_class_name('promo-catalog-product__price').find_element_by_css_selector('b').text)
        info.append('karusel')
        return info

    def scroll_to_down_page_1(self):
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            SCROLL_PAUSE_TIME = 2
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.driver.execute_script(f"window.scrollTo(0, window.scrollY - 500);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            last_height = new_height

    
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
        table.field_names = ["PRODUCT_NAME", "OLD_PRICE", "CURRENT_PRICE", "SHOP"]
        for element in self.result_list:
            table.add_row(element)
        print(table)
        table.clear()

    def clear_all(self):
        self.result_list.clear()

    URL_LIST_KARUSEL = ['https://karusel.ru/catalog/1/1/1/?shop=144',
    'https://karusel.ru/catalog/1/1/2/?shop=144',
    'https://karusel.ru/catalog/1/1/3/?shop=144',
    'https://karusel.ru/catalog/1/2/4/?shop=144',
    'https://karusel.ru/catalog/1/2/5/?shop=144',
    'https://karusel.ru/catalog/1/2/6/?shop=144',
    'https://karusel.ru/catalog/1/2/7/?shop=144',
    'https://karusel.ru/catalog/1/2/8/?shop=144',
    'https://karusel.ru/catalog/1/2/9/?shop=144',
    'https://karusel.ru/catalog/1/2/10/?shop=144',
    'https://karusel.ru/catalog/1/2/11/?shop=144',
    'https://karusel.ru/catalog/1/4/18/?shop=144',
    'https://karusel.ru/catalog/1/4/19/?shop=144',
    'https://karusel.ru/catalog/1/4/20/?shop=144',
    'https://karusel.ru/catalog/1/4/21/?shop=144',
    'https://karusel.ru/catalog/1/5/23/?shop=144',
    'https://karusel.ru/catalog/1/5/25/?shop=144',
    'https://karusel.ru/catalog/1/5/26/?shop=144',
    'https://karusel.ru/catalog/1/5/27/?shop=144',
    'https://karusel.ru/catalog/1/6/29/?shop=144',
    'https://karusel.ru/catalog/1/6/30/?shop=144',
    'https://karusel.ru/catalog/1/7/32/?shop=144',
    'https://karusel.ru/catalog/1/7/33/?shop=144',
    'https://karusel.ru/catalog/1/8/34/?shop=144',
    'https://karusel.ru/catalog/1/8/35/?shop=144',
    'https://karusel.ru/catalog/1/8/36/?shop=144',
    'https://karusel.ru/catalog/1/8/37/?shop=144',
    'https://karusel.ru/catalog/1/8/38/?shop=144',
    'https://karusel.ru/catalog/1/8/39/?shop=144',
    'https://karusel.ru/catalog/1/8/41/?shop=144',
    'https://karusel.ru/catalog/1/9/42/?shop=144',
    'https://karusel.ru/catalog/1/9/43/?shop=144',
    'https://karusel.ru/catalog/1/9/44/?shop=144',
    'https://karusel.ru/catalog/1/9/45/?shop=144',
    'https://karusel.ru/catalog/1/9/46/?shop=144',
    'https://karusel.ru/catalog/1/9/49/?shop=144',
    'https://karusel.ru/catalog/1/10/50/?shop=144',
    'https://karusel.ru/catalog/1/10/58/?shop=144',
    'https://karusel.ru/catalog/1/10/60/?shop=144',
    'https://karusel.ru/catalog/1/11/61/?shop=144',
    'https://karusel.ru/catalog/1/11/62/?shop=144',
    'https://karusel.ru/catalog/1/11/63/?shop=144',
    'https://karusel.ru/catalog/1/11/64/?shop=144',
    'https://karusel.ru/catalog/1/11/65/?shop=144'
    ]