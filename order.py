from selenium import webdriver
import time
import os
import click

def page_mapping(driver):
    page = ""
    title = driver.find_element_by_tag_name("title").get_attribute('innerHTML')
    if "amazon.com: online shopping" in title.lower():
        if "sign in" in driver.find_elements_by_class_name("nav-line-1")[0].text.lower():
            page = "home"
        else:
            page = "readytocart"
    elif title.lower() == "amazon sign-in":
        page = "sigin"
    elif title.lower() == "amazon.com shopping cart":
        page = "checkout"
    elif title.lower() == "before you checkout":
        page = "beforecheckout"
    elif title.lower() == "substitution preferences":
        page = "subsitem"
    elif "reserve a time slot" in title.lower():
        page = "timeslot"
    elif "edit quantities" in title.lower():
        page = "editquantity"
    else:
        print("No Page found: " + title)
        page = ""
    print("Current Page: " + page)
    return page


def home_page(driver):
    driver.get("https://amazon.com")
    print("PageLoaded")
    return driver


def sign_in(driver, user, password):
    driver.get("https://amazon.com")
    print("PageLoaded")
    driver.find_element_by_id("nav-link-accountList").click()
    driver.find_element_by_id("ap_email").send_keys(user)
    driver.find_element_by_id("continue").click()
    driver.find_element_by_id("ap_password").send_keys(password)
    driver.find_element_by_id("signInSubmit").click()
    print("SignInSuccessful")
    return driver


def checkout_wholefoods_cart(driver):
    driver.find_element_by_id("nav-cart").click()
    buttons = list(
        filter(lambda d: d.get_attribute("value") == "Proceed to checkout", driver.find_elements_by_tag_name("input")))
    buttons[0].click()
    print("ContinueCheckoutSuccessful")
    return driver


def before_you_checkout(driver):
    buttons = list(
        filter(lambda d: d.get_attribute("name") == "proceedToCheckout", driver.find_elements_by_tag_name("a")))
    buttons[0].click()
    print("BeforeYouCheckout Successful")
    return driver


def substitute_preferences(driver):
    buttons = list(
        filter(lambda d: d.get_attribute("data-action") == "doNotSubItem",
               driver.find_elements_by_tag_name("span")))
    for button in buttons:
        if not button.find_element_by_tag_name("input").is_selected():
            button.find_element_by_tag_name("i").click()
    print("DoNotSubstituteSuccessful")
    buttons = list(
        filter(lambda d: d.get_attribute("aria-labelledby") == "subsContinueButton-announce",
               driver.find_elements_by_tag_name("input")))
    buttons[0].click()
    return driver


def select_timeslot(driver):
    #driver.find_elements_by_class_name("ufss-slot-toggle-native-button")[0].click()
    search_slot = True
    while search_slot:
        slots = driver.find_elements_by_class_name("ufss-slot-toggle-native-button")
        if len(slots) > 0:
            print("Slot found")
            driver.find_elements_by_class_name("ufss-slot-toggle-native-button")[0].click()
            search_slot = False
        else:
            print("Slot not found...waiting for next one to show up")
            time.sleep(10)
            driver.refresh()
    return driver


def edit_quantities(driver):
    page = page_mapping(driver)
    print(page)
    if page == "editquantity":
        buttons = list(
            filter(lambda d: d.get_attribute("name") == "continue-bottom", driver.find_elements_by_tag_name("input")))
        buttons[0].click()
    return driver


def confirm_timeslot(driver):
    driver.find_elements_by_class_name("a-button-input")[0].click()
    print("Confirmed Time Slot")
    return driver


def review_order(driver):
    driver.find_element_by_id('continue-top').click()
    print("Order Reviewed")
    return driver


def place_order(driver, test):
    if test.lower() == "n":
        print("Placing Order")
        driver.find_elements_by_class_name("place-your-order-button")[0].click()
    else:
        print("This is test run, no order placed")
    print("Order Placed")
    return driver


def main(username, password, test):
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver = home_page(driver)
        driver = sign_in(driver, username, password)
        driver = checkout_wholefoods_cart(driver)
        driver = before_you_checkout(driver)
        driver = substitute_preferences(driver)
        time.sleep(10)
        driver = edit_quantities(driver)
        time.sleep(5)
        driver = select_timeslot(driver)
        time.sleep(10)
        driver = confirm_timeslot(driver)
        time.sleep(5)
        driver = review_order(driver)
        time.sleep(5)
        driver = place_order(driver, test)
        time.sleep(10)
        return True
    except Exception as e:
        print(str(e))
        return False
    finally:
        driver.close()
        driver.quit()


@click.command()
@click.option('-u', '--username', prompt='Amazon.com SignIn Username', help='Amazon.com SignIn Username')
@click.option('-p', '--password', prompt='Amazon.com SignIn Password', help='Amazon.com SignIn Password',
                       hide_input=True)
@click.option('-t', '--test', default='n', type=click.Choice(["y", 'n']))
def order(username, password, test):
    """Program to place order in whole foods automatically from existing cart"""
    while not main(username, password, test.upper()):
        main(username, password, test)


if __name__ == "__main__":
    order()
