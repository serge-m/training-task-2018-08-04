"""
273. Integer to English Words
Hard
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        res = []
        bln = 10 ** 9
        res.append(f(num // bln, "Billion"))
        num = num % bln

        mln = 10 ** 6
        res.append(f(num // mln, "Million"))
        num = num % mln

        tsd = 10 ** 3
        res.append(f(num // tsd, "Thousand"))
        num = num % tsd

        res.append(f(num, ""))

        res = ' '.join([part for part in res if part != ""])

        if res == "":
            return "Zero"
        return res


def f(x, name):
    assert x < 1000
    r = f_1000(x)
    if r and name:
        return r + " " + name
    else:
        return r


digits = [
    "------",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen"
]

tens = [
    "--",
    "--",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety"
]


def f_1000(x):
    res = []
    if x // 100 > 0:
        res.extend([digits[x // 100], "Hundred"])
        x = x % 100

    if x // 10 > 1:

        res.append(tens[x // 10])
        if x % 10 > 0:
            res.append(digits[x % 10])
    elif x > 0:
        res.append(digits[x])
    return " ".join(res)


