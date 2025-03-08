import re

text = 'abcdfghijk'
parser = re.search('a[b-f]*f', text )
print(parser)

print(parser.group())
print("_"*40)

#finditer() returns an iterator that produces match objects for each match

silly_string = 'the cat in the hat'
pattern = 'the'
for match in re.finditer(pattern, silly_string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=match.group(), begin=match.start(), end=match.end()
    )
    print(s)