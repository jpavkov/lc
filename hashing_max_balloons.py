# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

def maxNumberOfBalloons(text: str) -> int:
    dicto = {}
    ans = 0

    for char in text:
        dicto[char] = dicto.get(char, 0) + 1

    b = dicto.get("b", 0)
    a = dicto.get("a", 0)
    l = dicto.get("l", 0) / 2
    o = dicto.get("o", 0) / 2
    n = dicto.get("n", 0)

    ans = int(min(b, a, l, o, n))

    return ans


print(maxNumberOfBalloons(text="balloonballoonzyx"))
print(maxNumberOfBalloons(text="balon"))
print(maxNumberOfBalloons(text=""))
