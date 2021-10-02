def get_perfect_squares(start: int, end: int) -> list[int]:
    p_squares=[]
    for i in range(start,end):
        if i*i<=end:
            p_squares.append(i*i)

    return p_squares



def test_get_perfect_squares():
    assert get_perfect_squares(1,10)==[1, 4, 9]
    assert get_perfect_squares(1,25)==[1, 4, 9, 16, 25]

test_get_perfect_squares()