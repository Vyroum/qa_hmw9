import os

from selene import browser, have

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
    practice_form_page.fill_subject("Maths")
    practice_form_page.choose_interest_sport()
    practice_form_page.choose_interest_music()
    practice_form_page.choose_interest_reading()
    practice_form_page.upload_picture("image.jpg")
    practice_form_page.choose_state("NCR")
    practice_form_page.choose_city("Noida")
    practice_form_page.submit_button()

    practice_form_page.should_registered_user_with(
        "Andrei Monichev",
        "testmail@test.ru",
        "Male",
        "1231231234",
        "13 September,1995",
        "Maths",
        "Sports, Music, Reading",
        "image.jpg",
        "City Name, Street Name",
        "NCR Noida"
    )


