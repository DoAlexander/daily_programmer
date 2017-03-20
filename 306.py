# https://www.reddit.com/r/dailyprogrammer/comments/5z4f3z/20170313_challenge_306_easy_pandigital_roman/
# Description

# 1474 is a pandigital in Roman numerals (MCDLXXIV). It uses each of the symbols I, V, X, L, C, and M at least once. Your challenge today is to find the small handful of pandigital Roman numbers up to 2000.
# Output Description

# A list of numbers. Example:
# 1 (I), 2 (II), 3 (III), 8 (VIII) (Examples only, these are not pandigital Roman numbers)
# Challenge Input

# Find all numbers that are pandigital in Roman numerals using each of the symbols I, V, X, L, C, D and M exactly once.
# Challenge Input Solution

# 1444, 1446, 1464, 1466, 1644, 1646, 1664, 1666
# See OEIS sequence A105416 for more information.
# http://oeis.org/A105416

import collections

# Dict for numeral to int values | covers all possible combinations of letters | does not handle large number syntax for roman numerals
d_numerals = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':100,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
s_numerals = collections.OrderedDict(sorted(d_numerals.items(), key=lambda x: x[1], reverse=True))

# Converts integers to numerals
def int_to_numeral(arg):
	num = arg
	out = ''
	while(num > 0):
		for x,y in enumerate(s_numerals):
			if num - s_numerals[y] >= 0:
				num -= s_numerals[y]
				out += y
				break
	return out

print(int_to_numeral(2017))