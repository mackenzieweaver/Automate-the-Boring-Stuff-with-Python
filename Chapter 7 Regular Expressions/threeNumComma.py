import re

threeNumComma = re.compile(r'''(
    (^\d{1,3},)     # starts with one, two, or three numbers and a comma
    (\d{3},?)+      # there has to be 3 more numbers
)''', re.I)
threeNumComma.search('42').group()
threeNumComma.search('1,234').group()
threeNumComma.search('6,368,745').group()
