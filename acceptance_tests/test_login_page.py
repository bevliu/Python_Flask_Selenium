from selenium import webdriver

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-infobars')
driver = webdriver.Chrome(chrome_options=chrome_options)

# click on login

def test_login_function():
    with webdriver.Chrome() as driver:
        # webdriver load url
        try:
            driver.get('http://127.0.0.1:5000/login')
            login_element = driver.find_element_by_xpath('//*[@id="navbarToggle"]/div[2]/a[1]')
                # element.click
            login_element.click()
                # fill out email field
            email = driver.find_element_by_id('email')

                # fill out password field
            password = driver.find_element_by_id("password")
                # click on login button
            login_botton_element = driver.find_element_by_xpath('//*[@id="submit"]')
            login_botton_element.click()
                # check page is at home url
            home_url = driver.current_url
            return True
        except:
            return False

print('Home Page: {}'.format(test_login_function()))