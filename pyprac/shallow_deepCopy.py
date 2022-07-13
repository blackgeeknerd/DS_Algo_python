import copy


warmtones = ['Red', 'Blue', 'Green']

pallete = warmtones
# pallete[0] = 'brown'
print(warmtones)

pallete2 = list(warmtones)

pallete2[0] = 'white'
print(warmtones)
print(pallete2)
pallete2.append('Black')
print(pallete2)
pallete2.pop(0)
print(pallete2)
print(warmtones)

pallete3 = copy.deepcopy(warmtones)
pallete3.reverse()
print(pallete3)
