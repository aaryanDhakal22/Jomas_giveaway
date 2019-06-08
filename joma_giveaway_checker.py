import requests

results = list()
final_words = list()


f = open("sample_transcript.txt", 'r')
p = open('preps.txt', 'r')
final_result = list()

p_contents = [items.strip('\n') for items in p.readlines()]
f_contents = f.readlines()

for counter, items in enumerate(f_contents):
    if counter % 2 == 0:
        results.append(items.replace("\n", ''))


for items in results:
    words = items.split()
    final_words.extend(words)


for items in final_words:
    if items not in p_contents:
        final_result.append(items)


for hints in final_result:
    res = requests.get('https://bit.ly/joma_'+hints)
    if res.status_code == 200:
        print(hints)
    else:
        print("Sorry")
