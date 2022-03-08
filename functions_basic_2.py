#1. Countdown
def  countDown(num):
    list = []
    for x in range(num, -1, -1):
        list.append(x)
    return list
print(countDown(10))

#2. Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([46,5]))

#3. First Plus Length
def first_plus_length(list):
    print(list[0])
    return len(list)
print(first_plus_length(1,2,3,4,5,6,7))

#4. Values Greater than Second
def values_greater_than_second(list):
    if len(list)<2:
            return False
    newList = []
    # greaterThan = list[1]
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([20,36,1,76,5,10,42,7]))
print(values_greater_than_second([36,1,0,3,76,11,20,3]))
print(values_greater_than_second([1]))
print(values_greater_than_second([]))

#5. This Length, That Value
def this_length_that_value(size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(this_length_that_value(5,11))