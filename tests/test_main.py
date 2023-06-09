from unittest import TestCase
import pytest
from main import remove_some_country, get_unic_values

class Test_unittest_geo_logs(TestCase):
    def test_positive_country(self):
        x = 'Россия'
        result = remove_some_country(x)
        expected = [
        {'visit1': ['Москва', 'Россия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
        ]
        self.assertListEqual(list(result), expected)


# class Test_pytest_geo_logs:
#
#     @pytest.mark.parametrize(
#         "param, expected",
#         (
#                 ('Россия', [
#                     {'visit1': ['Москва', 'Россия']},
#                     {'visit3': ['Владимир', 'Россия']},
#                     {'visit7': ['Тула', 'Россия']},
#                     {'visit8': ['Тула', 'Россия']},
#                     {'visit9': ['Курск', 'Россия']},
#                     {'visit10': ['Архангельск', 'Россия']}
#                 ]),
#                 ('Индия', [
#                     {'visit2': ['Дели', 'Индия']}])
#         )
#     )
#     def test_with_params(self, param, expected):
#         result = remove_some_country(param)
#         assert result == expected

class Test_unittest_geo_id(TestCase):
    def test_unic_values(self):
        expected = [213, 15, 54, 119, 98, 35]
        result = get_unic_values()
        self.assertListEqual(result, expected)
