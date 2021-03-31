monthtoint = {
    'Январь': '01',
    'Февраль': '02',
    'Март': '03',
    'Апрель': '04',
    'Май': '05',
    'Июнь': '06',
    'Июль': '07',
    'Август': '08',
    'Сентябрь': '09',
    'Октябрь': '10',
    'Ноябрь': '11',
    'Декабрь': '12',
}

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()[5:]
    customer = lines[:6]
    lines = lines[13:]
    store = lines[:5]
    lines = lines[12:]
    book = lines[:7]
    lines = lines[14:]
    purchase = lines

for cus in customer:
    args = cus.split()
    args[0] = int(args[0])
    print("INSERT INTO customer VALUES ({}, '{}', '{}', {});".format(*args))
print('\n')
for st in store:
    args = st.split()
    if len(args) >= 4:
        new_args = [args[0], ' '.join(args[1:-2])]
        new_args.extend(args[-2:])
        args = new_args
    args[0] = int(args[0])
    print("INSERT INTO store VALUES ({}, '{}', '{}', {});".format(*args))
print('\n')
for b in book:
    args = b.split()
    new_args = [args[0], ' '.join(args[1:-3])]
    new_args.extend(args[-3:])
    args = new_args
    args[0] = int(args[0])
    print("INSERT INTO book VALUES ({}, '{}', {}, '{}', {});".format(*args))
print('\n')
for pur in purchase:
    args = pur.split()
    args[0] = int(args[0])
    args[1] = monthtoint[args[1]]
    args[2] = int(args[2])
    args[3] = int(args[3])
    args[4] = int(args[4])
    print("INSERT INTO purchase VALUES ({}, '2020-{}-01', {}, {}, {}, {}, {});".format(*args))
