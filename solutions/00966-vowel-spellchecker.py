class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        Time Complexity: O(W + Q)
        Space Complexity: O(W + Q)
        """
        vowels = set("aeiou")

        def devowel(word):
            return "".join('*' if c in vowels else c for c in word.lower())
        
        # 1. Exact match
        exact_words = set(wordlist)
        
        # 2. Case insensitive map 
        case_insensitive = {}
        for w in wordlist:
            lw = w.lower()
            # Only match the first occurance in the wordlist
            if lw not in case_insensitive:
                case_insensitive[lw] = w
        
        # 3. Vowel-error map
        vowel_map = {}
        for w in wordlist:
            vw = devowel(w)
            if vw not in vowel_map:
                vowel_map[vw] = w
        
        res = []
        for q in queries:
            lq, vq = q.lower(), devowel(q)
            if q in exact_words:
                res.append(q)
            elif lq in case_insensitive:
                res.append(case_insensitive[lq])
            elif vq in vowel_map:
                res.append(vowel_map[vq])
            else:
                res.append("")

        return res