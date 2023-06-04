from dataclasses import dataclass


@dataclass
class CustomSelector:
    selector: str
    description: str


student_name_submitted: CustomSelector = CustomSelector(
    selector='//tbody/tr/td[text() = "Student Name"]/following-sibling::td',
    description='Ячейка со значением для Student Name в итоговой таблице'
)

student_email_submitted: CustomSelector = CustomSelector(
    selector='//tbody/tr/td[text() = "Student Email"]/following-sibling::td',
    description='Ячейка со значением для Student Email в итоговой таблице'
)

student_gender_submitted: CustomSelector = CustomSelector(
    selector='//tbody/tr/td[text() = "Gender"]/following-sibling::td',
    description='Ячейка со значением для Gender в итоговой таблице'
)

student_mobile_submitted: CustomSelector = CustomSelector(
    selector='//tbody/tr/td[text() = "Mobile"]/following-sibling::td',
    description='Ячейка со значением для Mobile в итоговой таблице'
)

student_date_of_birth_submitted: CustomSelector = CustomSelector(
    selector='//tbody/tr/td[text() = "Date of Birth"]/following-sibling::td',
    description='Ячейка со значением для Date of Birth в итоговой таблице'
)

student_subjects_submitted: CustomSelector = CustomSelector(
    selector='//tbody/tr/td[text() = "Subjects"]/following-sibling::td',
    description='Ячейка со значением для Subjects в итоговой таблице'
)

student_hobbies_submitted: CustomSelector = CustomSelector(
    selector='//tbody/tr/td[text() = "Hobbies"]/following-sibling::td',
    description='Ячейка со значением для Hobbies в итоговой таблице'
)

student_picture_submitted: CustomSelector = CustomSelector(
    selector='//tbody/tr/td[text() = "Picture"]/following-sibling::td',
    description='Ячейка со значением для Picture в итоговой таблице'
)

student_address_submitted: CustomSelector = CustomSelector(
    selector='//tbody/tr/td[text() = "Address"]/following-sibling::td',
    description='Ячейка со значением для Address в итоговой таблице'
)

student_state_and_city_submitted: CustomSelector = CustomSelector(
    selector='//tbody/tr/td[text() = "State and City"]/following-sibling::td',
    description='Ячейка со значением для State and City в итоговой таблице'
)
