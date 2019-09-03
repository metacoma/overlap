import sys, json
import itertools

def overlap(a):
  s = sorted(a)
  result = []
  n = 0
  for i in s:
    for j in range(0, n):
      e = s[j]

      if (e[1] >= i[0] and e[1] <= i[1]):
        result.append(e)

      if (i[0] >= e[0] and e[1] >= i[0]):
        result.append(i)

    n = n + 1

  return result
print(json.dumps(overlap(json.load(sys.stdin)), indent=4))
