# Example sentences
sentences = [
    "Apple is looking at buying U.K. startup for $1 billion",
    "San Francisco considers banning sidewalk delivery robots",
    "London is a big city in the United Kingdom"
]

# Corresponding NER tags (BIO format)
labels = [
    "B-ORG O O O B-LOC O O O O O",
    "B-LOC I-LOC O O O O O O",
    "B-LOC O O O O O B-LOC I-LOC"
]

# Tag mapping
tag_map = {
    "O": 0,
    "B-ORG": 1,
    "I-ORG": 2,
    "B-LOC": 3,
    "I-LOC": 4
}
