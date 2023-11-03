def input_error(func): 
    def wrapper(*args, **kwargs):
        try :
            return func(*args, **kwargs)
        except KeyError:
            return 'Enter your name'
        except ValueError:
            return 'Give me name and phone please, or i will teach your kids to smoke'
        except IndexError:
            return 'I hate you. You really can`t remember the format of the appeal? Command name phone. You better make no mistake, because ... hehe'
    return wrapper 

phonebook = {}

@input_error
def hello():
    print ('Hello. I am angry bot. I can help you, but if you`re annoying, I`ll accidentally send everyone your browser history')

def add_contact(*args):
    name = args[0]
    phone = args[1]
    phonebook[name] = phone
    print(phonebook)
    return'Okay, I remembered this contact. But I don`t understand why, you don`t have any friends anyway'

def change_contact(*args):
    name = args[0]
    new_phone = args[1]
    fone = phonebook[name]
    if fone:
        phonebook[name] = new_phone
        print(phonebook)
        return'I changed the number for this person. I don`t like people who often change their phone'

def find_phone(*args):
    name = args[0]
    return f'{phonebook.get(name)}, do you want to call him? It is unlikely that he will answer... you'

def show_all():
    for i, y in phonebook.items():

        print(f'{i}: {y}')
        


COMMANDS = {
    add_contact: 'add',
    change_contact:'change',
    find_phone: 'phone',
    show_all: 'show all' 
}

def parser(text: str):
    for func, kw in COMMANDS.items():
        if text.startswith(kw):
            return func, text[len(kw):].strip().split()

def main():
    while True:
        user_input = input('Enter a command, if you not stupid russian ').strip().lower()
        func, data = parser(user_input)
        print(func(*data))
        if user_input in ('good bye', 'close', 'exit', 'go to hell', '.'):
            print ('ok.')
            break

if __name__ == '__main__':
    main()

