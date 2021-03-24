from selenium import webdriver
import requests
import threading
import time
import os


def initWebDriver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(executable_path='c:/chromedriver.exe', options=chrome_options)


def get_link(url):
    driver = initWebDriver()
    driver.get(url)
    time.sleep(3)
    list = []
    for i in range(1, 188):
        print("Grabing page {} links".format(i))
        divs = driver.find_elements_by_xpath('//div[@itemtype="schema.org/ImageObject"]/meta[1]')
        for div in divs:
            image_link = div.get_attribute('content')  # get default 510*340 px
            list.append(image_link)
        driver.implicitly_wait(3)

        driver.implicitly_wait(10)
        driver.find_element_by_xpath(
            "//body/div[@id='wrapper']/div[@id='content']/div[1]/a[1]").click()  # click next page
    return list


def download_img(url, n):
    r = requests.get(url)
    image_name = os.path.basename(url)
    dir = 'd:/download/'
    if not os.path.exists(dir):
        os.makedirs(dir)
    path = dir + str(image_name)
    with open(path, 'wb') as f:
        f.write(r.content)


def download_choice(pages=1, keyword=""):
    pages = input("how many pages do you want to download:")
    keyword = input("search for keyword:")


def main():
    url = "https://pixabay.com/zh/images/search/?order=ec&pagi=1"
    url_list = get_link(url)
    n = 1
    for url in url_list:
        print("Downloading page {}".format(n))
        n += 1
        t = threading.Thread(target=download_img, args=(url, n))
        t.start()


if __name__ == '__main__':
    main()

