import random

outcomes = [0, 1, 2, 3, 4, 6, 'W']
weights = [30, 25, 15, 5, 12, 8, 5]

def simulate_ball():
   
    return random.choices(outcomes, weights=weights)[0]


def create_team(name):
    return {
        "name": name,
        "runs": 0,
        "wickets": 0,
        "balls": 0,
        "overs_runs": [],
        "fall_of_wicket": [],
        "batsmen": {f"batsman{i}": {"runs": 0, "balls": 0} for i in range(1, 12)}
    }

team1 = create_team("Peshawar Zalmi")
team2 = create_team("Islamabad United")

# --- Function to play one inning ---
def play_inning(team, target=None):
    striker_key = "batsman1"
    non_striker_key = "batsman2"
    next_batsman = 3
    total_score = 0
    total_wickets = 0
    all_out = False

    for over in range(20):
        if all_out or (target and total_score >= target):
            break

        over_score = 0

        for ball in range(6):
            if all_out or (target and total_score >= target):
                break

            result = simulate_ball()
            team["balls"] += 1  

            if result == 'W':
                team["batsmen"][striker_key]["balls"] += 1  
                team["fall_of_wicket"].append(
                    f"batsman{next_batsman - 1}-{total_score}"
                )

                if next_batsman <= 11:
                    striker_key = f"batsman{next_batsman}"
                    next_batsman += 1
                else:
                    all_out = True  # FIX 3: set flag to break outer loop too
                    break
            else:
                total_score += result
                over_score += result
                team["batsmen"][striker_key]["runs"] += result
                team["batsmen"][striker_key]["balls"] += 1

                if result in [1, 3]:
                    striker_key, non_striker_key = non_striker_key, striker_key

        team["overs_runs"].append(over_score)
        
        striker_key, non_striker_key = non_striker_key, striker_key

    team["runs"] = total_score
    team["wickets"] = total_wickets


def print_scorecard(team):
    print(f"\n--- {team['name']} Scorecard ---")
    print(f"{'Batsman':<12} {'Runs':<6} {'Balls':<6}")
    for name, stats in team["batsmen"].items():
        if stats["balls"] > 0:  # only show batsmen who played
            print(f"{name:<12} {stats['runs']:<6} {stats['balls']:<6}")
    print(f"Total: {team['runs']}/{team['wickets']} in {team['balls']} balls ({team['balls']//6}.{team['balls']%6} overs)")
    print(f"Overs Runs: {team['overs_runs']}")
    print(f"Fall of Wickets: {team['fall_of_wicket']}")

# --- Simulate Match ---
print("\n--- First Inning ---")
play_inning(team1)

print("\n--- Second Inning ---")
play_inning(team2, target=team1["runs"])

# --- Print Scorecards ---
print_scorecard(team1)
print_scorecard(team2)

# --- Determine Winner ---
if team2["runs"] >= team1["runs"] and team2["wickets"] < 10:
    print(f"\nWinner: {team2['name']} by {10 - team2['wickets']} wickets")
elif team1["runs"] > team2["runs"]:
    print(f"\nWinner: {team1['name']} by {team1['runs'] - team2['runs']} runs")
else:
    print("\nMatch Tied!")