from datetime import date

def is_prime(nr):
    if nr < 2:
        return False
    for i in range(2, nr):
        if nr % i == 0:
            return False

    return True

def get_age_in_days(birthday):
    '''
    -Calculeaza varsta in zile
    Input:
    -date de nastere,data(ziua,luna,anul
    Output:
    -varsta in zile
    '''

    varsta_in_zile=date.today()-birthday
    return varsta_in_zile.days


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
    for i in range(3, n,1):
        if is_prime(i) == True:
            for j in range(i, n):
                if is_prime(j) == True:
                    if n == i + j:
                        return i,j

def is_palindrome(n):
    '''
    -Determina daca n este palindrom sau nu
    Input:
    -n, numar intreg
    Output:
    -bool, True sau False, daca n este palindrom,respectiv daca n nu este palindrom
    '''
    nr=0
    nrvechi=n
    while n>0:
        nr=nr*10+n%10
        n=n//10

    if nr==nrvechi:
        return True
    return False

def is_superprime(n):
    '''
    -Determina daca un numar este superprim
    Input:
    -n,numar intreg,natural
    Output:
    -True, daca n este superprim,respectiv False daca n nu este superprim

    '''
    while n>0:
        if(is_prime(n)==False): return False
        n=n//10
    return True

def test_is_superprime():
    assert is_superprime(133)==False
    assert is_superprime(146)==False
    assert is_superprime(246)==False
    assert is_superprime(237)==False
    assert is_superprime(233)==True

def test_is_palindrome():
    assert is_palindrome(1234)==False
    assert is_palindrome(1221)==True
    assert is_palindrome(1100)==False
def test_get_age_in_days():
    assert get_age_in_days(date(1996,1,1))==9405

def test_get_goldbach():

     assert get_goldbach(100)==(3,97)
     assert get_goldbach(6)==(3,3)
     assert get_goldbach(12)==(5,7)

test_get_goldbach()
test_get_age_in_days()
test_is_palindrome()
test_is_superprime()