"""
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)


"""
heros= ['spider man','thor','hulk','iron man','captain america']

#1
print(heros.__len__()) #O(n)


#2
heros.insert(5,'black panther')
#or,
# heros.append('black panther') #O(nheros=['spider man','thor','hulk','iron man','captain america']
print(heros)

#3 A bit complex way to do this:
heros.remove('black panther')

for i in range(len(heros)):
   if (heros[i] == 'hulk'):
      heros.insert(i+1, 'black panther')

print(heros)

#4
heros[1:3] = ['doctor strange']
print(heros)

#5
heros.sort() #O(n2)

print(heros)






