from selene import browser, be, by, have
from data_sources import resources
from data_sources import user_data
from data_sources.user_data import user_for_registration


class PracticeFormPage:

    def register_user(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        browser.element('[id="firstName"]').type(first_name)
        browser.element('[id="lastName"]').type(user_for_registration.last_name)
        browser.element('[id="userEmail"]').type(user_for_registration.last_name)
        self.user_number = browser.element('[id="userNumber"]')
        self.address = browser.element('[id="currentAddress"]')
        self.subject = browser.element("#subjectsInput")

        first_name.type(User.first_name)
        self.last_name.type(value)
        self.email.type(value)
        browser.element(by.text(value)).click()
        self.user_number.type(value)
        browser.element("#dateOfBirthInput").click()
        browser.element("[class='react-datepicker__year-select']").click().element(by.text(f"{year}")).click()
        browser.element("[class='react-datepicker__month-select']").click().element(by.text(f"{month}")).click()
        browser.element(by.text(f"{day}")).click()
        self.subject.type(value).press_enter()
        browser.element(by.text("Sports")).click()
        browser.element(by.text("Music")).click()
        browser.element(by.text("Reading")).click()
        browser.element('#uploadPicture').set_value(resources.path(value))
        browser.element('[id="state"]').click()
        browser.element(by.text(value)).click()
        browser.element('[id="city"]').click()
        browser.element(by.text(value)).click()
        self.address.type(value)
        browser.element('[id="submit"]').click()
    def should_registered_user_with(self, full_name, email, gender, user_number, birthdate, subjects, hobby, file,
                                    address, location):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                user_number,
                birthdate,
                subjects,
                hobby,
                file,
                address,
                location,
            )
        )
