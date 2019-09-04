rows = "ABCDEFGHI"
cols = "123456789"


def solve(board):
    for i, r in enumerate(rows):
        if i in [3, 6]:
            print("------+-------+------")
        for j, c in enumerate(cols):
            if j in [3, 6]:
                print("|"),
            print(values[r + c])

