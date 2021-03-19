import unittest
from collections import namedtuple

Salary = namedtuple('Salary', ('surname', 'name', 'worked', 'rate'))


def get_salary(line):
    '''
    Calculation of employee's salary
    '''

    line = line.split()
    if line:
        data = Salary(*line)
        fio = ' '.join((data.surname, data.name))
        salary = int(data.worked) * int(data.rate)
        res = (fio, salary)

    else:
        res = ()
    return res


class SalaryTestCase(unittest.TestCase):
    name = 'Ruslan'
    surname = 'Lutikov'
    worked = 60
    rate = 900

    def setUp(self):
        self.result = get_salary(f'{self.surname} {self.name} {self.worked} {self.rate}')

    def test_get_salary_sum(self):
        self.assertEqual(self.result[1], self.worked * self.rate)

    def test_get_salary_fio(self):
        self.assertEqual(self.result[0], f'{self.surname} {self.name}')

    def test_get_salary_empty(self):
        self.assertEqual(get_salary(''), ())


if __name__ == '__name__':
    unittest.main()



