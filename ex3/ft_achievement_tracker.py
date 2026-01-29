alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter',
           'boss_slayer', 'speed_demon', 'perfectionist'}

print("=== Achievement Tracker System ===")
print()
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")
print()
print("=== Achievement Analytics ===")
print(f"All unique achievements: {alice.union(bob, charlie)}")
print(f"Total unique achievements: {len(alice.union(bob, charlie))}")
print()
print(f"Common to all players: {alice.intersection(bob, charlie)}")
rare = (
    alice.difference(bob, charlie)
    .union(bob.difference(alice, charlie))
    .union(charlie.difference(alice, bob))
)

print(f"Rare achievements (1 player): {rare}")
print()
print(f"Alice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")