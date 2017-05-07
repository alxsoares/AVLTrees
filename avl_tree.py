
class Node(object):
	"""Nodes in binary search tree, specifically for AVL tree"""
	def __init__(self, data):
		self.data = data
		self.height = 0
		self.parent = None
		self.left_child = None
		self.right_child = None

	def is_leaf(self):
		return (self.height == 0)

	def balance_factor(self):
		return (self.left_child.height if self.left_child else -1) - (self.right_child.height if self.right_child else -1)
		
	def update_height(self, node):
		# not sure if this is correct
		if not node.right_child and not node.left_child:
			self.height = 0
		else if not node.right_child:
			self.height = (node.left_child.height + 1)
		else if not node.left_child:
			self.height = (node.right_child.height + 1)
		else:	
			self.height = (max(node.left_child.height, node.right_child.height) + 1)



class AVLTree(object):
	"""AVLTree, a self balancing binary search tree where the heights of each child node do not differ by more than 1"""
	def __init__(self, iterable=None):
		self.root = None
		if iterable:
			for item in iterable:
				self.insert(item)

	def find(self, data):
		current = self.root
		while current is not None:
			if current.data == data:
				return current
			else if current.data > data:
				current = current.left_child
				continue
			else if current.data < data:
				current = current.right_child
				continue
		raise ValueError, '%s not found in tree.' % (data)

	
	def insert(self, data):
		# find location to insert data into bst 
		n = Node(data)
		if self.root is None:
			self.root = n 
			return 

		current = self.root
		while current is not None:
			if current.data == data:
				# do nothing? raise error?
				raise ValueError, '%s already in tree.' % (data)
			else if current.data > data:
				if not current.left_child:
					current.left_child = n
					n.parent = current
					# update heights of parents
					self.retrace_loop(n)
					return 
				else: 
					current = current.left_child
					continue
			else if current.data < data:
				if not current.right_child:
					current.right_child = n
					n.parent = current
					# update heights of parents
					self.retrace_loop(n)
					return 
				else:
					current = current.right_child
					continue


	def retrace_loop(self, node):
		current = node.parent
		while current is not None: 
			current.update_height()
			balance_factor = current.balance_factor()
			# will have to rotate on the way up, and the heights are going to change AHAHHHHAHHHHHHHHH 
			if balance_factor < -1:
				# left heavy
				
				# check the left child of current to see if it's right heavy 
				left_child_balance_factor = current.left_child.balance_factor()
				if left_child_balance_factor > 1:
					# left right 
					self.left_rotation(current.left_child)
					self.right_rotation(current)
				else:
					self.right_rotation(current)

			else if balance_factor > 1:
				# right heavy

				# check the right child of current to see if it's left heavy 
				right_child_balance_factor = current.right_child.balance_factor()
				if right_child_balance_factor < -1:
					# right left 
					self.right_rotation(current.right_child)
					self.left_rotation(current)
				else: 
					# left
					self.left_rotation(current)
			else: 
				# balanced
				pass
			current = current.parent

	def update(self, node, data):
		try: 
			n = self.find(node)
			n.data = data
		except ValueError:
			raise ValueError, '%s not found in tree.' % node

	def delete(self, node):
		pass

	# def rebalance_necessary(self, node):
	# 	return balance_factor(node) >= 1 

	def left_rotation(self, node):
		pass

	def right_rotation(self, node):
		pass

	



