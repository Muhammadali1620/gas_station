import re

from rest_framework.exceptions import ValidationError


def validate_car_number(car_number: str) -> None:
    pattern = r'^[(01)|(10)|(20)|(25)|(30)|(40)|(50)|(60)|(70)|(75)|(80)|(90)|(95)]\s\d{3}\s{2}$'
    if not re.search(pattern, car_number):
        raise ValidationError('Invalid Number: {}'.format(car_number))