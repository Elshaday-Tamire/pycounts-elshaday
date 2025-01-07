from pycounts_elshaday.plotting import plot_words
from collections import Counter

def test_plot_words():
    """Test that plot_words creates a plot without errors."""
    word_counts = Counter({"beautiful": 1, "is": 2, "better": 2, "than": 2})
    try:
        plot_words(word_counts)
    except Exception as e:
        assert False, f"plot_words() raised an exception: {e}"
