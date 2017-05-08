from avl_tree import AVLTree, Node
import unittest 

class NodeTest(unittest.TestCase):

	def test_init(self):
		data = 'a'
		n = Node(data)
		assert n.data == 'a'
		assert n.left_child is None
		assert n.right_child is None


class AVLTreeTest(unittest.TestCase):

	def test_init(self):
		avl_tree = AVLTree()
		assert avl_tree.root is None 
	
	def test_init_with_iterable(self):
		data = [1, 2, 3]
		avl_tree = AVLTree(data)
		assert avl_tree.root == 2
		assert avl_tree.root.left_child == 1
		assert avl_tree.root.right_child == 3