# ############        Simulate a simple voting system.
votes = {"Alice": 0, "Bob": 0, "Charlie": 0}
voted  = []          # track who already voted

def cast_vote(voter, candidate):
    if voter in voted:                          # O(n) — searches list
        print(f"{voter} already voted!")
    elif candidate not in votes:               # O(1) — dict lookup
        print(f"{candidate} is not a valid candidate!")
    else:
        votes[candidate] += 1                  # O(1)
        voted.append(voter)                    # O(1)
        print(f"{voter} voted for {candidate} successfully.")

def show_results():
    print("\n------ Voting Results ------")
    for candidate, count in votes.items():     # O(n)
        print(f"{candidate:10} → {count} votes")

def declare_winner():
    winner = max(votes, key=lambda k: votes[k])  # O(n)
    print(f"\n Winner: {winner} with {votes[winner]} votes!")

# ---- Test ----
cast_vote("Mim",   "Alice")
cast_vote("Rahim", "Bob")
cast_vote("Karim", "Alice")
cast_vote("Mim",   "Bob")       # duplicate vote
cast_vote("Sana",  "Dragon")    # invalid candidate

show_results()
declare_winner()

# ############   Way 2 — Using set for voters (faster duplicate check)
# votes = {"Alice": 0, "Bob": 0, "Charlie": 0}
# voted  = set()        # set instead of list → O(1) lookup
#
# def cast_vote(voter, candidate):
#     if voter in voted:                    # O(1) — set lookup ⚡
#         print(f"{voter} already voted!")
#     elif candidate not in votes:          # O(1) — dict lookup
#         print(f"{candidate} is not a valid candidate!")
#     else:
#         votes[candidate] += 1            # O(1)
#         voted.add(voter)                 # O(1)
#         print(f"{voter} voted for {candidate} successfully.")
#
# def show_results():
#     print("\n------ Voting Results ------")
#     for candidate, count in sorted(votes.items(),
#                                    key=lambda x: x[1],
#                                    reverse=True):   # sorted by votes
#         print(f"{candidate:10} → {count} votes")
#
# def declare_winner():
#     winner = max(votes, key=lambda k: votes[k])    # O(n)
#     print(f"\n🏆 Winner: {winner} with {votes[winner]} votes!")
#
# # ---- Test ----
# cast_vote("Mim",   "Alice")
# cast_vote("Rahim", "Bob")
# cast_vote("Karim", "Alice")
# cast_vote("Mim",   "Bob")
#
# show_results()
# declare_winner()

# ############    Way 3 — Using Counter (automatic counting)
# from collections import Counter
#
# candidates = {"Alice", "Bob", "Charlie"}   # valid candidates
# voted      = set()
# votes      = Counter()                     # auto counts, starts at 0
#
# def cast_vote(voter, candidate):
#     if voter in voted:
#         print(f"{voter} already voted!")
#     elif candidate not in candidates:
#         print(f"{candidate} is not a valid candidate!")
#     else:
#         votes[candidate] += 1             # Counter handles counting
#         voted.add(voter)
#         print(f"{voter} voted for {candidate} successfully.")
#
# def show_results():
#     print("\n------ Voting Results ------")
#     for candidate, count in votes.most_common():   # O(n log n) auto sorted!
#         print(f"{candidate:10} → {count} votes")
#
# def declare_winner():
#     if votes:
#         winner, count = votes.most_common(1)[0]   # O(n log n)
#         print(f"\n🏆 Winner: {winner} with {count} votes!")
#     else:
#         print("No votes yet!")
#
# # ---- Test ----
# cast_vote("Mim",   "Alice")
# cast_vote("Rahim", "Bob")
# cast_vote("Karim", "Alice")
# cast_vote("Sana",  "Alice")
#
# show_results()
# declare_winner()

# ##########      Way 4 — Full menu driven system (real project style)
# from collections import Counter
#
# candidates = {}        # name → party
# voted      = set()
# votes      = Counter()
#
# def register_candidate(name, party):
#     if name in candidates:
#         print(f"'{name}' already registered!")
#     else:
#         candidates[name] = party
#         print(f"'{name}' ({party}) registered successfully.")
#
# def cast_vote(voter, candidate):
#     if voter in voted:                       # O(1)
#         print(f"'{voter}' already voted!")
#     elif candidate not in candidates:        # O(1)
#         print(f"'{candidate}' is not a valid candidate!")
#     else:
#         votes[candidate] += 1
#         voted.add(voter)
#         print(f"'{voter}' voted for '{candidate}' successfully.")
#
# def show_results():
#     print("\n====== Voting Results ======")
#     print(f"{'Candidate':12} {'Party':12} {'Votes':>6} {'Bar'}")
#     print("-" * 45)
#     total = sum(votes.values())
#     for candidate, count in votes.most_common():
#         party   = candidates[candidate]
#         bar     = "█" * count              # visual bar
#         percent = (count/total*100) if total else 0
#         print(f"{candidate:12} {party:12} {count:>6}  {bar} ({percent:.1f}%)")
#
#     # show candidates with 0 votes too
#     for candidate in candidates:
#         if candidate not in votes:
#             party = candidates[candidate]
#             print(f"{candidate:12} {party:12} {0:>6}  (0.0%)")
#     print(f"\nTotal votes cast: {total}")
#
# def declare_winner():
#     if not votes:
#         print("No votes cast yet!")
#         return
#     winner, count = votes.most_common(1)[0]
#     party = candidates[winner]
#     print(f"\n🏆 Winner : {winner} ({party}) with {count} votes!")
#
# def show_menu():
#     print("\n====== Voting System ======")
#     print("1. Register Candidate")
#     print("2. Cast Vote")
#     print("3. Show Results")
#     print("4. Declare Winner")
#     print("0. Exit")
#     print("===========================")
#
# # ---- Test without menu loop ----
# register_candidate("Alice",   "Party A")
# register_candidate("Bob",     "Party B")
# register_candidate("Charlie", "Party C")
#
# cast_vote("Mim",   "Alice")
# cast_vote("Rahim", "Bob")
# cast_vote("Karim", "Alice")
# cast_vote("Sana",  "Alice")
# cast_vote("Rafi",  "Charlie")
# cast_vote("Mim",   "Bob")       # duplicate
#
# show_results()
# declare_winner()

# ##############      Way 5 — Handle tie (edge case)
# from collections import Counter
#
# votes = Counter({"Alice": 3, "Bob": 3, "Charlie": 1})  # Alice & Bob tied
#
# def declare_winner(votes):
#     if not votes:
#         print("No votes yet!")
#         return
#
#     max_votes = max(votes.values())                          # O(n)
#     winners   = [c for c, v in votes.items()
#                  if v == max_votes]                          # O(n)
#
#     if len(winners) == 1:
#         print(f"🏆 Winner: {winners[0]} with {max_votes} votes!")
#     else:
#         print(f"🤝 It's a tie between: {', '.join(winners)}"
#               f" with {max_votes} votes each!")
#
# declare_winner(votes)