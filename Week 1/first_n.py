def analytic(n):
  phi = (1+(5**0.5))/2
  return (((phi)**n - ((1-phi)**n)))/(5**.5)

def last_two_values(n):
  a = b = 1
  for i in range(3,n+1):
    a,b = b, a+b
  return b

for i in range (2,100):
  if round(analytic(i))!=last_two_values(i):
    print(analytic(i))
    print(last_two_values(i))
    print(i)
    break

