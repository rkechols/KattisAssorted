from typing import List


NUMBER = "$"

ONE = "one"
TWO = "two"
THREE = "three"
FOUR = "four"
FIVE = "five"
SIX = "six"
SEVEN = "seven"
EIGHT = "eight"
NINE = "nine"

TEN = "ten"
TWENTY = "twenty"
THIRTY = "thirty"
FORTY = "forty"
FIFTY = "fifty"
SIXTY = "sixty"
SEVENTY = "seventy"
EIGHTY = "eighty"
NINETY = "ninety"
HUNDRED = "hundred"

ELEVEN = "eleven"
TWELVE = "twelve"
THIRTEEN = "thirteen"
FOURTEEN = "fourteen"
FIFTEEN = "fifteen"
SIXTEEN = "sixteen"
SEVENTEEN = "seventeen"
EIGHTEEN = "eighteen"
NINETEEN = "nineteen"


DIGIT_TO_STR_ONES = {1: ONE, 2: TWO, 3: THREE, 4: FOUR, 5: FIVE, 6: SIX, 7: SEVEN, 8: EIGHT, 9: NINE}
DIGIT_TO_STR_TENS = {2: TWENTY, 3: THIRTY, 4: FORTY, 5: FIFTY, 6: SIXTY, 7: SEVENTY, 8: EIGHTY, 9: NINETY}
DIGIT_TO_STR_TEENS = {10: TEN, 11: ELEVEN, 12: TWELVE, 13: THIRTEEN, 14: FOURTEEN, 15: FIFTEEN, 16: SIXTEEN, 17: SEVENTEEN, 18: EIGHTEEN, 19: NINETEEN}


def int_to_words(x: int) -> str:
	to_return = ""
	hundreds = x // 100
	if hundreds > 0:
		to_return += (DIGIT_TO_STR_ONES[hundreds] + HUNDRED)
	x = x % 100
	if x >= 20:
		tens = x // 10
		if tens > 0:
			to_return += DIGIT_TO_STR_TENS[tens]
		ones = x % 10
		if ones > 0:
			to_return += DIGIT_TO_STR_ONES[ones]
	else:
		if x >= 10:
			to_return += DIGIT_TO_STR_TEENS[x]
		elif x > 0:
			to_return += DIGIT_TO_STR_ONES[x]
	return to_return


def recenice(words: List[str]) -> str:
	otherwise_sum = 0
	for word in words:
		if word != NUMBER:
			otherwise_sum += len(word)
	for num in range(1, 1000):
		num_str = int_to_words(num)
		if len(num_str) + otherwise_sum == num:
			to_return = list()
			for word in words:
				if word == NUMBER:
					to_return.append(num_str)
				else:
					to_return.append(word)
			return " ".join(to_return) + " "
	return "NO ANSWER"


if __name__ == "__main__":
	n = int(input())
	values = list()
	for _ in range(n):
		values.append(input())
	answer = recenice(values)
	print(answer)
