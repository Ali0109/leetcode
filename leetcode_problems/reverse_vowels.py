import string


class Solution:

    min_len = 1
    max_len = 3 * 10 ** 5
    string = ""

    def is_validated(self) -> bool:
        printable_ascii_characters = string.printable

        for char in self.string:
            if char not in printable_ascii_characters:
                return False

        if len(self.string) <= self.min_len or len(self.string) >= self.max_len:
            return False

        return True

    def solve(self):

        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        list_s = list(self.string)
        index_len_list_s = len(list_s) - 1
        used_index = []

        for i in range(0, index_len_list_s):

            if list_s[i] in vowels:
                for j in range(index_len_list_s, i, -1):
                    if list_s[j] in vowels and j not in used_index:
                        list_s[i], list_s[j] = list_s[j], list_s[i]
                        used_index.append(i)
                        used_index.append(j)
        return "".join(list_s)

    def reverseVowels(self, s: str) -> str:

        self.string = s

        is_validated = self.is_validated()
        if not is_validated:
            return self.string

        return self.solve()


s = "aA"
print(Solution().reverseVowels(s))
