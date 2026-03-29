
mtn_code = {'*310#':'Credit', '*312#': 'Data', '*303#': 'Bonus'}

def my_mtn_app():
    dial_code = input('Enter the dial code: ')
    if dial_code in mtn_code:
        service = mtn_code[dial_code]
        print(f'\nThe {service} balance availabe')
    else:
        print(f"\nThe {dial_code} doesn't Exist")
my_mtn_app()



