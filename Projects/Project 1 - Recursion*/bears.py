
# Given integer n, returns True or False based on reachability of goal
# See write up for "rules" for bears
def bears(n: int) -> bool:
    if n == 42:
        return True
    if n < 42:
        return False
    if n % 5 == 0:
        if bears(n - 42):
            return True
    if n % 3 == 0 or n % 4 == 0:
        r = int((n % 10) * ((n % 100 - n % 10) / 10))
        if r != 0:
            if bears(n - r):
                return True
    if n % 2 == 0:
        if bears(n//2):
            return True
    return False

