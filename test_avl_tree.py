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
		data = [1, 2]
		avl_tree = AVLTree(data)
		assert avl_tree.root.data == 1
		assert avl_tree.root.right_child.data == 2

	def test_single_left_rotation(self):
		data = [1, 2, 3]
		avl_tree = AVLTree(data)
		assert avl_tree.root.data == 2
		assert avl_tree.root.left_child.data == 1
		assert avl_tree.root.right_child.data == 3
		assert avl_tree.items_level_order() == [2, 1, 3]

	def test_single_right_rotation(self):
		data = [3, 2, 1]
		avl_tree = AVLTree(data)
		assert avl_tree.root.data == 2
		assert avl_tree.root.left_child.data == 1
		assert avl_tree.root.right_child.data == 3
		assert avl_tree.items_level_order() == [2, 1, 3]

	def test_left_right_rotation(self):
		data = [1, 4, 8, 12, 16, 20, 25, 30, 35, 28]
		avl_tree = AVLTree(data)
		assert avl_tree.root.data == 12
		assert avl_tree.items_level_order() == [12, 4, 25, 1, 8, 20, 30, 16, 28, 35]
		# data = [1, 8, 4]
		# avl_tree = AVLTree(data)
		# assert avl_tree.root.data == 4
		# assert avl_tree


	def test_right_left_rotation(self):
		data = [8, 1, 4]
		avl_tree = AVLTree(data)
		assert avl_tree.root.data == 4
		assert avl_tree.items_level_order() == [4, 1, 8]
		# data = [10, 20, 30, 40, 50]
		


