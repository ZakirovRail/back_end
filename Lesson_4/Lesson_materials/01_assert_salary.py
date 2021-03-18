"""
Фамилия     Имя         Часов   Ставка
Иванов      Иван        45      400
Дакукин     Филимон     20      1000
Ромашкин    Сидар       45      500
"""


from collections import namedtuple
import datetime

Salary = namedtuple('Salary', ('surname', 'name', 'worked', 'rate'))


def get_salary(line):
    line = line.split()
    if line:
        data = Salary(*line)
        fio = ' '.join((data.surname, data.name))
        salary = int(data.worked) * int(data.rate)
        res = (fio, salary)
    else:
        res = ()
    return res


def test_get_salary_summ():
    assert get_salary('Лютиков Руслан 60 1000') == \
           ('Лютиков Руслан', 60000), 'Не верная сумма'


def test_get_salary_fio():
    assert get_salary('Лютиков Руслан 60 1000')[0] == 'Лютиков Руслан', 'Не верное имя'


def test_get_salary_empty():
    assert get_salary('') == (), 'Not empty data'


def test_get_salary_wrong_format():
    assert get_salary(' ') == (), 'Not empty data'


if __name__ == '__main__':
    test_get_salary_summ()
    test_get_salary_fio()
    test_get_salary_empty()
    test_get_salary_wrong_format()
