import random
from collections import Counter

dice = []

while len(dice) < 50:
    roll = random.randint(1, 6)
    dice.insert( (len(dice)+1) , roll )
    if len(dice) == 50:
        print("The average die value of all the rolls is " + str(float(sum(dice)/len(dice))))

counter = Counter(dice)

for roll in dice:
    counter[roll] += 1

for side, times in counter.most_common(1):
    print("The number %s was rolled the most, %d times." % (side, times))
