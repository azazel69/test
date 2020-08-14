from pprint import pprint

file_name = 'byron.txt'
file = open(file_name, mode='rb')  # mode (режим): чтение бинарное
file_content = file.read()
file.close()
#pprint(file_content)


file_name = 'pushkin.txt'
file = open(file_name, mode='r', encoding='utf8')
for line in file:  # если файл огромный - будет читать только строку
    print(line)
file.close()


class MyContextManager(object):

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('exit')


with MyContextManager() as manager:  # enter
    print(manager.__class__.__name__)  # MyContextManager
# exit