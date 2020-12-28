class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        length = int(len(s))
        a = s[0:int(length / 2)]
        b = s[int(length / 2):]
        num_a, num_b = 0, 0
        for i in a:
            if i in vowels:
                num_a += 1
        for j in b:
            if j in vowels:
                num_b += 1
        if num_a == num_b:
            return True
        else:
            return False
