from collections import defaultdict
from collections import Counter


text = """A press release is the quickest and easiest way to get free publicity. If 
well written, a press release can result in multiple published articles about your 
firm and its products. And that can mean new prospects contacting you asking you to 
sell to them. ….""".lower().split()

#defaultdict
word_count = defaultdict(lambda: 0) # Default 값을 0으로 설정합
for word in text:
    word_count[word] += 1

for i, v in word_count.items():
    print(i, v)
print()

#counter
print(Counter(text))
print(Counter(text)['the'])