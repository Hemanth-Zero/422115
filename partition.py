from itertools import combinations
from collections import defaultdict


def apriori_partition(partition, min_support, total_transactions):
    item_count = defaultdict(int)
    for transaction in partition:
        for item in transaction:
            item_count[frozenset([item])] += 1

    freq_items = {
        item for item, count in item_count.items()
        if count / total_transactions >= min_support
    }

    all_freq = list(freq_items)
    k = 2
    
    while freq_items:
        candidates = set()
        freq_items_list = list(freq_items)

        for i in range(len(freq_items_list)):
            for j in range(i + 1, len(freq_items_list)):
                union = freq_items_list[i] | freq_items_list[j]
                if len(union) == k:
                    candidates.add(union)

  
        candidate_count = defaultdict(int)
        for transaction in partition:
            for candidate in candidates:
                if candidate.issubset(transaction):
                    candidate_count[candidate] += 1

        freq_items = {
            item for item, count in candidate_count.items()
            if count / total_transactions >= min_support
        }

        all_freq.extend(freq_items)
        k += 1

    return set(all_freq)



def apriori_by_partition(dataset, min_support, num_partitions=2):
    n = len(dataset)
    partition_size = n // num_partitions

    partitions = [
        dataset[i:i + partition_size]
        for i in range(0, n, partition_size)
    ]

    global_candidates = set()
    for part in partitions:
        local_freq = apriori_partition(part, min_support, n)
        global_candidates |= local_freq

  
    final_count = defaultdict(int)
    for transaction in dataset:
        for candidate in global_candidates:
            if candidate.issubset(transaction):
                final_count[candidate] += 1

    final_freq = {
        item for item, count in final_count.items()
        if count / n >= min_support
    }

    return final_freq


dataset = [
    {'A', 'B', 'C'},
    {'A', 'C'},
    {'A', 'D'},
    {'B', 'C'},
    {'A', 'B', 'C', 'D'},
    {'B', 'C'}
]

min_support = 0.3

result = apriori_by_partition(dataset, min_support, num_partitions=2)

print("Frequent Itemsets:")
for item in result:
    print(set(item))