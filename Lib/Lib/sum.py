#python function to sum all numbers in a list

def sum(a):
    sum=0
    for i in range(len(a)):#5 elem -0,1,2,3,4
        sum+=a[i] #sum=sum+a[i]
    print(sum)

sum([1,2,3])

