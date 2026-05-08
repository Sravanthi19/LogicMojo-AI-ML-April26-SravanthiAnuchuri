# Write a program to check palindrome.
mylist = ['anna']
for i in range(len(mylist)//2):
  if mylist[i] != mylist[len(mylist)-i-1]:
    print('not palindrome')
    break
else:
  print('palindrome')