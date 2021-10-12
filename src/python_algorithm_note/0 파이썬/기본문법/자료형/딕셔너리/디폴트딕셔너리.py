
# [difaulst_dict]
# https://devdocs.programmers.co.kr/references/python3/library/collections.html?highlight=defaultdict#collections.defaultdict
# * 존재하지 않는 키 조회시
# * 인자로 주어진 값으로 아이템 생성!!!
# ! 디폴트 타입을 지정해줘야한다.

import collections
# - 디폴트 값이 int인 디폴트 딕셔너리
int_dict = collections.defaultdict(int)

print(int_dict)
print(int_dict['제임스'])
print(int_dict)

# - 디폴트 값이 set인 디폴트 딕셔너리
set_dict = collections.defaultdict(set)
print(set_dict)
print(set_dict['병원'])
# set_dict['약국'] = set() #이렇게 지정하지 않아줘도 정상 작동
set_dict['약국'].add(7)
print(set_dict)


# ! 아래와 같이 기본타입을 지정해주지 않으면 그냥 평범한 dict로서 작동
none_dict = collections.defaultdict()
none_dict['지하철'] = set()  # 얘가 없으면 아래 코드에서 오류 뜸
none_dict['지하철'].add(7)
print(none_dict)
