sentences = [
    "Peter Parker works at White House",
    "Sharon Floyd flew to Miami last Friday",
    "Apple is buying a startup in London",
    "Many French citizens are going to visit Morocco for summer",
    "White House announced new policy on Sunday morning"
]

labels = [
    "B-PER I-PER O O B-ORG I-ORG",
    "B-PER I-PER O O B-LOC O B-TIM I-TIM",
    "B-ORG O O O O B-LOC",
    "O B-LOC O O O O B-LOC O O",
    "B-ORG I-ORG O O O B-TIM I-TIM"
]


# Tag mapping
tag_map = {
    "O": 0,
    "B-PER": 1, "I-PER": 2,
    "B-ORG": 3, "I-ORG": 4,
    "B-LOC": 5, "I-LOC": 6,
    "B-TIM": 7, "I-TIM": 8
}
