cursor = [-6, -5, -4, -1, 1, 4, 5, 6]


def compare(board, word, bi, wi):
    board_size = len(board)
    word_size = len(word)
    wi = wi + 1

    if wi == word_size:
        return True

    for ci in range(0, 8):
        # 인덱스가 음수이면 다음 커서로
        if (bi + cursor[ci]) < 0:
            continue

        # 인덱스가 보드의 크기보다 크면 다음 커서로
        if (bi + cursor[ci]) >= board_size:
            continue

        # 글자가 다르면 다음 커서로
        if word[wi] != board[bi + cursor[ci]]:
            continue

        if compare(board, word, bi + cursor[ci], wi):
            return True

    return False


def case_solve():
    board = ""
    for _ in range(0, 5):
        board += input()

    board_size = len(board)
    word_cnt = int(input())
    for _ in range(0, word_cnt):
        word = input()
        is_yes = False
        for bi in range(0, board_size):
            # 첫글자가 다르면 다음칸으로 이동
            if word[0] != board[bi]:
                continue

            if compare(board, word, bi, 0):
                is_yes = True
                print(word + " YES")
                break

        if not is_yes:
            print(word + " NO")


case_cnt = int(input())
for _ in range(0, case_cnt):
    case_solve()
