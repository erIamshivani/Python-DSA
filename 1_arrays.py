"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this.
"""
monthlyExpense = [2200,2350,2600,2130,2190]

#1 :
febExtraExpense = monthlyExpense[1] - monthlyExpense[0]
print("Extra $ spent in Feb as compared to Jan: $", febExtraExpense)
print("Time Complexity: O(1)")

#2 :
firstQuarterExpense = 0
firstQuarterExpense = monthlyExpense[0] + monthlyExpense[1] + monthlyExpense[2]

print("\n\nFirst Quarter expense: $", firstQuarterExpense)

#3:
flag = 0
for i in range(len(monthlyExpense)):
    if monthlyExpense[i] == 2000:
        flag =1
    else:
        flag =0

if flag is 1:
    print("\n\nYou spent $2000 in '" + i + "' month.")
else:
    print("\n\nYou did not spend exact $2000 in any month.")


#4 :
monthlyExpense.append(1980)
print("\n\nExpenses with June as well:", monthlyExpense)

#5 :
print("\n\nInitial expense before deduction:", monthlyExpense)
aprilRefund = 200
aprilExpense = monthlyExpense[3]
monthlyExpense[3] = aprilExpense - aprilRefund
print("Updated expense after april refund:", monthlyExpense)

print("--------------------------------------------------------------------------------------------------------------")
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
heros=['spider man','thor','hulk','iron man','captain america']

#1 :
print("Length of list:", len(heros))

#2:
heros.append("Black Panther")
print("\n\nAppending Black Panther:",heros)

#3:
heros.remove("Black Panther")
heros.insert(3, "Black Panther")
print("\n\nRe-arranging Black Panther after Hulk:",heros)

#4:
heros[1:3] = ['Doctor Strange']
print("\n\nReplacing Hulk and Thor with Doctor Strange:", heros)

#5 :
heros.sort()
print("\n\nList sorted alphabetically:", heros)


print("--------------------------------------------------------------------------------------------------------------")


"""
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
"""

maxNumber = int(input("\n\nEnter a max number you desire:"))
num= []
for i in range(maxNumber):
    if i % 2 == 1:
        num.append(i)
print("Odd numbers between 1 and %s are: "% str(maxNumber), num)


"""
Output :

usr/bin/python3.6 /home/sshinde/PycharmProjects/Python-DSA/1_arrays.py
Extra $ spent in Feb as compared to Jan: $ 150
Time Complexity: O(1)


First Quarter expense: $ 7150


You did not spend exact $2000 in any month.


Expenses with June as well: [2200, 2350, 2600, 2130, 2190, 1980]


Initial expense before deduction: [2200, 2350, 2600, 2130, 2190, 1980]
Updated expense after april refund: [2200, 2350, 2600, 1930, 2190, 1980]
--------------------------------------------------------------------------------------------------------------
Length of list: 5


Appending Black Panther: ['spider man', 'thor', 'hulk', 'iron man', 'captain america', 'Black Panther']


Re-arranging Black Panther after Hulk: ['spider man', 'thor', 'hulk', 'Black Panther', 'iron man', 'captain america']


Replacing Hulk and Thor with Doctor Strange: ['spider man', 'Doctor Strange', 'Black Panther', 'iron man', 'captain america']


List sorted alphabetically: ['Black Panther', 'Doctor Strange', 'captain america', 'iron man', 'spider man']
--------------------------------------------------------------------------------------------------------------


Enter a max number you desire:20
Odd numbers between 1 and 20 are:  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

Process finished with exit code 0


"""