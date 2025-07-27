import os

def convert_to_12_hour_format(lines_count):
    if lines_count <= 12:
        return f"{lines_count} AM"
    else:
        return f"{lines_count - 12} PM"

def clean_word(word):
    return ''.join(ch for ch in word if ch.isalnum())

def process_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    lines_count = len(lines)
    meeting_time = convert_to_12_hour_format(lines_count)
    text = ' '.join(lines)
    words = text.split()
    freq = {}
    for w in words:
        w_clean = clean_word(w)
        if w_clean == '':
            continue
        w_lower = w_clean.lower()
        freq[w_lower] = freq.get(w_lower, 0) + 1
    max_word = max(freq, key=freq.get)
    meeting_place = max_word.capitalize() + " Street"
    print(f"\nFile: {filename}")
    print(f"Meeting time: {meeting_time}")
    print(f"Meeting place: {meeting_place}")

base_path = os.path.dirname(__file__)

for i in range(1, 3):
    filename = os.path.join(base_path, f"Sample{i}.txt")
    process_file(filename)
