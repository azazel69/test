from pprint import pprint

file_name = 'events.txt'
file_out = 'out.txt'
with open(file_out, mode='w') as out:
    with open(file_name, mode='r') as file:
        ss = ''
        for line in file:
            b = line.find('NOK')

            if b != -1 and ss != line[15:17]:
                out.write(line[0:17] + '] NOK')
                out.write('\n')
                ss = line[15:17]
    file.close()
out.close()
