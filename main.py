def is_prime(nr):
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

def get_temp(temp: float,: str, to: str) -> float:
    return 12.9

def test_get_largest_prime_below():
    assert get_largest_prime_below(9)==7
    assert get_largest_prime_below(12)==11
    assert get_largest_prime_below(7)==5


test_get_largest_prime_below()


