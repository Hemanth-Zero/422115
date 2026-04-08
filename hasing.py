from itertools import combinations
from collections import defaultdict

def hash_func(pair, bucket_size):
    return (hash(pair[0]) ^ hash(pair[1])) % bucket_size


def apriori_hashing(dataset, min_support, bucket_size=10):

    item_count = defaultdict(int)
    for transaction in dataset:
        for item in transaction:
            item_count[item] += 1

    n = len(dataset)

    L1 = {item for item, count in item_count.items()
          if count / n >= min_support}

    bucket_count = defaultdict(int)

    for transaction in dataset:
        valid_items = [item for item in transaction if item in L1]

        for pair in combinations(valid_items, 2):
            h = hash_func(pair, bucket_size)
            bucket_count[h] += 1


    frequent_buckets = {
        b for b, count in bucket_count.items()
        if count / n >= min_support
    }


    C2 = set()

    for transaction in dataset:
        valid_items = [item for item in transaction if item in L1]

        for pair in combinations(valid_items, 2):
            h = hash_func(pair, bucket_size)
            if h in frequent_buckets:
                C2.add(pair)

    pair_count = defaultdict(int)

    for transaction in dataset:
        for pair in combinations(transaction, 2):
            if pair in C2:
                pair_count[pair] += 1

    L2 = {pair for pair, count in pair_count.items()
          if count / n >= min_support}

    return L1, L2



dataset = [
    ['A', 'B', 'C'],
    ['A', 'C'],
    ['A', 'D'],
    ['B', 'C'],
    ['A', 'B', 'C', 'D'],
    ['B', 'C']
]

L1, L2 = apriori_hashing(dataset, min_support=0.3)

print("L1:", L1)
print("L2:", L2)