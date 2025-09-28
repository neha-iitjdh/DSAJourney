class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #APPROACH1
        answer = []
        for i in range(n):
            div3 = True if (i+1) % 3 == 0 else False
            div5 = True if (i+1) % 5 == 0 else False
            answer.append(
                "FizzBuzz"
                if (div3 and div5)
                else "Fizz" if div3 else "Buzz" if div5 else str(i+1)
            )
        return answer
