def is_prime(nr):
    '''
    -Determina daca un numar este prim sau nu
    Input:
    n,numar intre
    Output:
    True, n prim
    False, n neprim
    '''
    if nr < 2:            #daca numarul este mai mic decat 2 nu este prim
        return False
    for i in range(2, nr,1):#o metoda mai eficienta ar fi sa mergem pana la i*i<=nr
        if nr % i == 0:
            return False

    return True


def get_goldbach(n):
    '''
    -Determina perechile de numere p1,minim,p2,maxim,pentru care p1+p2=n
    Input:
    n,nummar natural,intreg
    Output:
    -p1 si p2, numere prime,naturale
    observam ca orice numar par diferit de 2 poate fi scris ca suma de doua numere prime
    de ex: 6=3+3,8=5+3,10=5+5
    '''
    for i in range(2, n, 1):
        if is_prime(i) == True and is_prime(n - i) == True:
            return i, n - i


def get_largest_prime_below(n):
    '''
    -Determina ultimul număr prim mai mic decât un număr dat.
    Input:
    -n,nr intreg,natural,numar dat
    Output:
    -ultimul numar prim mai mic decat n
    '''
    #problema specifica faptul ca ultimul numar prim mai mic decat un numar dat,astfel numarul dat nu se va ferifica chiar daca acesta este prim

    if n==3:
        return 2

    for i in range(n-1,2,-1):
          if(is_prime(i)):
              return i

def get_n_choose_k(n: int, k: int) -> int:
    '''
    -Calculează combinări de n luate câte k
    Input:
    n,k,numere intregi,naturale,n>0
    Output:
    -Combinarile de n luate cate k
    '''
    #o metoda mai eficienta de calcul a combinarilor cu o singura structura repetitiva
    c=1
    for i in range(1,k+1,1):
          c=c*(n-i+1)//i

    return c

# am ales sa dau minim 3 teste corecte in functiile de test
# am verificat si posibilele raspunsuri gresit si erori

def test_get_n_choose_k():
    assert get_n_choose_k(3,2)==3
    assert get_n_choose_k(10,5)==252
    assert get_n_choose_k(10,3)==120
    assert get_n_choose_k(4,2)==6

def test_get_largest_prime_below():
    assert get_largest_prime_below(9)==7
    assert get_largest_prime_below(12)==11
    assert get_largest_prime_below(7)==5
    assert get_largest_prime_below(22)==19
    assert get_largest_prime_below(5)==3

def test_get_goldbach():
    assert get_goldbach(100)==(3,97)
    assert get_goldbach(6)==(3,3)
    assert get_goldbach(12)==(5,7)

#Testele intotdeauna se vor face inainte de main
test_get_largest_prime_below()
test_get_n_choose_k()
test_get_goldbach()

def main():

  while True:
    print("1.Cel mai mare numar strict mai mic decat n")
    print("2.Combinari de n luate cate k")
    print("3.Conjectura lui Goldbach")
    print("x.Exit")

    option=input("Alege problema pe care o vrei rezolvata: ")
    if option=='1':
        n=int(input("Da numarul n: "))
        print(get_largest_prime_below(n))
    elif option=='2':
        n=int(input("Da numarul n: "))
        k=int(input("Da numarul k: "))
        a=n
        b=k
        print(get_n_choose_k(a, b))
    elif option=='3':
        n=int(input("Da numarul pentru a-l verifica: "))
        print(get_goldbach(n))
    elif option=='x':
        break
    else:
        print("Optiune gresita")

if __name__ == '__main__':
    main()
