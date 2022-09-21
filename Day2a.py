# weight= int(input("Weight: "))
# unit= input("(K)g or (L)bs: ")
# if unit.upper()=="K":
#     converted=weight/0.45
#     print("Weight in Lbs: "+str(converted))
# else:
#     converted=weight*0.45
#     print("Weight in Kgs: "+str(converted))

"""
Weight: 266
(K)g or (L)bs: l
Weight in Kgs: 119.7
"""


# i=1
# while i<=5:
#     print(i)
#     i=i+1

"""
1
2
3
4
5
"""


# i=1
# while i<=10:
#     print(i*'*')
#     i=i+1

"""
*
**
***
****
*****
******
*******
********
*********
**********
"""


# names=["chandu", "raj", "sam", "adhi"]
# print(names)
# print(names[0])
# print(names[1])
# print(names[-1])            #[-1] is the last element in the list
# print(names[-2])            #[-2] is the second last element in the list
# names[3]="adi"              #replace the mistakes 
# print(names)
# print(names[0:3])
# print(names[1:3])
# print(names)

"""
['chandu', 'raj', 'sam', 'adhi']
chandu
raj
adhi
sam
['chandu', 'raj', 'sam', 'adi']
['chandu', 'raj', 'sam']
['raj', 'sam']
['chandu', 'raj', 'sam', 'adi']
"""


# numbers=[1,2,3,4,5]
# numbers.append(6)
# print(numbers)              #[1, 2, 3, 4, 5, 6]
# numbers.insert(0,-1)
# print(numbers)              #[-1, 1, 2, 3, 4, 5, 6]
# numbers.insert(0,-3)
# print(numbers)              #[-3, -1, 1, 2, 3, 4, 5, 6]
# numbers.remove(3)
# print(numbers)              #[-3, -1, 1, 2, 4, 5, 6]
# print(1 in numbers)         #True
# print(10 in numbers)        #False
# print(len(numbers))         #7
# numbers.clear()
# print(numbers)              #[]
# print(len(numbers))         #0


# numbers=[1,2,3,4,5]           
# for item in numbers:
#     print(item)

"""(((or)))"""              #o/p will be same for these two method types

# i=0
# while i<len(numbers):
#     print(numbers[i])
#     i=i+1

"""
1
2
3
4
5
"""


# numbers=range(5)
# for number in numbers:
#     print(number)

"""
1
2
3
4
"""


# numbers=range(5,10)
# for number in numbers:
#     print(number)

"""
5
6
7
8
9
"""


# numbers=range(5,10,2)
# for number in numbers:
#     print(number)

"""
5
7
9
"""


# numbers=range(5)
# for number in range(5):
#     print(number)

"""
0
1
2
3
4
"""

