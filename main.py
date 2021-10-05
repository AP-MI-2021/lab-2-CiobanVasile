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
    for i in range(2, nr):#o metoda mai eficienta ar fi sa mergem pana la i*i<=nr
        if nr % i == 0:
            return False

    return True

def get_largest_prime_below(n):
    '''
    -Determina ultimul număr prim mai mic decât un număr dat.
    Input:
    -n,nr intreg,natural,numar dat
    Output:
    -ultimul numar prim mai mic decat n
    '''
    #problema specifica faptul ca ultimul numar prim mai mic decat un numar dat,astfel numarul dat nu se va ferifica chiar daca acesta este prim
    nr=n-1
    while is_prime(nr)==False:
        nr=nr-1

    return nr

def get_n_choose_k(n: int, k: int):
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

# am ales sa dau 5 teste corecte in functiile de test
# am verificat si posibilele raspunsuri gresit si erori
def test_get_n_choose_k():
    assert get_n_choose_k(3,2)==3
    assert get_n_choose_k(10,5)==252
    assert get_n_choose_k(10,3)==120
    assert get_n_choose_k(3,1)==3
    assert get_n_choose_k(4,2)==6

def test_get_largest_prime_below():
    assert get_largest_prime_below(9)==7
    assert get_largest_prime_below(12)==11
    assert get_largest_prime_below(7)==5
    assert get_largest_prime_below(22)==19
    assert get_largest_prime_below(5)==3

#Testele intotdeauna se vor face inainte de main
test_get_largest_prime_below()
test_get_n_choose_k()



def main():

  while True:
    print("1.Cel mai mare numar strict mai mic decat n")
    print("2.Combinari de n luate cate k")
    print("x.Exit")

    option=input("Alege problema pe care o vrei rezolvata: ")
    if option=='1':
        n=int(input("Da numarul n: "))
        print(get_largest_prime_below(n))
    elif option=='2':
        n=int(input("Da numarul n: "))
        k=int(input("Da numarul k: "))
        print(get_n_choose_k(n,k))
    elif option=='x':
        break
    else:
        print("Optiune gresita")


main()
