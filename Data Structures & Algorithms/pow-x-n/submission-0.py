class Solution:

    def binary_pow(self,base: float, exp: int) -> float:
        # Base cases
        if exp == 0:
            return 1.0
        if base == 0:
            return 0.0

        # Step 1: Divide - compute half power once
        half = self.binary_pow(base, exp // 2)

        # Step 2: Conquer - square the result
        if exp % 2 == 0:
            return half * half
        else:
            return half * half * base

    def myPow(self, x: float, n: int) -> float:


        if n < 0:
            return 1.0 / self.binary_pow(x, abs(n))
        return self.binary_pow(x,n)
    
    

        