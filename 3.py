def lengthOfLongestSubstring(self, s: str) -> int:
    idx_per_c = {}
    left = -1  # left excluding, right including. Otherwise difficult to use last char
    lmax = 0
    for right, c in enumerate(s):
        if c in idx_per_c:
            left = max(left, idx_per_c[c])  # max necessary. Else last "a" in "abcba" would reset
        idx_per_c[c] = right
        lmax = max(lmax, right - left)
    return lmax
