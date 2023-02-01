"""sample test"""


from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """tetst the calc modules"""

    def test_add_numbers(self):
        res = calc.add(5,6
        )


        self.assertEqual(res, 11)



        


    def test_subtracting_numbers(self):
        """testing the subtraction of numbers"""
        res = calc.subtract(15,10)


        self.assertEqual(res, 5)


    

    