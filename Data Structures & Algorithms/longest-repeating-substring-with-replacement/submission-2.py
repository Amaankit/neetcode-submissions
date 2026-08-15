"""
LeetCode 424 - Longest Repeating Character Replacement

PATTERN:
    Sliding Window + Frequency Array

GOAL:
    Find the longest substring that can be converted into a string
    containing only one unique character by replacing at most k characters.

CORE IDEA:

    For every sliding window [l ... r], we keep track of the frequency
    of each character.

    Example:

        Window = "AABA"

        Frequency:
            A -> 3
            B -> 1

        The most frequent character is A.

        Window length = 4
        max_freq = 3

        Characters that need to be replaced:

            window_length - max_freq
            = 4 - 3
            = 1

        Therefore, with k = 1, "AABA" is a valid window because we can
        replace B with A:

            A A B A
              ↓
            A A A A


WHY DOES THIS WORK?

    We don't care which character we replace.

    We only care about keeping the most frequent character and replacing
    all other characters.

    Therefore:

        replacements_needed =
            window_size - max_frequency


SLIDING WINDOW:

    1. Move right pointer forward.
    2. Add s[r] to the frequency array.
    3. Update max_freq.
    4. Check whether the current window needs more than k replacements.
    5. If it does, move the left pointer forward until the window becomes
       valid again.
    6. Record the maximum valid window length.


IMPORTANT OPTIMIZATION:

    max_freq is only increased when we add a character.

    We DO NOT decrease max_freq when the left pointer moves.

    This means max_freq can become slightly stale.

    That's okay.

    A stale max_freq cannot make us miss the correct maximum answer.
    It only means that a window may temporarily appear valid when its
    actual max frequency is slightly smaller.

    This allows us to avoid recalculating the maximum frequency by
    scanning all 26 characters every time the window shrinks.


WHY IS THIS O(n)?

    The right pointer moves from left → right once.

    The left pointer also only moves forward.

    Neither pointer ever moves backwards.

    Therefore, even though there is a while loop inside the for loop,
    the total number of left-pointer movements is at most n.

        Right pointer movements = O(n)
        Left pointer movements  = O(n)

    Therefore:

        Time  = O(n)

    The frequency array has only 26 positions:

        Space = O(26) = O(1)


KEY FORMULA TO REMEMBER:

    replacements_needed = window_size - max_frequency


GENERAL PATTERN:

    Expand window
         ↓
    Update frequency
         ↓
    Calculate how many changes are required
         ↓
    If changes > k:
         shrink window
         ↓
    Update maximum answer
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        freq = [0] * 26
        max_len = 0
        max_freq = 0
        while(r<len(s)):
            freq[ord(s[r])-ord('A')] = freq[ord(s[r])-ord('A')]+1
            max_freq = max(max_freq,freq[ord(s[r])-ord('A')])
            while((r-l+1) -max_freq > k):
                
                freq[ord(s[l])-ord('A')] = freq[ord(s[l])-ord('A')]-1
                max_freq = 0
                for f in freq:
                    max_freq = max(max_freq,f)
                l=l+1
            if((r-l+1) -max_freq <= k):
                max_len = max(max_len,r-l+1)
            r+=1
        return max_len
        