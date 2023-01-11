"""Тобі необхідно написати функцію котра буде виконувати наступне.
 Приймати список, а повертати список значень тієї самої довжини на першому місці сумма всіх значень мінус перше значення.
 На другому суму всіх вхідних значеннь і мінус друге значення.
 """


def sum_minus_list(): pass


assert sum_minus_list([1, 2, 3] == [4, 3, 2])

# підсказка list comp, але спершу цикл

"""
    Задача 2
    у вас текст треба написати функцію котра буде приймати його а другим аргументом слово Виконавець. Як що воно є повертаємо сфоромований рядок
    titles (всі назви платівок де грав актор) Price sum (сумма всіх платівок де він грав.)
"""

cd_catalog = """<CATALOG><CD><TITLE>Empire Burlesque</TITLE><ARTIST>Bob Dylan</ARTIST><COUNTRY>USA</COUNTRY><COMPANY>Columbia</COMPANY><PRICE>10.90</PRICE><YEAR>1985</YEAR></CD>
<CATALOG><CD><TITLE>Bla bla</TITLE><ARTIST>Bob Dylan</ARTIST><COUNTRY>USA</COUNTRY><COMPANY>Columbia</COMPANY><PRICE>10.90</PRICE><YEAR>1985</YEAR></CD>
<CD><TITLE>Hide your heart</TITLE><ARTIST>Bonnie Tyler</ARTIST><COUNTRY>UK</COUNTRY><COMPANY>CBS Records</COMPANY><PRICE>9.90</PRICE><YEAR>1988</YEAR></CD>
<CD><TITLE>Greatest Hits</TITLE><ARTIST>Dolly Parton</ARTIST><COUNTRY>USA</COUNTRY><COMPANY>RCA</COMPANY><PRICE>9.90</PRICE><YEAR>1982</YEAR></CD>
</CATALOG>"""
artist = 'Bob Dylan'
def actor_sum(cd_catalog, artist): pass


assert actor_sum(cd_catalog, artist) == "Titles: Empire Burlesque, Bla bla \n Artist: Bob Dylan \n Price Sum 21.8"

# підсказка вирішуй це на як xml та звичайно іншими способами.