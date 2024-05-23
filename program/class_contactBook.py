import sqlite3

class ContactBook:
    def __init__(self):
        pass


    def add_contact(self, contact):
        connection = sqlite3.connect('agenda.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO contatos (name, number, email)
            VALUES (?, ?, ?)
                    ''', (contact.name, contact.number, contact.email))
        connection.commit()
        connection.close()


    def contacts_list(self):
        print('>> Lista de contatos <<')
        connection = sqlite3.connect('agenda.db')
        cursor = connection.cursor()
        for row in cursor.execute('SELECT * FROM contatos'):
            print(f'{row[0]} - Nome: {row[1]} - Nº: {row[2]} - E-mail: {row[3]}')
        connection.close()


    def search(self, name):
        connection = sqlite3.connect('agenda.db')
        cursor = connection.cursor()
        contacts_found = []

        stop = False

        while stop is False:
            for row in cursor.execute('SELECT * FROM contatos'):
                if name.upper() in row[1].upper():
                    contacts_found.append(row)
            print('>> Contatos encontrados abaixo <<')

            if len(contacts_found) > 0:
                for c in contacts_found:
                    print(f'{c[0]} - Nome: {c[1]} - Nº: {c[2]} - E-mail: {c[3]}')
            else:
                print('A busca não retornou resultados.')

            while True:
                check = input('Deseja buscar outro contato?(s/n)').upper().strip()
                if check[0] in 'SN':
                    break
                else:
                    print('Digite apenas S ou N.')
            if check in 'S':
                name = input('Digite o nome: ')
            else:
                stop = True

        connection.close()
        return contacts_found


    def remove_contact(self, name):

        print('>> Excluir contatos <<')

        contacts_found = []
        contacts_found = self.search(name)

        if len(contacts_found) > 0:
            stop = False
            while stop is False:
                try:
                    if len(contacts_found) > 1:
                        option = int(input('Digite o nº da opção do contato que deseja excluir: '))
                    else:
                        option = contacts_found[0][0]
                except:
                    print('Por favor, digite somente números inteiros.')
                else:
                    for c in contacts_found:
                        if option == c[0]:
                            while True:
                                check = input(f'Deseja mesmo excluir {c}? (s/n)').upper().strip()
                                if check[0] in 'SN':
                                    stop = True
                                    break
                                else:
                                    print('Digite apenas S ou N')

                            if check[0] in 'S':
                                connection = sqlite3.connect('agenda.db')
                                cursor = connection.cursor()
                                cursor.execute('''
                                                DELETE FROM contatos
                                                WHERE id = ?
                                                ''', (option,))
                                connection.commit()
                                connection.close()
                                print('Contato excluído com sucesso!')
                            if stop is True:
                                break
                    if stop is False:
                        print('Por favor, digite uma opção válida da lista!')
        else:
            print('Por favor, tente novamente e pesquise um contato existente.')


    def update_contact(self, name):

        print('>> Atualizar contatos <<')

        contacts_found = []
        contacts_found = self.search(name)

        if len(contacts_found) > 0:
            stop = False
            while stop is False:
                try:
                    if len(contacts_found) > 1:
                        id = int(input('Digite o nº da opção do contato que deseja atualizar: '))
                    else:
                        id = contacts_found[0][0]
                except:
                    print('Por favor, digite somente números inteiros.')
                else:
                    for c in contacts_found:
                        if id == c[0]:
                            while True:
                                check = input(f'Deseja mesmo atulizar {c}? (s/n)').upper().strip()
                                if check[0] in 'SN':
                                    stop = True
                                    break
                                else:
                                    print('Digite apenas S ou N')

                            if check[0] in 'S':
                                name = str(input('Digite o novo nome: '))
                                number = int(input('Novo número: '))
                                email = str(input('Novo e-mail: '))
                                connection = sqlite3.connect('agenda.db')
                                cursor = connection.cursor()
                                cursor.execute('''
                                                        UPDATE contatos set name = ?, number = ?, email = ?
                                                        WHERE id = ?
                                                        ''', (name, number, email, id))
                                connection.commit()
                                connection.close()
                                print('Contato atualizado com sucesso!')
                            if stop is True:
                                break
                    if stop is False:
                        print('Por favor, digite uma opção válida da lista!')
        else:
            print('Por favor, tente novamente e pesquise um contato existente.')
