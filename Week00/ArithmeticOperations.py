'''
Task 
Read two integers from STDIN and print three lines where:

* The first line contains the sum of the two numbers.
* The second line contains the difference of the two numbers (first - second).
* The third line contains the product of the two numbers.
https://www.hackerrank.com/challenges/python-arithmetic-operators

Sample Solution with format() method:

a = int(input())
b = int(input())
print('{0} \n{1} \n{2}'.format((a+b), (a-b), (a*b)))

'''

#dani
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b, a-b, a*b, sep="\n")
 #elena
a=int(input())
b=int(input())
sum=a+b
difference=a-b
product=a*b
print(sum)
print(difference)
print(product)
