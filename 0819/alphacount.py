import sys

arr = '''english is a west germanic
language originating in england
and is the first language for
most people in the united
kingdom the united states
canada australia new zealand
ireland and the anglophone
caribbean it is used
extensively as a second
language and as an official
language throughout the world
especially in common wealth
countries and in many
international organizations
'''


alpha = [0] * 27

for al in arr:
    alpha[al] += 1

print(alpha)