import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Downloader for pexels.com

class search:

    photo_url = []
    browser = None
    chrome_opt = Options()

    def __init__(self, search="", browser='Chrome', delay=2, head_less=False):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.browser=webdriver.Chrome(executable_path='c:/chromedriver.exe', options=chrome_options)

        #self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

        self.browser.get(f'https://www.pexels.com/search/{search}')
        time.sleep(delay)
        print('You are using pexels.com - Free stock photos')
        result=self.browser.find_elements_by_xpath('//div[@class="search__grid"]/div[@class="photos"]/div[@class="photos__column"]/div[@class="hide-featured-badge hide-favorite-badge"]/article/a[1]')
        for url in result:
            photo=url.get_property('href')
            self.photo_url.append(photo)

    def download(self, delay=1):
        if self.photo_url.__len__() > 0:
            count = 0
            print(f'Looking for possible ...{self.photo_url.__len__()} Wallpapers')
            for l1 in self.photo_url:
                try:
                    print(l1)
                    self.browser.get(l1)
                    time.sleep(delay)
                    dn = self.browser.find_element_by_class_name('rd__button--download')
                    time.sleep(1)
                    dn.click()
                    time.sleep(3)
                    count = count + 1
                except:
                    pass
            print(f'{count}  wallpapers downloaded')
        else:
            print('No photo found, slow internet connection may be')
            self.__del__()

    def __del__(self):
        try:
            #self.browser.close()
            print('Completed')
            #quit()
        except:
            pass
