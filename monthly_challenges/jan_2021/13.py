# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3602/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Each boat can carry at max 2 people, this is important because otherwise this is a very tough problem figuring out which people go in which boat
        1. Sort
        2. Because the max people in each boat is two, it doesn't benefit us to pair the heaviest person with the next heaviest person. Thus, we can pair the heaviest with the lightest, or they get their own boat.
            This will allow us to iterate from both directions, rather than do an n**2 iteration by starting at the heaviest and iterating through the rest to find one that fits
        3. End when i = j, keep a count
        """
        
        people.sort()
        boats = 0
        
        i = 0
        j = len(people) - 1
        while i <= j:
            boats += 1
            # if lightest doesn't fit with heaviest, heaviest gets his own boat
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        
        return boats
