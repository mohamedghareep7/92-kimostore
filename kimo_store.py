from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
driver = webdriver.Chrome()

all_products = []

for pages in range(1,3):
    driver.get(f"https://kimostore.net/collections/laptops?page={pages}")
    print("page :" , pages)

    container = driver.find_elements(By.XPATH , '//div[contains(@class , "grid__item")]')
    # print(container)

    for items in container:
        description = items.find_element(By.XPATH , './/div[@class="product-collection__title"]').text
        print("description :" , description)

        price = items.find_element(By.XPATH , './/span[@class="price"]').text
        print("price :" , price)

        try:
            rating = items.find_element(By.XPATH , './/div[@class="jdgm-prev-badge"]').get_attribute("data-average-rating")
            print("rating :" , rating)
        except:
            rating = "no rating found"
            print("rating :" , rating)


        try:
            reviews = items.find_element(By.XPATH , './/span[@class="jdgm-prev-badge__text"]').text
            print("reviews :" , reviews)
        except:
            reviews ="no reviews found"
            print("reviews :" , reviews)

        in_stock = items.find_element(By.XPATH , './/p[@class="in_stock"]').text
        print("available :" , in_stock)

        print("="*20)

        dict_products = {
            "description" : description ,
            "price" : price ,
            "rating" : rating ,
            "reviews" : reviews ,
            "in_stock" : in_stock ,
        }

        all_products.append(dict_products)

header = all_products[0].keys()
path = "all products.csv"
with open (path , "w" , encoding="utf-8" , newline="") as file:
    writer = csv.DictWriter(file , header)
    writer.writeheader()
    writer.writerows(all_products)

input("press enter to close :")
driver.quit()