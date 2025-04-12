class Solution(object):
    def __init__(self):
        self.palindromes = []
        self.fact = [1] * 11

    def make_palindrome(self, num, is_odd):
        s = str(num)
        result = s
        idx = len(s) - 1
        if is_odd:
            idx -= 1
        while idx >= 0:
            result += s[idx]
            idx -= 1
        print(s,result)
        return int(result)



    def generate_palindromes(self, n, k):# n=3,k=5
        half = (n + 1) // 2
        start = 10**(half - 1)
        end = 10**half
        for i in range(start, end):
            palindrome = self.make_palindrome(i, n % 2)
            if palindrome % k == 0:
                self.palindromes.append(palindrome)

    def count_valid_permutations(self, s):
        from collections import Counter

        frequency = Counter(s)
        print(frequency)
        total_permutations = self.fact[len(s)]
        for count in frequency.values():
            total_permutations //= self.fact[count]
# ----------------------------------
        if '0' in frequency and frequency['0'] > 0:
            frequency['0'] -= 1
            invalid_permutations = self.fact[len(s) - 1]
            for count in frequency.values():
                invalid_permutations //= self.fact[count]
            total_permutations -= invalid_permutations

        return total_permutations

    def initialize_factorials(self):
        for i in range(2, 11):
            self.fact[i] = self.fact[i - 1] * i

    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        self.palindromes = []
        self.initialize_factorials()
        self.generate_palindromes(n, k)
        print(self.palindromes)
        total_count = 0
        unique_permutations = set()

        for palindrome in self.palindromes:
            s = str(palindrome)
            sorted_s = ''.join(sorted(s))
            if sorted_s not in unique_permutations:
                unique_permutations.add(sorted_s)
                total_count += self.count_valid_permutations(sorted_s)
        return total_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.countGoodIntegers(3, 5))
