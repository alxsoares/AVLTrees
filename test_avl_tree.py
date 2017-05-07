from avl_tree import AVLTree, Node
import unittest 

class NodeTest(unittest.TestCase):

	def test_init(self):
		data = 'a'
		n = Node(data)
		assert n.data = 'a'
		assert n.left_child is None
		assert n.right_child is None


class AVLTreeTest(unittest.TestCase):

	def test_init(self):
		avl_tree = AVLTree()
		assert self.root is None 
	
	def test_init_with_iterable(self):
		data = ['a', 'b', 'c']
		avl_tree = AVLTree(data)
		assert self.root == 'b'
		assert self.root.left_child == 'a'
		assert self.root.right_child == 'c'