
# - '.' Matches any single character.​​​​
# ! 틀림 (50분)
# - 어려워.. 답 봐도 이해 안됨 ㅋ큐ㅠㅠ
# ! 아 이제보니 난이도가 hard였네
# - '*' Matches zero or more of the preceding element.

def isMatch(self, text, pattern):
    if not pattern:  # 패턴이 없는데
        return not text  # 텍스트가 남아있으면 False

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (self.isMatch(text, pattern[2:]) or
                first_match and self.isMatch(text[1:], pattern))
    else:
        return first_match and self.isMatch(text[1:], pattern[1:])


s = "aab"
p = "c*a*b"
print(isMatch(s, p))
