class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_list1=[i for i in s]
        new_list2 = [j for j in t]
        new_list1.sort()
        new_list2.sort()
        if new_list1==new_list2:
            return True
        else:
            return False
