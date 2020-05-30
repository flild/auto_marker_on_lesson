from selenium import webdriver
from config import password, login

import schedule
import time


def marker(driver):
    # click on button "Учеба"
    driver.find_element_by_xpath("/html/body/div[1]/div[10]/div/div/div/div[1]/div[1]/h5/div/font/nobr").click()

    # click on button "Расписание"
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[10]/div/div/div/div[1]/div[2]/div/div/ul/li[1]/span/nobr").click()
    time.sleep(1)


def job():
    driver = webdriver.Firefox(executable_path=r'C:\\Files\\geckodriver.exe')
    # <input id="users" title="Введите логин!" value="E-mail" name="users" onfocus="IndexKeyFocus(this);">
    # <input id="parole" title="Введите пароль!" type="password" value="..." name="parole" onfocus="IndexKeyFocus(this);">
    # <a onclick="open_zan(446885,39);">Начать занятие</a>
    driver.get("https://lk.sut.ru/cabinet/?login=yes")
    # driver.set_window_position(-3000, 0) 
    # driver.set_window_position(0, 0) to get it back
    # login
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/dl/dd[1]/input").send_keys(login)

    # password
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/dl/dd[2]/input").send_keys(password)

    # click on button "Войти"
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/dl/dd[3]/input").click()
    time.sleep(1)

    marker(driver)

    for i in range(5):
        try:
            driver.find_element_by_partial_link_text("Начать занятие").click()
            return
        except:
            print("Препода нет")
            driver.get("https://lk.sut.ru/cabinet/?login=yes")
            marker(driver)
            time.sleep(60)
    driver.quit()


if __name__ == '__main__':
    schedule.every().day.at("09:00").do(job)
    schedule.every().day.at("10:45").do(job)
    schedule.every().day.at("12:00").do(job)
    schedule.every().day.at("13:00").do(job)
    schedule.every().day.at("14:45").do(job)
    schedule.every().day.at("16:35").do(job)
    schedule.every().day.at("18:10").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)