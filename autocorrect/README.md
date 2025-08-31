# AutoCorrector 🔠

A simple autocorrect engine built using Minimum Edit Distance algorithm (Levenshtein distance).

## Features

- Suggests top-k corrections for a misspelled word
- Based on dynamic programming edit distance
- CLI interface
- Easy to extend with a larger dictionary or probability model

## Usage

```bash
python cli.py --word teh
```

example:

```
> python cli.py --word rahl
Suggestions:
1. rah
2. rahul
3. rail

> python cli.py --word parot
Suggestions:
1. parol
2. parrot
3. part

 > python cli.py --word convolutionl
Suggestions:
1. convolution
2. convolutional
3. consolation
```
