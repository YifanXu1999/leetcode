class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow_(x, n):
            if (n == 0):
                return 1
            if (n == 1):
                return x
            if (n % 2 == 0):
                return pow(pow_(x, n // 2), 2)
            else:
                return pow(pow_(x, n // 2), 2) * x

        x = x if n > 0 else 1/x
        n_ = abs(n)
        ret = pow_(x, n_)
        return ret
