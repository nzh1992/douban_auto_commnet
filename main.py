import time

from selenium import webdriver

if __name__ == '__main__':
    url = "https://www.douban.com/group/topic/227049694/?dt_dapp=1"

    driver = webdriver.Chrome()
    driver.get(url)

    house_login_button = driver.find_element_by_link_text("登录/注册")
    house_login_button.click()

    # choose username and password login
    choose_button = driver.find_element_by_class_name("account-tab-account")
    choose_button.click()

    # login
    user_account = "19921061992"
    user_password = "a1992662007"
    user_account_input = driver.find_element_by_id("username")
    user_account_input.send_keys(user_account)
    user_password_input = driver.find_element_by_id("password")
    user_password_input.send_keys(user_password)
    login_button = driver.find_element_by_class_name("account-form-field-submit")
    login_button.click()

    # 模拟网络延迟
    time.sleep(3)

    # 是否弹出验证滑块
    pass

    # 滑块验证码
    iframe_xpath = '//*[@id="tcaptcha_iframe"]'
    iframe = driver.find_element_by_xpath(iframe_xpath)

    driver.switch_to.frame(iframe)

    time.sleep(2)
    slide_block = driver.find_element_by_id("tcaptcha_drag_thumb")

    webdriver.ActionChains(driver).click_and_hold(slide_block).perform()
    webdriver.ActionChains(driver).move_by_offset(xoffset=200, yoffset=0).perform()
    webdriver.ActionChains(driver).release().perform()

    # 等待页面跳转
    time.sleep(2)

    # 新增一条评论
    driver.switch_to.parent_frame()
    driver.find_element_by_id("last").send_keys("hello")
    driver.find_element_by_name("submit_btn").click()

    print("process done.")
