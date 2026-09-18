"""Рекурсивная функция Фибоначчи с мемоизацией"""
def fib(n, memo=None):
    
    if memo is None:
        memo = {}

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print(fib(10))
print(fib(50))
print(fib(100))

"""Разделяй и властвуй"""
def count_even(arr, left=0, right=None):
    
    if right is None:
        right = len(arr) - 1

    if left == right:
        return 1 if arr[left] % 2 == 0 else 0

    mid = (left + right) // 2

    left_count = count_even(arr, left, mid)
    right_count = count_even(arr, mid + 1, right)

    return left_count + right_count

arr = [1, 2, 3, 4, 5, 6, 7, 8, 10]
print(count_even(arr))

arr2 = [1, 3, 5, 7]
print(count_even(arr2))

arr3 = [2, 4, 6, 8]
print(count_even(arr3))

"""задача с расписанием"""
def schedule(intervals):
    
    if not intervals:
        return []

    intervals_sorted = sorted(intervals, key=lambda x: x[1])

    selected = []
    last_end = float('-inf')

    for start, end in intervals_sorted:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected

intervals = [
    (13*60,       17*60),   
    (13*60+45,    15*60),
    (13*60,       14*60),
    (17*60+45,    18*60+15),
    (13*60+45,    14*60+15),
    (16*60,       16*60+30),
    (15*60,       16*60),
    (15*60,       17*60+45),
    (13*60+30,    15*60+15),
    (14*60+30,    15*60+30),
    (16*60+45,    17*60+30),
]

result = schedule(intervals)
print("Выбрано интервалов:", len(result))
for s, e in result:
    print(f"  {s//60}:{s%60:02d} – {e//60}:{e%60:02d}")