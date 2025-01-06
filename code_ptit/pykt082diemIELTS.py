d = {
    (3, 4): 2.5, (5, 6): 3.0, (7, 9): 3.5, (10, 12): 4.0,
    (13, 15): 4.5, (16, 19): 5.0, (20, 22): 5.5, (23, 26): 6.0,
    (27, 29): 6.5, (30, 32): 7.0, (33, 34): 7.5, (35, 36): 8.0,
    (37, 38): 8.5, (39, 40): 9.0
}
def scr(x):
    return next((score for (a, b), score in d.items() if a <= x <= b), None)

if __name__ == '__main__':
    for _ in range(int(input())):
        l, r, s, w = map(float, input().split())
        l, r = scr(l), scr(r)
        overall = (l + r + s + w) / 4
        k = overall - int(overall)
        if 0.25 <= k < 0.75: overall = int(overall) + 0.5
        elif k >= 0.75: overall = int(overall) + 1
        else:overall = int(overall)
        print(f'{overall:.1f}')
