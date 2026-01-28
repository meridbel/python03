import sys
print("=== Player Score Analytics ===")
if len(sys.argv) == 1:
    print("No scores provided. Usage: python3"
          " ft_score_analytics.py <score1> <score2> ...")

if len(sys.argv) > 1:
    listpy = sys.argv[1:]
    numbers: list[int] = []
    try:
        for x in listpy:
            numbers.append(int(x))
    except ValueError:
        print("all data should be an int")
        sys.exit(1)
    print(f"Scores processed: {numbers}")
    print(f"Total players: {len(numbers)}")
    print(f"Total score: {sum(numbers)}")
    print(f"Average score: {(sum(numbers)) / (len(numbers))}")
    print(f"High score: {max(numbers)}")
    print(f"Low score: {min(numbers)}")
    print(f"Score range: {(max(numbers)) - (min(numbers))}")
