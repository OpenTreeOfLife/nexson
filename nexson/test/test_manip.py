#! /usr/bin/env python
import unittest
import logging
from nexson.manip import count_num_trees, iter_trees
from nexson.test.support.pathmap import get_test_path_mapper as ntest_path_mapper

pathmap = ntest_path_mapper()

_LOG = logging.getLogger(__name__)

class TestManip(unittest.TestCase):
    def testCanCountTrees(self):
        for v in ['0.0', '1.0', '1.2']:
            inp = pathmap.nexson_obj('otu/v{v}.json'.format(v=v))
            self.assertEqual(1, count_num_trees(inp, v))

    def testIterTree(self):
        id_order_list = []
        f_list = ['expected', 'input']
        for v in ['1.0', '1.2']:
            for f in f_list:
                inp = pathmap.nexson_obj('merge/merge-{f}.v{v}.json'.format(v=v, f=f))
                id_order = []
                for t_tuple in iter_trees(inp):
                    ti = t_tuple[1]
                    id_order.append(ti)
                id_order_list.append(id_order)
        for i in range(1, 4):
            self.assertEqual(id_order_list[0], id_order_list[i])


if __name__ == "__main__":
    unittest.main()
