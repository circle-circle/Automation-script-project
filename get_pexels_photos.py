import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# Downloader for pexels.com

class search:

    photo_url = []
    browser = None
    chrome_opt = Options()

    def __init__(self, search="", page=1,browser='Chrome', delay=2):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.browser=webdriver.Chrome(executable_path='c:/chromedriver.exe', options=chrome_options)

        #self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.browser.get(f'https://www.pexels.com/search/')
        #self.browser.get(f'https://www.pexels.com/search/{search}/')
        time.sleep(delay)
        print('You are using pexels.com - Free stock photos')
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.browser.execute_script(js)
        while page < 100:
            self.browser.execute_script(js) 
            page+=1
        time.sleep(1)
        #Download directly through the home page without entering search keywords
        #result=self.browser.find_elements_by_xpath('//div[@class="photos"]/div[@class="photos__column"]/div[@class="hide-featured-badge hide-favorite-badge"]/article/a[1]') 
        
        #Download photos without videos from homepage
        result=self.browser.find_elements_by_xpath('//div[@class="photos"]/div[@class="photos__column"]/div[@class="hide-featured-badge hide-favorite-badge" and not(@data-track-action="videos")]/article/a[1]')  
        
        #Download directly through the home page with entering search keywords
        #result=self.browser.find_elements_by_xpath('//div[@class="search__grid"]/div[@class="photos"]/div[@class="photos__column"]/div[@class="hide-featured-badge hide-favorite-badge"]/article/a[1]')
        for url in result:
            photo=url.get_property('href')
            self.photo_url.append(photo)

    def download(self, delay=1):
        if self.photo_url.__len__() > 0:
            count = 0
            print(f'Looking for {self.photo_url.__len__()} Wallpapers')
            for url in self.photo_url:
                try:
                    print(url)
                    self.browser.get(url)
                    time.sleep(delay)
                    click_button = self.browser.find_element_by_class_name('rd__button--download')
                    #time.sleep(1)
                    click_button.click()
                    time.sleep(2)
                    count = count + 1
                except:
                    pass
            print(f'{count} photos downloaded')
        else:
            print('No photo found, slow internet connection may be')
            self.__del__()

    def __del__(self):
        try:
            self.browser.close()
            print('Completed')
            quit()
        except:
            pass

# with entering search keywords
#keyword="dog"
#for page in range(1,50):        
#    search(keyword,page).download() 
    
#without entering search keywords from homepage
search().download()      
