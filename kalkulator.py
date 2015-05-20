def dodawanie(a,b):
    return a+b
def get_info():
    print("To jest prosty programik kalkulator")
get_info()
print('Podaj pierwsza liczbe:')
a=int(input())
print('Podaj druga liczbe:')
b=int(input())
wynik=dodawanie(a,b)
print(wynik)
