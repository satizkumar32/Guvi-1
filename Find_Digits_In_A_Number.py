''' PROGRAM TO COUNT NUMBER OF DIGIT IN A NUMBER '''
a=int(input())
b=0
while(a!=0):
  a=a//10
  b+=1
print(b)
