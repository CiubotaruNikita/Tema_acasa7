nterms = int(input("Câți termeni? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Vă rugăm să introduceți un număr întreg pozitiv")
else:
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1