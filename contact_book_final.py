# -*- coding: utf-8 -*-

import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        # enumerate() iterea y provee indice
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self, name):
        for contact in self._contacts:
            # Se busca contacto en el arreglo
            if contact.name.lower() == name.lower():
                self._print_contact(contact)

                # Se elimina el contacto encontrado
                for idx, contact in enumerate(self._contacts):
                    if contact.name.lower() == name.lower():
                        del self._contacts[idx]

                # Ingreso de datos nuevos
                print(' ')
                print('ACTUALIZAR DATOS')
                name = str(input('Nombre del contacto: '))
                phone = str(input('Telefono del contacto: '))
                email = str(input('Email del contacto: '))

                # Se guardan los datos nuevos
                contact = Contact(name, phone, email)
                self._contacts.append(contact)
                self._save()
                break
        else:
            # Muestra  mensaje si el contacto no fue encontrado
            self._not_found()

    def _save(self):
        with open('/content/100-contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('***************')
        print('No encontrado!')
        print('***************') 

def run():

    contact_book = ContactBook()

    with open('/content/100-contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            elif row == []:
                continue
            else:
                contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Nombre del contacto: '))
            phone = str(input('Telefono del contacto: '))
            email = str(input('Email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input('Nombre del contacto: '))

            contact_book.update(name)

        elif command == 'b':
            name = str(input('Nombre del contacto: '))

            contact_book.search(phone)

        elif command == 'e':
            name = str(input('Nombre del contacto: '))

            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()
