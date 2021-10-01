def is_prime(nr):
    '''
    -Determina daca un numar este prim sau nu
    Input:
    n,numar intre
    Output:
    True, n prim
    False, n neprim
    '''
    if nr < 2:
        return False
    for i in range(2, nr):
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
    if n<k:
        return 0
    factn=1
    factk=1
    factnk=1
    i=1
    while i<=n:
        factn=factn*i
        i=i+1
    i=1
    while i<=k:
        factk=factk*i
        i=i+1
    i=1
    while i<=n-k:
        factnk=factnk*i
        i=i+1

    return factn//(factk*factnk)


def test_get_n_choose_k():
    assert get_n_choose_k(3,2)==3
    assert get_n_choose_k(10,5)==252

def test_get_largest_prime_below():
    assert get_largest_prime_below(9)==7
    assert get_largest_prime_below(12)==11
    assert get_largest_prime_below(7)==5


def main():

  while True:
    print("Alege problema pe care o vrei rezolvata: ")
    print("1.Cel mai mare numar strict mai mic decat n")
    print("2.Combinari de n luate cate k")
    print("x.Exit")

    nr=input()
    if nr=='1':
        n=int(input("Da numarul n: "))
        print(get_largest_prime_below(n))
    elif nr=='2':
        n=int(input("Da numarul n: "))
        k=int(input("Da numarul k: "))
        print(get_n_choose_k(n,k))
    elif nr=='x':
        break
    else:
        print("Optiune gresita")


test_get_largest_prime_below()
test_get_n_choose_k()

main()
