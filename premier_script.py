import unittest
from typing import List

NAME_LENGTH_THRESHOLD = 7

def count_long_names(name_list: List[str]) -> int:
  
    long_names = [name for name in name_list if len(name) > NAME_LENGTH_THRESHOLD]

    # Affichage des prénoms longs
    for name in long_names:
        print(f"{name} est un prénom avec un nombre de lettres supérieur à {NAME_LENGTH_THRESHOLD}")

    return len(long_names)

# Test Unitaire
class TestCountLongNames(unittest.TestCase):
    def test_count_long_names(self):
        names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_long_names(names)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
