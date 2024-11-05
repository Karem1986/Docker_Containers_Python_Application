
name = input('What is your name: ')

which_pie = input('Which pie would you like to make' + " " + name + " " + 'leek potato or apple pie? ')
print(which_pie)

if which_pie == 'apple':
  print('Your pie will have as ingredients: ')
  apple_pie = ['flour', 'soya drink', 'sugar', 'cinnamon']
  print(apple_pie)
elif which_pie == 'leek potato':
 leek_potato_pie = ['leeks', 'soya drink', 'onions', 'potatoes']
 print('Your pie will have as ingredients: ')
 print(list(leek_potato_pie))
