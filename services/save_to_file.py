def save_to_file(choices_arr, number):
    file = open('forms.txt', 'a+')
    file.write('Анкета №' + str(number) + '\n')
    for line in choices_arr:
        file.write('{0} - {1} \n'.format(choices_arr.index(line) + 1, line))

    file.close()