# chapter02-1
# 파이썬 완전 기초
# print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php
# 파이썬 3가지 Print Formatting
# 자주 나오는 질문 참고

"""
참고 : Escape 문자
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : Null 문자
'''

"""

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# separator 옵션 사용
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션 사용
print('Welcome To', end=' ')
print('IT News', end=' ')
print('Web Site')

# file 옵션 사용
import sys

print('Learn Python', file=sys.stdout)

print()

# format 사용(d, s, f)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{0} {1}'.format('one', 'two'))

# %s

print('%10s' % ('nice',)) # 10칸을 확보하고 우측 정렬
print('{:>10}'.format('nice')) # 10칸을 확보하고 우측 정렬

print('%-10s' % ('nice',)) # 10칸을 확보하고 좌측 정렬
print('{:10}'.format('nice')) # 10칸을 확보하고 좌측 정렬



