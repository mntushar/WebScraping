import time
from datetime import datetime

from selenium.webdriver.common.by import By

from Handler.Handler import *

handler: Handler
driver: any
field_title = ['Date-time scraper run',
               'URL',
               'Company name',
               'Last updated',
               'Business establishment',
               'Location',
               'Fiscal code',
               'Legal form',
               'Internet site',
               'NACE Code',
               'Sector',
               'Legal representative',
               'Number of Employees Range',
               'email',
               'company linkedin profile',
               'Presentation',
               'Competitors']


def main_page():
    driver.get("https://startup.registroimprese.it/isin/home#")

    time.sleep(10)

    advance_search_element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/div/div/div["
                                                           "2]/form/div[4]/a")
    if advance_search_element:
        advance_search_element.click()

    region = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/div/div/div[2]/form/div["
                                           "5]/div/div[2]/div/div[1]/div/div/div/div[2]/div[1]")
    if region:
        driver.execute_script("arguments[0].click();", region)

    search_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/div/div/div[2]/form/div["
                                                  "7]/a")
    if search_button:
        driver.execute_script("arguments[0].click();", search_button)


def search_data(is_main: bool):
    try:
        time.sleep(10)

        current_url = driver.current_url
        next_page_url = ''

        next_element = driver.find_element(By.XPATH,
                                           "/html/body/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div/a[3]")
        if next_element:
            next_page_url = next_element.get_attribute('href')

        for count in range(0, 9):
            datas = driver.find_elements(By.ID, "searchResults")
            if not datas:
                return
            element = datas[count].find_element(By.ID,
                                                "title")
            if element:
                element_tag = element.find_element(By.TAG_NAME, "a")
                if element_tag:
                    driver.execute_script("arguments[0].click();", element_tag)
                    data_detail(driver.current_url)

            if is_main:
                driver.get(current_url)
            else:
                driver.get(next_page_url)

        time.sleep(10)

        search_data(False)
    except Exception as e:
        print(e)


def data_detail(url: str):
    time.sleep(10)

    data = {'Date-time scraper run': datetime.now(), 'URL': url, 'Company name': '', 'Last updated': '',
            'Business establishment': '', 'Location': '', 'Fiscal code': '', 'Legal form': '', 'Internet site': '',
            'NACE Code': '', 'Sector': '', 'Legal representative': '', 'Number of Employees Range': '', 'email': '',
            'company linkedin profile': '', 'Presentation': '', 'Competitors': ''}

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div['
                                           '1]/div[2]/div[2]/b/span'):
        company_name = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div['
                                           '1]/div[2]/div[2]/b/span')
        if company_name:
            data['Company name'] = company_name.text

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div['
                                           '1]/div[1]/div[2]'):
        last_updated = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div['
                                           '1]/div[1]/div[2]')
        if last_updated:
            date_text = last_updated.text
            data['Last updated'] = date_text.split("\n")[-1].strip()

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/span'):
        business_establishment = driver.find_element(By.XPATH,
                                                     '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/span')
        if business_establishment:
            data['Business establishment'] = business_establishment.text

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[4]/span'):
        location = driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[4]/span')
        if location:
            data['Location'] = location.text

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[6]/span'):
        fiscal_code = driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[6]/span')
        if fiscal_code:
            data['Fiscal code'] = fiscal_code.text

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[8]/span'):
        legal_form = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[8]/span')
        if legal_form:
            data['Legal form'] = legal_form.text

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[12]/a'):
        internet_site = driver.find_element(By.XPATH,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[12]/a')
        if internet_site:
            data['Internet site'] = internet_site.text

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[14]/b/span'):
        nace_Code = driver.find_element(By.XPATH,
                                        '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[14]/b/span')
        if nace_Code:
            data['NACE Code'] = nace_Code.text

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[16]/span'):
        sector = driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[16]/span')
        if sector:
            data['Sector'] = sector.text

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[4]/div/div/div[2]/h3/span'):
        legal_representative = driver.find_element(By.XPATH,
                                                   '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[4]/div/div/div[2]/h3/span')
        if legal_representative:
            text = legal_representative.text
            rep_index = text.find("representative") + len("representative")
            on_index = text.find("on")
            data['Legal representative'] = text[rep_index:on_index].strip()

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span'):
        number_of_employees_range = driver.find_element(By.XPATH,
                                                        '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span')
        if number_of_employees_range:
            data['Number of Employees Range'] = number_of_employees_range.text

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[4]/div/div/div[3]/div/div[1]/div[2]/a'):
        email = driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[4]/div/div/div[3]/div/div[1]/div[2]/a')
        if email:
            data['email'] = email.text

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[4]/div/div/div[3]/div/div[1]/div[1]'):
        company_linkedin_profile = driver.find_element(By.XPATH,
                                                       '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[4]/div/div/div[3]/div/div[1]/div[1]')
        if company_linkedin_profile:
            a_tag = company_linkedin_profile.find_elements(By.TAG_NAME, 'a')
            if len(a_tag) > 2:
                data['company linkedin profile'] = a_tag[2].get_attribute('href')

    if handler.scarping_handler.check_xpath(driver,
                                            '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[7]/div/div[2]'):
        presentation = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[7]/div/div[2]')
        if presentation:
            data['Presentation'] = presentation.text

    if handler.scarping_handler.check_xpath(driver, '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[12]/div/div[2]'):
        competitors = driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[12]/div/div[2]')
        if competitors:
            data['Competitors'] = competitors.text

    handler.file_handler.append_data_csv('startup_registroimprese',
                                         data,
                                         field_title)


if __name__ == '__main__':
    handler = Handler()
    driver = handler.scarping_handler.selenium_create()

    main_page()
    search_data(True)

    time.sleep(1000)
    driver.close()
