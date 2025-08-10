def mySqrt(x: int) -> int:
        low = 0
        high = x

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                high = mid - 1
            else: 
                low = mid + 1
        return high

print(mySqrt(8))

        