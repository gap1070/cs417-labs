"""
Lab 9: Open Addressing with Linear Probing

In this lab you will implement a hash table that uses open addressing
instead of separate chaining. Every item lives directly in the table
array — no lists of pairs, just one item per slot.

When a collision happens, you probe forward (linear probing) to find
the next available slot. Deletion uses tombstones to preserve probe chains.

Complete the four methods marked with TODO.
Do NOT change the method signatures or the __init__ method.

Run tests:
    pytest -v
"""

# Sentinel value for deleted slots. Do not modify.
_TOMBSTONE = object()


class HashTableOpen:
    """A hash table using open addressing with linear probing."""

    def __init__(self, size=10):
        """Create an empty hash table with the given number of slots."""
        self.size = size
        self.table = [None] * self.size
        self.count = 0

    # ── TODO 1: Hash Function ─────────────────────────────────────

    def _hash(self, key):
        return hash(key) % self.size 

    # ── TODO 2: Put ───────────────────────────────────────────────

    def put(self, key, value):
        start = self._hash(key)

        for step in range(self.size):
            index = (start + step) % self.size
            slot = self.table[index]

            # treats the tombstones just like other empty slots 
            if slot is None or slot is _TOMBSTONE:
                self.table[index] = (key, value)
                self.count += 1 
                return
            
            # updates the existing key
            if slot[0] == key:
                self.table[index] = (key, value)
                return

        raise Exception("Hash table is full")


    # ── TODO 3: Get ───────────────────────────────────────────────

    def get(self, key):
        start = self._hash(key)

        for step in range(self.size):
            index = (start + step) % self.size
            slot = self.table[index]

            # a slot is None if it was never placed 
            if slot is None:
                break

            # skips the tombstones
            if slot is _TOMBSTONE:
                continue

            if slot[0] == key:
                return slot[1]
            
        raise KeyError(key)

    # ── TODO 4: Delete ────────────────────────────────────────────

    def delete(self, key):
        """
        Remove a key-value pair by replacing it with a tombstone.

        Why not just set the slot to None? Because it would break probe
        chains — any keys that were placed AFTER this slot (due to
        collisions) would become unreachable.

        Algorithm:
            1. Start at _hash(key), probe forward (like get).
            2. If you find the matching key → replace with _TOMBSTONE,
               decrement self.count.
            3. If you hit None or exhaust the table → raise KeyError.

        Args:
            key: The key to remove.

        Raises:
            KeyError: If the key is not found.
        """
        start = self._hash(key)

        for step in range(self.size):
            index = (start + step) % self.size
            slot = self.table[index]

            # if a slots none, the key doesn't exist
            if slot is None:
                break

            # skips the tombstones
            if slot is _TOMBSTONE:
                continue

            # finds the key and replaces with tombstone 
            if slot[0] == key:
                self.table[index] = _TOMBSTONE
                self.count -= 1 
                return 
            
        raise KeyError(key)

    # ── Provided Methods (do not modify) ──────────────────────────

    def __len__(self):
        """Return the number of key-value pairs in the table."""
        return self.count

    def __contains__(self, key):
        """Support 'in' operator: key in table."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def load_factor(self):
        """Return the current load factor (items / slots)."""
        return self.count / self.size

    def __repr__(self):
        """Show a readable view of the hash table's internal state."""
        lines = []
        for i, slot in enumerate(self.table):
            if slot is None:
                lines.append(f"  [{i}] empty")
            elif slot is _TOMBSTONE:
                lines.append(f"  [{i}] TOMBSTONE")
            else:
                k, v = slot
                lines.append(f"  [{i}] {k!r}: {v!r}")
        return f"HashTableOpen({self.count} items, {self.size} slots):\n" + "\n".join(lines)