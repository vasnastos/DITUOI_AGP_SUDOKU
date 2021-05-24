strgntest="DIT UOI-DEPARTRMENT OF INFORMATICS AND TELECOMMUNICATIONS"
print(f'String Length:{len(strgntest)}')

print('1.')
for k in strgntest:
    print(k,end='')
print('\n')

print('2.')
for k in list(strgntest):
    print(k,end='')
print('\n')

print('3.')
for i in range(len(strgntest)):
    print(strgntest[i],i,' ',end='')
