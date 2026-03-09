# ============================================================
#         THE ULTIMATE WORD FREQUENCY ANALYZER
# ============================================================

text = """
Artificial intelligence is transforming the world at an unprecedented pace. 
Machine learning algorithms can now recognize faces, translate languages, 
diagnose diseases, and even compose music. Deep learning models trained on 
massive datasets have achieved superhuman performance on tasks that once 
seemed impossible for computers. Neural networks power recommendation systems 
that suggest what movies to watch, what products to buy, and what news to read. 
Natural language processing allows machines to understand human speech and text 
with remarkable accuracy. Self-driving cars use computer vision and sensor fusion 
to navigate complex roads safely. Robots equipped with artificial intelligence 
can perform delicate surgeries with precision beyond human capability. Scientists 
use machine learning to discover new drugs, predict climate patterns, and unlock 
secrets of the universe. However, artificial intelligence also raises important 
ethical questions about privacy, job displacement, and algorithmic bias. Society 
must carefully consider how these powerful technologies shape our future. Education 
systems need to prepare students for careers that do not yet exist. Governments 
around the world are developing policies to regulate artificial intelligence 
responsibly. Despite challenges, artificial intelligence holds enormous promise 
for solving humanity greatest problems including poverty, climate change, and disease.
"""

stop_words = ['the', 'a', 'an', 'is', 'in', 'to', 'and', 'of', 'for',
              'it', 'on', 'that', 'with', 'was', 'are', 'be', 'as', 'at']

# ============================================================
#                     FUNCTIONS
# ============================================================

def clean_word(word):
    """Remove punctuation from word"""
    cleaned = ""
    for ch in word:
        if ch.isalpha() or ch == "'":
            cleaned += ch
    return cleaned.lower()

def count_sentences(text):
    """Count sentences by . ! ? """
    count = 0
    for ch in text:
        if ch in '.!?':
            count += 1
    return count

def get_all_words(text):
    """Return list of all cleaned words"""
    raw_words = text.split()
    words = []
    for w in raw_words:
        cleaned = clean_word(w)
        if cleaned:
            words.append(cleaned)
    return words

def build_frequency_dict(words):
    """Count frequency of each word"""
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def remove_stop_words(freq_dict):
    """Remove stop words from frequency dict"""
    filtered = {}
    for word, count in freq_dict.items():
        if word not in stop_words:
            filtered[word] = count
    return filtered

def top_10(freq_dict):
    """Get top 10 most frequent words — manual sorting"""
    items = list(freq_dict.items())

    # Bubble sort by frequency (descending)
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j][1] < items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]

    return items[:10]

def longest_shortest(words):
    """Find longest and shortest words"""
    longest = ""
    shortest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
        if len(word) < len(shortest):
            shortest = word
    return longest, shortest

def avg_word_length(words):
    """Calculate average word length"""
    total = 0
    for word in words:
        total += len(word)
    return total / len(words)

def bar_chart(top_words):
    """Print text-based bar chart using # """
    print("\n" + "="*55)
    print("          WORD FREQUENCY BAR CHART")
    print("="*55)
    max_count = top_words[0][1]  # highest freq (already sorted)

    for word, count in top_words:
        # scale bar to max 30 #
        bar_len = int((count / max_count) * 30)
        bar = '#' * bar_len
        print(f"  {word:<18} | {bar:<30} {count}")

    print("="*55)

# ============================================================
#                     MAIN ANALYSIS
# ============================================================

print("\n" + "="*55)
print("        ULTIMATE WORD FREQUENCY ANALYZER")
print("="*55)

# --- Step 1: Get all words
all_words   = get_all_words(text)
total_words = len(all_words)
total_sents = count_sentences(text)

# --- Step 2: Frequency dict
freq_dict    = build_frequency_dict(all_words)
unique_words = len(freq_dict)

# --- Step 3: Basic Stats
print(f"\n   BASIC STATISTICS")
print(f"  {'Total Words':<22}: {total_words}")
print(f"  {'Total Sentences':<22}: {total_sents}")
print(f"  {'Unique Words':<22}: {unique_words}")

# --- Step 4: Longest & Shortest
longest, shortest = longest_shortest(all_words)
avg_len = avg_word_length(all_words)

print(f"\n   WORD LENGTH STATS")
print(f"  {'Longest Word':<22}: {longest} ({len(longest)} chars)")
print(f"  {'Shortest Word':<22}: {shortest} ({len(shortest)} chars)")
print(f"  {'Average Length':<22}: {avg_len:.2f} chars")

# --- Step 5: Top 10 (no stop words)
filtered_freq = remove_stop_words(freq_dict)
top_words     = top_10(filtered_freq)

print(f"\n   TOP 10 MOST FREQUENT WORDS")
print(f"  {'Rank':<6} {'Word':<20} {'Count'}")
print("  " + "-"*35)
for rank, (word, count) in enumerate(top_words, 1):
    print(f"  {rank:<6} {word:<20} {count}")

# --- Step 6: Bar Chart
bar_chart(top_words)
