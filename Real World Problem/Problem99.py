# ###########     Create a leaderboard sorted by score.
# leaderboard = {
#     "Mim":   1500,
#     "Rahim": 3200,
#     "Karim": 2800,
#     "Sana":  4100,
#     "Rafi":  1900
# }
#
# def show_leaderboard(leaderboard):
#
#     # convert to list of [player, score] pairs
#     items = list(leaderboard.items())
#
#     # manually sort using bubble sort
#     n = len(items)
#     for i in range(n):                          # O(n²)
#         for j in range(0, n - i - 1):
#             if items[j][1] < items[j+1][1]:    # compare scores
#                 items[j], items[j+1] = items[j+1], items[j]   # swap
#
#     print("\n===== Leaderboard =====")
#     print(f"{'Rank':<6} {'Player':<12} {'Score':>8}")   ###### <6,<12,>8 used for creating the gap
#     print("-" * 28)     ###### -- it will print 28 times within 1 line
#     rank = 1
#     for player, score in items:                 # simple for loop
#         print(f"{rank:<6} {player:<12} {score:>8}")
#         rank += 1
#
# show_leaderboard(leaderboard)

################    Way2
# leaderboard = {
#     "Mim":   1500,
#     "Rahim": 3200,
#     "Karim": 2800,
#     "Sana":  4100,
#     "Rafi":  1900
# }
#
# def get_score(item):        # regular function replaces lambda x: x[1]
#     return item[1]          # item = ("Mim", 1500) → returns 1500
#
# def show_leaderboard(leaderboard):
#     sorted_board = sorted(leaderboard.items(),
#                           key=get_score,            # ✅ no lambda
#                           reverse=True)
#     print("\n===== Leaderboard =====")
#     print(f"{'Rank':<6} {'Player':<12} {'Score':>8}")
#     print("-" * 28)
#     for rank, (player, score) in enumerate(sorted_board, start=1):
#         print(f"{rank:<6} {player:<12} {score:>8}")
#
# show_leaderboard(leaderboard)

# ##########  Way 2 — Using operator.itemgetter (faster than lambda)
# from operator import itemgetter
#
# leaderboard = {
#     "Mim":   1500,
#     "Rahim": 3200,
#     "Karim": 2800,
#     "Sana":  4100,
#     "Rafi":  1900
# }
#
# def show_leaderboard(leaderboard):
#     # itemgetter(1) → grabs index 1 (score) from each tuple
#     sorted_board = sorted(leaderboard.items(),
#                           key=itemgetter(1),        # faster than lambda ⚡
#                           reverse=True)
#
#     print("\n===== Leaderboard =====")
#     print(f"{'Rank':<6} {'Player':<12} {'Score':>8}")
#     print("-" * 28)
#     for rank, (player, score) in enumerate(sorted_board, start=1):
#         print(f"{rank:<6} {player:<12} {score:>8}")
#
# show_leaderboard(leaderboard)

# ##############  Way 3 — Using Counter (built for counting/ranking)
# from collections import Counter
#
# scores = Counter({
#     "Mim":   1500,
#     "Rahim": 3200,
#     "Karim": 2800,
#     "Sana":  4100,
#     "Rafi":  1900
# })
#
# # Add/update score
# scores["Mim"]   += 500      # O(1)
# scores["David"]  = 2000     # O(1) — new player
#
# # Top N players
# def top_players(n):
#     return scores.most_common(n)    # O(n log n)
#
# def show_leaderboard():
#     print("\n===== Leaderboard =====")
#     print(f"{'Rank':<6} {'Player':<12} {'Score':>8}")
#     print("-" * 28)
#     for rank, (player, score) in enumerate(scores.most_common(), start=1):
#         print(f"{rank:<6} {player:<12} {score:>8}")
#
# def show_top(n):
#     print(f"\n🏆 Top {n} Players:")
#     for rank, (player, score) in enumerate(top_players(n), start=1):
#         print(f"  {rank}. {player} → {score}")
#
# show_leaderboard()
# show_top(3)

# #########   Way 4 — Using heapq (most efficient for top N)
# import heapq
#
# leaderboard = {
#     "Mim":   1500,
#     "Rahim": 3200,
#     "Karim": 2800,
#     "Sana":  4100,
#     "Rafi":  1900
# }

# # Get top N — most efficient way
# def top_n_players(n):
#     # nlargest → O(n log k) — much faster than sorting all
#     return heapq.nlargest(n, leaderboard.items(), key=lambda x: x[1])
#
# # Get bottom N (lowest scores)
# def bottom_n_players(n):
#     return heapq.nsmallest(n, leaderboard.items(), key=lambda x: x[1])
#
# def show_leaderboard():
#     print("\n===== Leaderboard =====")
#     print(f"{'Rank':<6} {'Player':<12} {'Score':>8}")
#     print("-" * 28)
#     for rank, (player, score) in enumerate(top_n_players(len(leaderboard)),
#                                            start=1):
#         print(f"{rank:<6} {player:<12} {score:>8}")
#
# def show_top(n):
#     print(f"\n🏆 Top {n} Players:")
#     for rank, (player, score) in enumerate(top_n_players(n), start=1):
#         medal = ["🥇","🥈","🥉"][rank-1] if rank <= 3 else f"{rank}."
#         print(f"  {medal} {player:12} → {score}")
#
# def show_bottom(n):
#     print(f"\n⚠️ Bottom {n} Players (need improvement):")
#     for rank, (player, score) in enumerate(bottom_n_players(n), start=1):
#         print(f"  {rank}. {player:12} → {score}")
#
# show_leaderboard()
# show_top(3)
# show_bottom(2)

##########      Way 5 — Full leaderboard system (real project style)
import heapq
from collections import defaultdict

leaderboard = {}
score_history = defaultdict(list)    # tracks score over time

def add_player(name, score=0):
    if name in leaderboard:          # O(1)
        print(f"'{name}' already exists! Use update.")
        return
    leaderboard[name] = score        # O(1)
    score_history[name].append(score)
    print(f"✅ '{name}' added with score {score}.")

def update_score(name, new_score):
    if name not in leaderboard:      # O(1)
        print(f"'{name}' not found!")
        return
    old = leaderboard[name]
    leaderboard[name] = new_score    # O(1)
    score_history[name].append(new_score)
    diff = new_score - old
    arrow = "📈" if diff > 0 else "📉"
    print(f"{arrow} '{name}' score updated {old} → {new_score} ({diff:+})")

def remove_player(name):
    if name not in leaderboard:      # O(1)
        print(f"'{name}' not found!")
        return
    leaderboard.pop(name)            # O(1)
    print(f"🗑️ '{name}' removed.")

def get_rank(name):
    if name not in leaderboard:      # O(1)
        print(f"'{name}' not found!")
        return
    sorted_board = sorted(leaderboard,
                          key=leaderboard.get,
                          reverse=True)          # O(n log n)
    rank = sorted_board.index(name) + 1          # O(n)
    print(f"🎯 '{name}' is ranked #{rank} with {leaderboard[name]} points.")

def show_leaderboard():
    if not leaderboard:
        print("No players yet!")
        return
    total   = sum(leaderboard.values())          # O(n)
    average = total / len(leaderboard)

    print("\n========== Leaderboard ==========")
    print(f"{'Rank':<6}{'Player':<12}{'Score':>8}{'Bar':>5}")
    print("-" * 40)

    for rank, (player, score) in enumerate(
        heapq.nlargest(len(leaderboard),
                       leaderboard.items(),
                       key=lambda x: x[1]),       # O(n log n)
        start=1
    ):
        medal   = ["🥇","🥈","🥉"][rank-1] if rank <= 3 else f" {rank} "
        bar     = "█" * (score // 500)
        percent = score / total * 100
        print(f"{medal:<6}{player:<12}{score:>8}  {bar} ({percent:.1f}%)")

    print("-" * 40)
    print(f"{'Players:':20} {len(leaderboard)}")
    print(f"{'Total score:':20} {total}")
    print(f"{'Average score:':20} {average:.1f}")

def show_history(name):
    if name not in score_history:
        print(f"'{name}' not found!")
        return
    history = score_history[name]                 # O(1)
    print(f"\n📊 Score history for '{name}':")
    for i, score in enumerate(history, start=1):
        print(f"  Round {i}: {score}")

# ---- Test ----
add_player("Mim",   1500)
add_player("Rahim", 3200)
add_player("Karim", 2800)
add_player("Sana",  4100)
add_player("Rafi",  1900)

update_score("Mim", 3500)
update_score("Rafi", 1200)
remove_player("Karim")

show_leaderboard()
get_rank("Mim")
show_history("Mim")