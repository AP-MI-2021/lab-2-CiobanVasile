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

def test_is_antipalindrome():
    assert is_antipalindrome(2783)==True
    assert is_antipalindrome(2773)==False


test_is_antipalindrome()
