from selene import have, command
from selene.support.shared import browser


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('#genterWrapper')
        self.mobile = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.element('#hobbiesWrapper')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = browser.element('#submit')

    def open(self):
        browser.config.browser_name = 'firefox'
        browser.config.window_width = 1980
        browser.config.window_height = 1080
        browser.config.hold_browser_open = True
        browser.open('https://demoqa.com/automation-practice-form')
        browser.execute_script("document.querySelector('#fixedban').remove()")
        browser.execute_script("document.querySelector('footer').remove()")
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def fill_gender(self, value):
        self.gender.element_by(have.exact_text(value)).click()
        return self

    def fill_mobile(self, value):
        self.mobile.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, *subjects):
        for subject in subjects:
            self.subjects.type(subject).press_enter()
        return self

    def fill_hobbies(self, *hobbies):
        for hobby in hobbies:
            self.hobbies.element_by(have.exact_text(hobby)).click()
        return self

    def fill_picture(self, path):
        self.picture.upload_from(path)
        return self

    def fill_address(self, value):
        self.address.type(value)
        return self

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_city(self, name):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def should_have_registered(self, *values):
        browser.element('.table').all('td').even.should(have.exact_texts(*values))
        return self
