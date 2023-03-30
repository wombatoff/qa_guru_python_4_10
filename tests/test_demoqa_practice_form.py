from demoqa_tests.model.pages.registration_page import RegistrationPage
from demoqa_tests import resource


test_data = {
    'Name': 'Oleg',
    'Last Name': 'Greckiy',
    'Email': 'GreckiyOleg@gmail.com',
    'Gender': 'Male',
    'Mobile': '1234567890',
    'Day of Birth': '16',
    'Month of Birth': 'January',
    'Year of Birth': '1991',
    'Subjects': 'Maths',
    'Hobbies': 'Sports',
    'Picture': resource.path('foto.jpg'),
    'Address': '221B Baker Street',
    'State': 'NCR',
    'City': 'Delhi'
}


def test_filling_form():
    registration_page = RegistrationPage()
    registration_page.open()
    # \
    #     .fill_first_name(test_data['Name']) \
    #     .fill_last_name(test_data['Last Name']) \
    #     .fill_email(test_data['Email']) \
    #     .fill_gender(test_data['Gender']) \
    #     .fill_mobile(test_data['Mobile']) \
    #     .fill_date_of_birth(test_data['Year of Birth'],
    #                         test_data['Month of Birth'],
    #                         test_data['Day of Birth']) \
    #     .fill_subjects(test_data['Subjects']) \
    #     .fill_hobbies(test_data['Hobbies']) \
    #     .fill_picture(test_data['Picture']) \
    #     .fill_address(test_data['Address']) \
    #     .fill_state(test_data['State']) \
    #     .fill_city(test_data['City']) \
    #     .submit() \
    #     .should_have_registered(
    #         f"{test_data['Name']} {test_data['Last Name']}",
    #         test_data['Email'],
    #         test_data['Gender'],
    #         test_data['Mobile'],
    #         f"{test_data['Day of Birth']} {test_data['Month of Birth']},{test_data['Year of Birth']}",
    #         test_data['Subjects'],
    #         test_data['Hobbies'],
    #         test_data['Picture'],
    #         test_data['Address'],
    #         f"{test_data['State']} {test_data['City']}"
    #     )
