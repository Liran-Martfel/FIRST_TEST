def most_common_word(story: tuple[str, ...]) -> str:
    all_words = []
    for sentence in story:
        for word in sentence.split():
            word = word.lower().strip('.,?')
            all_words.append(word)

    dict1 = {}
    for word in set(all_words):
        dict1[word] = all_words.count(word)
    best_word = max(dict1, key=dict1.get)
    count = dict1[best_word]

    return f'the word is: "{best_word}" \nand it has been showed: {count} times'

story = (
    "The little fox saw the little bird and the little cat.",
    "The fox was happy because the little bird sang, and the little cat jumped.",
    "The little fox, the little bird, and the little cat became friends."
)

print(most_common_word(story))