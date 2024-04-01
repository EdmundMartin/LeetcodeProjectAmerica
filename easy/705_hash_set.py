
class MyHashSet:

    def __init__(self):
        self.buckets = 10_000
        self.hash_set = [None] * self.buckets

    def add(self, key: int) -> None:
        bucket = hash(key) % self.buckets
        if self.hash_set[bucket] is None:
            self.hash_set[bucket] = [key]
        else:
            items = self.hash_set[bucket]
            for item in items:
                if key == item:
                    return
            self.hash_set[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = hash(key) % self.buckets
        val = self.hash_set[bucket]
        if val is None:
            return
        remove_idx = -1
        for idx, item in enumerate(val):
            if item == key:
                remove_idx = idx
                break
        if remove_idx == -1:
            return
        val.remove(key)

    def contains(self, key: int) -> bool:
        bucket = hash(key) % self.buckets
        val = self.hash_set[bucket]
        if val is None:
            return False
        for item in val:
            if key == item:
                return True
        return False
