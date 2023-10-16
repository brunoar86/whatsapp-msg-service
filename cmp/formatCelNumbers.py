import pandas as pd

def earnData(xlsx_file):
    df = pd.read_excel(xlsx_file)
    return list(df['Contact'])

def toWhatsAppNumber(string):
    return ''.join(filter(str.isdigit, string))

def formatContactsList(contact_list):
    formattedContactList = []
    for contact in contact_list:
        if not isinstance(contact, str):
            continue
        contactString = toWhatsAppNumber(contact)
        if not contactString.startswith('55'):
            contactString = '55' + contactString
        if len(contactString) == 12:
            contactString = contactString[:5] + '9' + contactString[5:]
        formattedContactList.append('+' + contactString)
    return formattedContactList

def loadData(xlsx_file):
    contacts = formatContactsList(earnData(xlsx_file))
    with open('whatsAppNumbers.txt', 'w') as file:
        for number in contacts:
            file.write(number + '\n')
