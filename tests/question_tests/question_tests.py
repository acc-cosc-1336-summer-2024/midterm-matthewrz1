#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_a.question_a import get_assessment_value
from src.question_a.question_a import get_tax_assessed
from src.question_b.question_b import get_bonus_pay
from src.question_c.question_c import reverse_string
from src.question_d.question_d import is_prime

class Test_Config(unittest.TestCase):

    #question a
    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_question_a_get_assessment_value(self):
        self.assertEqual(6000,get_assessment_value(10000))
        self.assertEqual(12000, get_assessment_value(20000))

    def test_question_a_get_tax_assessed(self):
        self.assertEqual(43.20, get_tax_assessed(6000))
        self.assertEqual(72, get_tax_assessed(10000))
        
    #question b
    def test_question_b_get_bonus_pay(self):
        self.assertEqual("Invalid arguments", get_bonus_pay(-1))
        self.assertEqual(10, get_bonus_pay(200))
        self.assertEqual(36, get_bonus_pay(600))
        self.assertEqual(70, get_bonus_pay(1000))
        self.assertEqual(120, get_bonus_pay(1500))
        self.assertEqual("Invalid arguments", get_bonus_pay(2000))
    
    #question c
    def test_question_c_reverse_string(self):
        self.assertEqual("dlrow olleh", reverse_string("hello world"))

    #question d
    def test_question_d_is_prime(self):
        self.assertEqual(False, is_prime(4))
        self.assertEqual(True, is_prime(11))


