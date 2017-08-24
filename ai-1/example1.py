
i=10
j=20
if i>5 and j >10:
    print('i is greater than 5 now')
    print("Good!")
print ("out of if block")
# no data type



#print('call function sum:', sum(i,j))

list1=[1,2,3,4,5]

print(list1)

#list comprehension
# create list 2, elem in list 2 is  =every elem +1 in list 1
list2=[x+1 for x in list1]

print ("list2:", list2)

# get all odd number from list1
list3=[x for x in list1 if x%2==1]
print ("list3:", list3)

def sumandmulanddiv(i,j):
    s=i+j
    m=i*j
    d=i/j
    return (s,m,d)

#tuple: immutable, better performance, runs fast
t1=(100,200) # tuple
x,y=t1
print(x)
print ("tuple t1=", t1[0], t1[1])
(sum,mul,div)=sumandmulanddiv(10,5)
print('sum=', sum, "div=", div)

#sorted takes three paras, the seond one could be a function)
# lambda function: is a function without name, only used once

price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# a list containing three tuples
#x is parameter, each item in price
sortedList=sorted(price, key=lambda x: x[1], reverse=True)
print('sortedList=',sortedList)
#dictionay
#every elem has  a key and a value
#{} for dictionary
dic1={"apple":1.50, "grape":1.89, "pears": 2.20}

for k,v in dic1.items():
    print (k,": ", v)
#print(dic1.keys())

fruit='blueberry'
# in operator
if fruit not in dic1.keys():
    print (fruit, " needs to be in stock!")
else:
    print (fruit, " is in stock!")