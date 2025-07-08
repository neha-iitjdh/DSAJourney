def isPalindrome(x):
    if x<0 or (x !=0 and x%10 ==0):
        return False
    half = 0
    while x >half:
        half =(half * 10) + (x%10)
        x=x//10
        print(f"half: {half}, x: {x}")
    return x == half or x ==half //10

# This works only on half of the input

print(isPalindrome(1213443121))  # True