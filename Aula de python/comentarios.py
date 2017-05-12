''''
comentario com 3 aspas 
'''
a = int(input("primeiro: "))
b = int(input("segundo"))
c = int(input("terceiro"))

if a >= b and a>=c:
    print("primeiro: %d" %a)
elif b>= c:
    print("segundo: %d" %b)
else:
    print("terceiro: %d" %c)