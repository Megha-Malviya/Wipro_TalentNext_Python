#Given the participant’s score sheet for your University Sports Day, store the scores in a list and find the runner-up score. 
# Example: for [2, 3, 6, 6, 5] the maximum score is 6, the second maximum is 5, so the output should be 5.

scores = [2, 3, 6, 6, 5]
highest = scores[0]
for s in scores:
    if s > highest:
        highest = s

second = None
for s in scores:
    if s != highest:
        if second is None or s > second:
            second = s

print(second)
