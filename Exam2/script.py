import random

NUM_CONTESTANTS = 10
NUM_JUDGES = 8
MIN_SCORE = 1.0
MAX_SCORE = 10.0

scores = [[round(random.uniform(MIN_SCORE, MAX_SCORE), 2) for _ in range(NUM_JUDGES)] for _ in range(NUM_CONTESTANTS)]

print("Judges' Scores:")
for i, row in enumerate(scores):
    print(f"Contestant {i+1}: {row}")
print()

results = []
for i, row in enumerate(scores):
    sorted_row = sorted(row)
    trimmed_scores = sorted_row[1:-1]
    total = round(sum(trimmed_scores), 2)
    results.append(total)
    print(f"Contestant {i+1}'s total score: {total:.2f} (excluding lowest score of {sorted_row[0]} and highest score of {sorted_row[-1]})")

max_score = max(results)
winner_index = results.index(max_score)

print(f"\nWinner: Contestant {winner_index + 1} \nScore: {max_score:.2f}")
