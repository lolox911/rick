

fibo = lambda n: 1 if n <= 1 else fibo(n-1) + fibo(n-2)
print(fibo(int(input("Entrez un nombre pour calculer le n-ème terme de la suite de fibo:"))))

