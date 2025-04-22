numbs = int(input('Enter any 5 numbs:'))

numb1 =numbs % 10
numb2 = (numbs // 10) % 10
numb3 = (numbs // 100) % 10
numb4 = (numbs // 1000) % 10
numb5 = numbs // 10000

reversed_numb = numb1 * 10000 + numb2 * 1000 + numb3 * 100 + numb4 * 10 + numb5

print('Перевернуте число:',reversed_numb)