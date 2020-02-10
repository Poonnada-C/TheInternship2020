n_name = int(input('Enter number of names : '))
len_name = []
initial_list = []
sort_list = []
for i in range(n_name):
    initial_name = ''
    fullname = input('Enter name : ')
    split_name = fullname.split()
    for word in split_name:
        if word[0].isupper() == True:
            initial_name += word[0]
    if initial_name != '':
        initial_list.append(initial_name)
for i in sorted(sorted(initial_list), key = len, reverse = True):
    print(i)

