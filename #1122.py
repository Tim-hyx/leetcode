class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr2) == 0:
            return arr1
        not_in_list = []
        return_list = []
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                not_in_list.append(arr1[i])
        for i in arr2:
            for j in arr1:
                if j == i:
                    return_list.append(j)
        if len(not_in_list) == 0:
            return return_list
        else:
            not_in_list.sort()
            for i in not_in_list:
                return_list.append(i)
            return return_list
