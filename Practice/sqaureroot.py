#/usr/bin/env python

def is_sqaure(n):
    low, high = 0, n
    mid = n // 2

    if n < 0: return False
    if n**2 == 0 or n**2 == 1: return True

    while low <= high:
        if mid**2 == n:
            return True
        elif mid**2 > n:
            high = mid
            mid = (high+low) // 2
        elif mid**2 < n:
            low = mid
            mid = (high+low) // 2
