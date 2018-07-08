
participant = {'name' : 'Ola', 'country' : 'Poland', 'favorite_number' : [7, 4, 49]}


print(participant['country'])


if participant['name'] == 'Sonja':
    print('Hey Sonja')
elif participant['name'] == 'Ola':
    print('Hey OLa')
else:
    print('Hey anonymous')



def hi(name):
    if name == 'Sonja':
        print('Hey Sonja')
    elif name == 'Ola':
        print('Hey OLa')
    else:
        print('Hey anonymous')

hi('Sonja')



def hi2(name):
    print('Hi ' + name + '!')

hi2('marco')



girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for name in girls:
    hi2(name)
    print('Next girl')


for i in range(1, 6):
    print(i)
