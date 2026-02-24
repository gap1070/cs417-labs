"""
Lab 9: Tombstone Tests — YOU WRITE THESE.

Each test function has a description of what to test.
Your job is to write the implementation. Use the tests in
test_hash_table.py as examples for how to write assertions.

Run your tests:
    pytest -v -k "TestTombstones"
"""

from hash_table_open import HashTableOpen


class TestTombstones:
    """Tests that tombstones keep the hash table working correctly."""

    def test_probe_chain_survives_deletion(self):
        ht = HashTableOpen(size=3)
        # adds everything 
        ht.put("a", 1)
        ht.put("b", 2)
        ht.put("c", 3)
        # deletes middle key 
        ht.delete("b")
        # retrieves key 3, and sees if last key is still able to reach 
        assert ht.get("c") == 3 
        assert "c" in ht 

    def test_tombstone_slot_reused_on_insert(self):
        ht = HashTableOpen(size=3)
        # puts table together
        ht.put("a", 100)
        # deletes key
        ht.delete("a")
        # checks if anything 
        assert len(ht) == 0 
        # inserts new key 
        ht.put("b", 200)
        # checks if worked 
        assert ht.get("b") == 200 
        assert len(ht) == 1 

    def test_count_correct_through_delete_and_reinsert(self):
        ht = HashTableOpen(size=5)
        # creates table
        ht.put("a", 1)
        ht.put("b", 2)
        ht.put("c", 3)
        # checks length
        assert len(ht) == 3
        # deletes second key 
        ht.delete("b")
        assert len(ht) == 2
        # puts another key 
        ht.put("b", 22)
        assert len(ht) == 3 
        assert ht.get("b") == 22 
        # delete first and last key 
        ht.delete("a")
        ht.delete("c")
        # checks final length 
        assert len(ht) == 1 