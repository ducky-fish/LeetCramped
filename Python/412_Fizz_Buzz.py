class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        for x in range(1,n+1):
            modThree = x%3
            modFive = x%5
            
            
            if modThree + modFive == 0:
                answer.append("FizzBuzz")
            elif modThree == 0:
                answer.append("Fizz")
            elif modFive == 0:
                answer.append("Buzz")
            else:
                answer.append(str(x))
        
        return answer
