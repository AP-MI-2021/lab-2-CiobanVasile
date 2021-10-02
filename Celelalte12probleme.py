from datetime import date

def is_prime(nr):
    if nr < 2:
        return False
    for i in range(2, nr):
        if nr % i == 0:
            return False

    return True


'''def get_age_in_days(birthday):
    data_nasterii_str_lst = birthday.split('/')
    data_nasterii_int_lst = []
    today=date.today()
    for fiecare_data in data_nasterii_str_lst:
        data_nasterii_int_lst.append(int(fiecare_data))
    return (today.year-data_nasterii_int_lst[2]) * 365 + (data_nasterii_int_lst[1] - today.month) * 30 + data_nasterii_int_lst[0] - today.day

'''
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

def get_leap_years(start: int, end: int) -> list[int]:
    years_list=[]
    i=start
    for i in range(i,end+1):
        if (i%4==0 and i%100!=0) or i%400==0:
            years_list.append(i)


    return years_list


def is_antipalindrome(n) -> bool:
    cifre_n = []
    while n > 0:
        cifre_n.append(n % 10)
        n = n // 10

    lenght=len(cifre_n)
    '''
    i=0
    while i<=lenght//2:
        if cifre_n[i] == cifre_n[lenght-1-i]:
            return False
        i=i+1
'''
    for i in range(0,lenght//2):
          if cifre_n[i] == cifre_n[lenght-1-i]:
              return False

    return True




def test_get_leap_years():
    assert get_leap_years(2000,2021)==[2000, 2004, 2008, 2012, 2016, 2020]
    assert get_leap_years(1990,2001)==[1992, 1996, 2000]

def test_is_antipalindrome():
    assert is_antipalindrome(2773)==True

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

#def test_get_age_in_days():
 #   assert get_age_in_days(date(7/3/2002))==6732

def test_is_antipalindrome():
    assert is_antipalindrome(2783) == True
    assert is_antipalindrome(2773) == False

def test_get_goldbach():

     assert get_goldbach(100)==(3,97)
     assert get_goldbach(6)==(3,3)
     assert get_goldbach(12)==(5,7)

test_get_goldbach()
#test_get_age_in_days()
test_is_palindrome()
test_is_superprime()
test_is_antipalindrome()
test_get_leap_years()
test_is_antipalindrome()