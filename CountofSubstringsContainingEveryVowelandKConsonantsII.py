# Example 1:
# Input: word = "aeioqq", k = 1
# Output: 0
# Explanation:
# There is no substring with every vowel.

# Example 2:
# Input: word = "aeiou", k = 0
# Output: 1
# Explanation:
# The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

# Example 3:
# Input: word = "ieaouqqieaouqq", k = 1
# Output: 3
# Explanation:
# The substrings with every vowel and one consonant are:
# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".


def countOfSubstrings( word: str, k: int):
    def isVowel(c):
        return c in {'a', 'e', 'i', 'o', 'u'}
    
    def atLeastK(word, k):
        n = len(word)
        ans = 0
        consonants = 0
        left = 0
        vowel_map = {}
        
        for right in range(n):
            if isVowel(word[right]):
                vowel_map[word[right]] = vowel_map.get(word[right], 0) + 1
            else:
                consonants += 1
            
            while len(vowel_map) == 5 and consonants >= k:
                ans += n - right
                if isVowel(word[left]):
                    vowel_map[word[left]] -= 1
                    if vowel_map[word[left]] == 0:
                        del vowel_map[word[left]]
                else:
                    consonants -= 1
                left += 1
        
        return ans
    
    return atLeastK(word, k) - atLeastK(word, k + 1)

word = "ieaouqqieaouqq"
k = 1
print(countOfSubstrings(word,k))