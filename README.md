# pycounts_elshaday

Calculate word counts in a text file!

## Installation

```bash
$ pip install pycounts_elshaday
```

## Usage

After installation, you can use the package as follows:

```python
from pycounts_elshaday.pycounts_elshaday import count_words
from pycounts_elshaday.plotting import plot_words

# Count the words in a text file
counts = count_words("yourfile.txt")

# Plot the top 10 words
plot_words(counts, n=10)


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pycounts_elshaday` was created by Elshaday Yoseph. It is licensed under the terms of the MIT license.

## Credits

`pycounts_elshaday` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
