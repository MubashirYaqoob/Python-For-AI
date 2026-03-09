logs = [
    {"member": "Farrukh",  "task": "did intro slide only lol",        "commits": 1},
    {"member": "Mahnoor",  "task": "wrote entire report please check", "commits": 11},
    {"member": "Junaid",   "task": "bhai kab submit hai",              "commits": 0},
    {"member": "Farrukh",  "task": "made cover page font bigger",      "commits": 1},
    {"member": "Asad",     "task": "main tha hi nahi yaar",            "commits": 0},
    {"member": "Mahnoor",  "task": "DOING EVERYTHING ALONE AGAIN!!",   "commits": 22},
    {"member": "Junaid",   "task": "reviewed mahnoor ka kaam thx",     "commits": 2},
    {"member": "Farrukh",  "task": "ok submitted good teamwork guys",  "commits": 1},
]

total_commit = {}

for i in logs:
    member = i["member"]
    commit = i["commits"]
    total_commit[member] = total_commit.get(member, 0) + commit

# Most active
top = max(total_commit, key=total_commit.get)
print("Most Active:", top)

# Uski tasks
for i in logs:
    if i["member"] == top:
        print(i["task"])  # seedha print!

keyword = "bhai"
count = 0
for i in logs :
    task = i["task"]

    if keyword.lower() in task.lower():
        count += 1

print(count)


def find_logs(log,kewword) :
    for i in logs:
        member = i["member"]
        task =i["task"]

        if keyword.lower() in task.lower() :
            print(member.upper(), "-",task[:20] + "...")

def calculate_contribution_score(logs):
    scores = {}
    
    for i in logs:
        member  = i["member"]
        task    = i["task"]
        commits = i["commits"]   # Fix 1 ✅
        
        score = 0
        
        # 0 commits → -3
        if commits == 0:
            score += -3
            
        # ALL CAPS → +6
        if task.isupper():       # Fix 2 ✅
            score += 6
            
        # per commit → +2
        score += commits * 2     # Fix 3 ✅
            
        # task > 30 chars → +4
        if len(task) > 30:
            score += 4
            
        # "?" in task → +0
        if "?" in task:
            score += 0
        
        scores[member] = scores.get(member, 0) + score
    
    # Sort highest to lowest
    sorted_scores = sorted(scores.items(),  # Fix 4 ✅
                    key=lambda x: x[1], 
                    reverse=True)
    
    for rank, (member, score) in enumerate(sorted_scores, start=1):
        print(f"#{rank} {member} → Score: {score}")

calculate_contribution_score(logs)
