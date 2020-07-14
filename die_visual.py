from die import Die
import numba

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)