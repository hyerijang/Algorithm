
# [difaulst_dict]
# * 존재하지 않는 키 조회시
# * 인자로 주어진 값으로 아이템 생성!!!

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
set_dict['약국'] = set()
set_dict['약국'].add(7)
print(set_dict)
