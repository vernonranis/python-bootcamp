# Functions with Outputs
input_f_name = input('Enter your first name: ')
input_l_name = input('Enter your last name: ')

def format_name(f_name, l_name):
    if f_name == ''  or l_name == '':
        return 'Invalid Input'
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f'{formatted_f_name} {formatted_l_name}'


print(format_name(input_f_name,input_l_name))
