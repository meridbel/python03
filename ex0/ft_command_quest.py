import sys

print("=== Command Quest ===")
program_name = sys.argv[0]
if len(sys.argv) == 1:
    print("No arguments provided!")
    print(f"Program name: {program_name}")
    print(f"Total arguments: {len(sys.argv)}")

if len(sys.argv) > 1:
    print(f"Program name: {program_name}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    i = 1
    for x in sys.argv[1:]:
        print(f"Argument {i}: {x}")
        i = i + 1
    print(f"Total arguments: {len(sys.argv)}")
