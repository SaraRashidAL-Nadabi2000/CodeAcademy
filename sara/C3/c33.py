def is_even(L):
    evenList =[]
    for num in L:
        if num%2 ==0: #even
            evenList.append(num)
    return evenList
number = [10,2,3,14,17,29,19,22,26]
evens= is_even(number)
print("Numbers:",number)
print("Even Number:",evens)
##using filters
evenusingfilters =lis (filter(lambda n: n%2==0 ,numbers))
print("Filterde evens:",evenusingfilters)