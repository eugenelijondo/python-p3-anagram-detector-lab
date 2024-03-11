# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        matches = []
        for possible in possible_anagrams:
            if self.is_anagram(possible):
                matches.append(possible)
        return matches

    def is_anagram(self, possible):
        sorted_word = sorted(self.word)
        sorted_possible = sorted(possible.lower())
        return sorted_word == sorted_possible

# Example usage:
if __name__ == "__main__":
    listen = Anagram("listen")
    matches = listen.match(['enlists', 'google', 'inlets', 'banana'])
    print(matches)  # Output: ['inlets']
