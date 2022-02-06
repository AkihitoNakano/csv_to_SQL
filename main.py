import csv


csv_data = 'list.csv'
convert_text = 'tweet_list.txt'

table_name = 'list'

def create_table(row):
    return f'CREATE TABLE {table_name}(\n' \
           f'id INT,\n' \
           f'{row[0]} VARCHAR(140) NOT NULL,\n' \
           f'{row[1]} VARCHAR(20) NOT NULL,\n' \
           f'{row[2]} VARCHAR(10) NOT NULL,\n' \
           f'{row[3]} INT,\n' \
           f'{row[4]} INT,\n' \
           f'{row[5]} DATE NOT NULL,\n' \
           f'PRIMARY KEY(id)\n' \
           f');'

def insert_values(i, row):
    if  row[5] == '0' :
        date = '0000-00-00'
    else:
        date = row[5].replace('/', '-')

    return f'INSERT INTO {table_name} VALUES\n' \
           f'({i}, "{row[0]}", "{row[1]}","{row[2]}", {row[3]}, {row[4]}, "{date}");\n'


with open(csv_data, encoding='utf-8') as f:
    reader = csv.reader(f)
    values = ''
    for i, row in enumerate(reader):
        if i == 0:
            table = create_table(row)
        else:
            values += insert_values(i, row)

with open(convert_text, mode='wt', encoding='utf-8') as f:
    f.write(f'{table} \n\n{values}')



# print(f'{table} + \n+ {values}')
