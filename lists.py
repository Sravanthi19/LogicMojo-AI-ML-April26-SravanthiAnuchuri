# Write a program to check palindrome.
mylist = ['anna']
for i in range(len(mylist)//2):
  if mylist[i] != mylist[len(mylist)-i-1]:
    print('not palindrome')
    break
else:
  print('palindrome')

#Write program count the blank spaces.

mylist = ['i am sravanthi ']
for i in mylist:
  count = 0
  for j in i:
    if j == ' ':
      count +=1
  print(count)

  ################ reverse string################
s = 'i am sravanti'

re = s[::-1]
print(re)

##############count no. of vowels and print all the vowels.################
s = 'i am sravanthi'
count = 0
vowels = 'aeiou'
for i in s:
  if i in vowels:
    count +=1
    print(i)
print(count)