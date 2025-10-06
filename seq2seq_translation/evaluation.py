from collections import Counter

def rouge1_similarity(candidate,reference):
  candidate_counts = Counter(candidate)
  reference_counts = Counter(reference)
  overlap = sum(min(candidate_counts[t], reference_counts[t]) for t in candidate_counts)
  precision = overlap/len(candidate) if candidate else 0
  recall = overlap/len(reference) if reference else 0
  return (2*precision*recall)/(precision+recall) if (precision + recall) else 0

def average_overlap(samples,similarity_fn):
  scores = {}
  for i, candidate in enumerate(samples):
    overlap = 0
    for j, sample in enumerate(samples):
      if i == j:
        continue
      overlap+=similarity_fn(candidate,sample)
    scores[i] = round(overlap/len(samples)-1,3)
  return scores