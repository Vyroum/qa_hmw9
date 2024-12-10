from selene import browser, be, by, have
from Data_sources import resources


class PracticeFormPage:
    def __init__(self):
        self.first_name = browser.element('[id="firstName"]')
        self.last_name = browser.element('[id="lastName"]')
        self.email = browser.element('[id="userEmail"]')
        self.user_number = browser.element('[id="userNumber"]')
        self.address = browser.element('[id="currentAddress"]')

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def select_gender(self, value):
        self.user_gender = browser.element(by.text(value))

    def fill_user_number(self, value):
        self.user_number.type(value)

    def pick_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element("[class='react-datepicker__year-select']").click().element(by.text(f"{year}")).click()
        browser.element("[class='react-datepicker__month-select']").click().element(by.text(f"{month}")).click()
        browser.element(by.text(f"{day}")).click()

    def choose_interest_sport(self):
        browser.element(by.text("Sports")).click()

    def choose_interest_music(self):
        browser.element(by.text("Music")).click()

    def choose_interest_reading(self):
        browser.element(by.text("Reading")).click()

    def upload_picture(self, value):
        browser.element('#uploadPicture').set_value(resources.path(value))

    def choose_state(self, value):
        browser.element('[id="state"]').click()
        browser.element(by.text(value)).click()

    def choose_city(self, value):
        browser.element('[id="city"]').click()
        browser.element(by.text(value)).click()

    def fill_address(self, value):
        self.address.type(value)
