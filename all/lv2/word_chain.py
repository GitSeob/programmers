def solution(n, words):
    prev = words[0]
    for i, word in enumerate(words[1:]):
        if prev[-1] != word[0] or word in words[:i]:
            return [(i+1)%n + 1, (i+1)//n + 1 ]
        prev = word
    return [0, 0]
