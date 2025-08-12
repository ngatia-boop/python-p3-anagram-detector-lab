# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        matches = []

        for candidate in possible_anagrams:
            candidate_lower = candidate.lower()

            if candidate_lower == self.word:
                continue

            if sorted(candidate_lower) == sorted(self.word):
                matches.append(candidate)

        return matches           

        
