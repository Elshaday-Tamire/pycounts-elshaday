import matplotlib.pyplot as plt

def plot_words(word_counts, n=10):
    """Plot a bar chart of word counts."""
    top_n_words = word_counts.most_common(n)
    words, counts = zip(*top_n_words)
    plt.bar(words, counts)
    plt.xticks(rotation=45)
    plt.xlabel("Words")
    plt.ylabel("Counts")
    plt.title("Word Counts")
    plt.show()
