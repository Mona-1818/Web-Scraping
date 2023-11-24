import os
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

workbook = openpyxl.Workbook()
sheet = workbook.active
row = ["Blog Title","Blog Date","Blog Image URL","Blog Likes Count"]
sheet.append(row)

os.environ['PATH'] += "E:"
driver = webdriver.Firefox()
driver.get("https://rategain.com/blog") 

def gather_info():
    Count = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/article/div/div[2]/div[3]/div/div/div/div[1]")
    tag_count = Count.find_elements(By.TAG_NAME, "article")
    for i in range(len(tag_count)):
        new_row = []
        path = "/html/body/div[1]/main/div/article/div/div[2]/div[3]/div/div/div/div[1]/article[{}]".format(i+1)
        main = driver.find_elements(By.XPATH,path)
        element=main[0]
        image_path = "div/div[1]/a"
        image = element.find_element(By.XPATH, image_path)
        value = image.get_attribute("href")
        try: 
            name_path = "div/div[2]/h6/a"
            name = element.find_element(By.XPATH, name_path).text
            date_path = "div/div[2]/div[1]/div[1]/span"
            date = element.find_element(By.XPATH, date_path).text
            like_path = "div/div[2]/a[2]/span"
            like_count = element.find_element(By.XPATH, like_path).text
            new_row.append(name,date,value,like_count)
            sheet.append(new_row)

        except:
            name_path = "div/div/h6/a"
            name = element.find_element(By.XPATH, name_path).text
            date_path = "div/div/div[1]/div[1]/span"
            date = element.find_element(By.XPATH, date_path).text
            like_path = "div/div/a[2]/span"
            like_count = element.find_element(By.XPATH, like_path).text
            new_row.append(name)
            new_row.append(date)
            new_row.append(value)
            new_row.append(like_count)
            sheet.append(new_row)
                     
        
gather_info()

page_count = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/article/div/div[2]/div[3]/div/div/div/div[2]")
num = page_count.find_elements(By.TAG_NAME, "a")
x = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/article/div/div[2]/div[3]/div/div/div/div[2]/a[{}]".format(len(num)-1)).text
for k in range(2, int(x)+1):
    driver.get("https://rategain.com/blog/page/{}/".format(k))
    gather_info()

workbook.save('<{path}>\webscrapping.xlsx')
driver.quit()
 
