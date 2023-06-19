import os

source = 'lesson_8/phonebook.txt'

# Чтение данных из файла
def readData(fileName):
    with open(fileName) as f:
        phoneBook = []
        for line in f:
            phoneBook.append(line.strip().split(','))
    return phoneBook

# Запись данных в файл
def writeData(fileName, phoneBook):
    with open(fileName, 'w') as f:
        for i in phoneBook:
            f.write(','.join(i) + '\n')

# Вывод информации о контакте
def printContact(contact):
    print("ID              :", contact[0])
    print("SURNAME         :", contact[1])
    print("FIRST_NAME      :", contact[2])
    print("SECOND_NAME     :", contact[3])
    print("TELEPHONE_NUMBER:", contact[4])
    print("")

# Поиск контакта по фамилии
def findPersonBySurname(phoneBook, surname):
    foundContacts = []
    for contact in phoneBook:
        if contact[1] == surname:
            foundContacts.append(contact)
    return foundContacts

# Поиск контакта по имени
def findPersonByName(phoneBook, name):
    foundContacts = []
    for contact in phoneBook:
        if contact[2] == name:
            foundContacts.append(contact)
    return foundContacts

# Показать все контакты
def selectAllReadPhoneNumber():
    phoneBook = readData(source)
    for contact in phoneBook:
        printContact(contact)

# Поиск контакта по номеру телефона
def selectSomethingReadPhoneNumber():
    phoneBook = readData(source)
    flag = False
    phoneNumber = input("Enter telephone number: ")
    for contact in phoneBook:
        if phoneNumber == contact[4]:
            printContact(contact)
            flag = True
    return flag

# Добавление контакта
def addPerson():
    phoneBook = readData(source)
    maxID = max(int(contact[0]) for contact in phoneBook) if phoneBook else 0
    print("Enter data:")
    number = str(maxID + 1)
    surname = input("Enter surname: ")
    nameFirst = input("Enter first name: ")
    nameSecond = input("Enter second name: ")
    phoneNumber = input("Enter telephone number: ")
    contact = [number, surname, nameFirst, nameSecond, phoneNumber]
    phoneBook.append(contact)
    writeData(source, phoneBook)

# Изменение контакта
def editPerson():
    phoneBook = readData(source)
    print("Edit data:")
    flag = selectSomethingReadPhoneNumber()
    if flag:
        print("Do you want to change the details of a person?")
        if input("[Y]es or [N]o: ").upper() == 'Y':
            print("Enter ID to edit person:")
            editID = input()
            for contact in phoneBook:
                if editID == contact[0]:
                    print("ATTENTION! EDIT PERSON MOD: ON")
                    printContact(contact)

                    oldSurName = contact[1]
                    oldFirstName = contact[2]
                    oldSecondName = contact[3]
                    oldPhoneNumber = contact[4]

                    print("Edit SURNAME?")
                    newSurName = input("[Y]es or [N]o: ").upper()
                    if newSurName == 'Y':
                        newSurName = input("Enter surname: ")
                    else:
                        newSurName = oldSurName

                    print("Edit FIRST_NAME?")
                    newFirstName = input("[Y]es or [N]o: ").upper()
                    if newFirstName == 'Y':
                        newFirstName = input("Enter first name: ")
                    else:
                        newFirstName = oldFirstName

                    print("Edit SECOND_NAME?")
                    newSecondName = input("[Y]es or [N]o: ").upper()
                    if newSecondName == 'Y':
                        newSecondName = input("Enter second name: ")
                    else:
                        newSecondName = oldSecondName

                    print("Edit TELEPHONE_NUMBER?")
                    newPhoneNumber = input("[Y]es or [N]o: ").upper()
                    if newPhoneNumber == 'Y':
                        newPhoneNumber = input("Enter telephone number: ")
                    else:
                        newPhoneNumber = oldPhoneNumber

                    print("ID              :", editID)
                    print("SURNAME         :", oldSurName, "==>", newSurName)
                    print("FIRST_NAME      :", oldFirstName, "==>", newFirstName)
                    print("SECOND_NAME     :", oldSecondName, "==>", newSecondName)
                    print("TELEPHONE_NUMBER:", oldPhoneNumber, "==>", newPhoneNumber)
                    print("Are you sure about these changes?")
                    if input("[Y]es or [N]o: ").upper() == 'Y':
                        contact[1] = newSurName
                        contact[2] = newFirstName
                        contact[3] = newSecondName
                        contact[4] = newPhoneNumber
                        writeData(source, phoneBook)
                        print("Data successfully edited and saved")
                    else:
                        print("Edit not saved")
        else:
            print("Edit canceled")
    return flag

# Удаление контакта
def deletePerson():
    phoneBook = readData(source)
    print("Delete data:")
    flag = selectSomethingReadPhoneNumber()
    if flag:
        print("Do you want to delete this person?")
        if input("[Y]es or [N]o: ").upper() == 'Y':
            print("Enter ID to delete person:")
            deleteID = input()
            for contact in phoneBook:
                if deleteID == contact[0]:
                    print("ATTENTION! DELETE PERSON MOD: ON")
                    printContact(contact)
                    print("Are you sure about deleting this person?")
                    if input("[Y]es or [N]o: ").upper() == 'Y':
                        phoneBook.remove(contact)
                        writeData(source, phoneBook)
                        print("Data successfully deleted. Changes saved")
                    else:
                        print("Delete not saved")
        else:
            print("Delete canceled")
    return flag

# Системные сообщения
def systemMessage(numberMSG):
    if numberMSG == 2:
        print("Found person finished")
    elif numberMSG == 3:
        print("Data successfully added and saved")
    elif numberMSG == 4:
        print("Data successfully edited and saved")
    elif numberMSG == 5:
        print("Data successfully deleted. Changes saved")
    elif numberMSG == 0:
        print("GOODBYE! COME AGAIN!")
    else:
        print("Something ERROR. Please contact the developers")

clear = lambda: os.system('cls')
clear()

print('''HELLO, USER
        \n [1] -- press for SHOW ALL
        \n [2] -- press for SELECT
        \n [3] -- press for ADD DATA
        \n [4] -- press for EDIT DATA
        \n [5] -- press for DELETE DATA
        \n [0] -- press for EXIT
        ''')
while True:
    number = int(input("Enter number: "))
    if number == 1:
        print("WORKING SELECT *:")
        selectAllReadPhoneNumber()
        print("Select all finished")
    elif number == 2:
        print("WORKING SELECT SOMETHING:")
        selectSomethingReadPhoneNumber()
        systemMessage(number)
    elif number == 3:
        print("WORKING ADD:")
        addPerson()
        systemMessage(number)
    elif number == 4:
        print("WORKING EDIT:")
        editPerson()
        systemMessage(number)
    elif number == 5:
        print("WORKING DELETE:")
        deletePerson()
        systemMessage(number)
    elif number == 0:
        systemMessage(number)
        break
    else:
        systemMessage(99)