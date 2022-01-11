from Person import Person
import gspread

def read():
    sa = gspread.service_account(filename="service_account.json")
    sh = sa.open("Secret Santa List")

    wks = sh.worksheet("Sheet1")

    personList = []
    for x in range(2, wks.row_count+1):
        name = str(wks.cell(x, 1).value)
        family = str(wks.cell(x, 2).value)
        gifts = str(wks.cell(x, 3).value)
        phone = str(wks.cell(x, 4).value)

        person = Person(name, family, gifts, phone, None)
        personList.append(person)

    return personList