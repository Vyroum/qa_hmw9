import os

from selene import browser, be, have, by

from Pages.practice_form_page import PracticeFormPage


def test_practice_form():
    practice_form_page = PracticeFormPage()
    practice_form_page.open()

    practice_form_page.fill_first_name("Andrei")
    practice_form_page.fill_last_name("Monichev")

    practice_form_page.fill_email("testmail@test.ru")
    practice_form_page.select_gender("Male")

    practice_form_page.fill_user_number("1231231234")

    practice_form_page.pick_date_of_birth("1995", "September", "13")

    browser.element("#subjectsInput").type('Maths').press_enter().type("Arts").press_enter().type(
        "Computer Science").press_enter()

    practice_form_page.choose_interest_sport()
    practice_form_page.choose_interest_music()
    practice_form_page.choose_interest_reading()

    practice_form_page.upload_picture("image.jpg")


    practice_form_page.choose_state("NCR")
    practice_form_page.choose_city("Noida")

    browser.element('[id="submit"]').click()
    browser.element(".modal-body").should(have.text("Andrei Monichev"))
    browser.element(".modal-body").should(have.text("testmail@test.ru"))
    browser.element(".modal-body").should(have.text("Male"))
    browser.element(".modal-body").should(have.text("1231231234"))
    browser.element(".modal-body").should(have.text("13 September,1995"))
    browser.element(".modal-body").should(have.text("Maths, Arts, Computer Science"))
    browser.element(".modal-body").should(have.text("Sports, Music, Reading"))
    browser.element(".modal-body").should(have.text("image.jpg"))
    browser.element(".modal-body").should(have.text("City Name, Street Name"))
    browser.element(".modal-body").should(have.text("NCR Noida"))
