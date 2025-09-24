class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []
        
        if (numerator < 0) ^ (denominator < 0):
            result.append('-') # result will be negative
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        if remainder > 0:
            result.append(".")
            seen = {} # Keeps the index position of the remainder in result list 
            while remainder != 0:
                if remainder in seen: # Repetition detected
                    result.insert(seen[remainder], '(')
                    result.append(')')
                    break
                seen[remainder] = len(result)
                remainder *= 10
                result.append(str(remainder // denominator))
                remainder %= denominator
        
        return ''.join(result)