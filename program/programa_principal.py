from class_contact import Contact
from class_contactBook import ContactBook

contato_agenda = ContactBook()

while True:
    print('--- Opções agenda de contatos ---')
    print('1. Adicionar contato')
    print('2. Remover contato')
    print('3. Listar contatos')
    print('4. Buscar contato')
    print('5. Atualizar contato')
    print('6. Sair')

    choice = input('Ecolha a opção: ')

    if choice == '1':
        name = input('Digite o nome: ')
        phone = input('Digite o número: ')
        email = input('Digite o e-mail: ')

        contact = Contact(name, phone, email)
        contato_agenda.add_contact(contact)
        print('Contato adicionado!')
    elif choice == '2':
        name = input('Digite o nome do contato a ser excluído: ')
        contato_agenda.remove_contact(name)
    elif choice == '3':
        contato_agenda.contacts_list()
    elif choice == '4':
        name = input('Digite o nome do contato que quer buscar: ')
        contato_agenda.search(name)
    elif choice == '5':
        name  = input('Digite o nome do contato que quer atulizar: ')
        contato_agenda.update_contact(name)
    elif choice == '6':
        break
    else:
        print('Digite uma opção válida do menu: ')