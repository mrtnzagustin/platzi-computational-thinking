import unittest


def is_old_person(age):
    if age >= 18:
        return True
    else:
        return False


class CrystalBoxTest(unittest.TestCase):

    def test_old(self):
        age_1 = 20
        result = is_old_person(age_1)

        self.assertEqual(result, True)

    def test_young(self):
        age_1 = 17
        result = is_old_person(age_1)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
