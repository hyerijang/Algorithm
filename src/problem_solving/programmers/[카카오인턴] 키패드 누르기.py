# 정답
left = ['1', '4', '7']
right = ['3', '6', '9']

keypad = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]


def find_location(s):
    for i in range(len(keypad)):
        for j in range(len(keypad[i])):
            if keypad[i][j] == s:
                return (i, j)


def solution(numbers, hand):
    answer = ''
    last_left = '*'
    last_right = '#'
    for n in numbers:
        n = str(n)

        if n in left:
            answer += 'L'
            last_left = n
            continue
        elif n in right:
            answer += 'R'
            last_right = n
            continue

        # 2,5,7,0의 경우
        location = find_location(n)
        last_left_loaction = find_location(last_left)
        last_right_loaction = find_location(last_right)

        # print(location, last_left_loaction, last_right_loaction)

        left_diff = abs(location[0]-last_left_loaction[0]) + \
            abs(location[1]-last_left_loaction[1])
        right_diff = abs(location[0]-last_right_loaction[0]) + \
            abs(location[1]-last_right_loaction[1])

        # print(left_diff, right_diff)
        if left_diff < right_diff or (left_diff == right_diff and hand == "left"):
            answer += 'L'
            last_left = n
            continue
        else:
            answer += 'R'
            last_right = n
            continue

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR")
