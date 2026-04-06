class Manacher:
    
    def __init__(self, s):
        # transform string with # and sentinels (# in between characters, @ at start, $ at end)
        # allows us to treat even-length palindromes as odd-length and avoid bounds checking during expansion
        self.ms = "@"
        for c in s:
            self.ms += "#" + c
        self.ms += "#$"

        # initialize p[] to store palindrome radii for each center in transformed string
        self.p = [0] * len(self.ms)

        # run Manacher’s algorithm
        self.runManacher()

    # runs Manacher’s algorithm and returns longest palindromic substring in O(n)
    def runManacher(self):
        # l and r track the rightmost palindrome found so far (l is left boundary, r is right boundary)
        l = r = 0
        n = len(self.ms)
        longest = -1

        for i in range(1, n - 1):
            # mirror of i around center (l + r)/2
            mirror = l + r - i

            # initialize p[i] based on its mirror if within bounds
            # if i is within the right boundary, we can use the mirror's palindrome radius as a starting point
            if i < r:
                self.p[i] = min(r - i, self.p[mirror])

            # expand palindrome centered at i
            while self.ms[i + 1 + self.p[i]] == self.ms[i - 1 - self.p[i]]:
                self.p[i] += 1

            # update [l, r] if the palindrome expands beyond current r
            if i + self.p[i] > r:
                l = i - self.p[i]
                r = i + self.p[i]
                
            # update longest palindrome length
            if longest == -1 or self.p[i] > self.p[longest]:
                longest = i
            
        # return longest palindromic substring in original string
        return self.ms[longest - self.p[longest]: longest + self.p[longest] + 1].replace("#", "")


# take in a string from io and print the longest palindromic substring
if __name__ == "__main__":
    s = input()
    result = Manacher(s).runManacher()
    print(result)