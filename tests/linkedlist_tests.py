import unittest

from ds import LinkedList


class LinkedListTests(unittest.TestCase):

    # method name has to start with test for the framework to run the test
    def test_create_empty_list(self):
        llist = LinkedList()
        self.assertEqual(0, llist.length())
        self.assertEqual("", str(llist))
        self.assertListEqual([], [x for x in llist])

    def test_append(self):
        llist = LinkedList()
        n = 10
        for i in range(0, n):
            llist.append(i)
            self.assertEqual(i, llist.at(i))
        for i in range(0, n):
            self.assertEqual(i, llist.at(i))
        self.assertEqual(n, llist.length())
        self.assertListEqual([x for x in range(0, n)], [x for x in llist])

    def test_appends(self):
        llist = LinkedList()
        n = 10
        llist.appends(range(0, int(n/2)))
        llist.appends(range(int(n/2), n))
        for i in range(0, n):
            self.assertEqual(i, llist.at(i))
        self.assertEqual(n, llist.length())
        self.assertListEqual([x for x in range(0, n)], [x for x in llist])

    def test_inserts(self):
        llist = LinkedList()
        n = 10
        for i in range(0, int(n/2)):
            llist.insert(i, 2*i)
        for i in range(1, n, 2):
            llist.insert(i, i)
        self.assertListEqual([x for x in range(0, n)], [x for x in llist])

    def test_remove(self):
        llist = LinkedList()
        n = 10
        llist.appends(range(0, n))
        for i in range(0, n):
            llist.remove(0)
        self.assertEqual(0, llist.length())
        llist.appends(range(0, n))
        for i in range(n-1, -1, -1):
            llist.remove(i)
        llist.append(range(0, n))

    def test_at_invalid_pos(self):
        llist = LinkedList()
        n = 10
        llist.appends(range(0, n))
        with self.assertRaises(Exception) as cm:
            llist.at(n)
        self.assertEqual("10 is out of range, valid range [0, 9]", str(cm.exception))

    def test_insert_at_invalid_pos(self):
        llist = LinkedList()
        n = 10
        llist.appends(range(0, n))
        llist.insert(n, n)
        with self.assertRaisesRegex(Exception, f'.*position {n+2}.*'):
            llist.insert(n+2, n+2)


if __name__ == '__main__':
    unittest.main()
