
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
		
	def update_height(self):
		# not sure if this is correct
		if not self.right_child and not self.left_child:
			self.height = 0
		elif not self.right_child:
			self.height = (self.left_child.height + 1)
		elif not self.left_child:
			self.height = (self.right_child.height + 1)
		else:	
			self.height = (max(self.left_child.height, self.right_child.height) + 1)



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
			elif current.data > data:
				current = current.left_child
				continue
			elif current.data < data:
				current = current.right_child
				continue
		raise ValueError('%s not found in tree.' % (data))

	
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
				raise ValueError('%s already in tree.' % (data))
			elif current.data > data:
				if not current.left_child:
					current.left_child = n
					n.parent = current
					# update heights of parents and rotate if needed
					self.retrace_loop(n)
					return 
				else: 
					current = current.left_child
					continue
			elif current.data < data:
				if not current.right_child:
					current.right_child = n
					n.parent = current
					# update heights of parents and rotate if needed
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
				if current.left_child:			
					# check the left child of current to see if it's right heavy 
					left_child_balance_factor = current.left_child.balance_factor()
					if left_child_balance_factor > 1:
						# left right 
						self.left_rotation(current.left_child)
						self.right_rotation(current)
				else:
					# right
					self.right_rotation(current)

			elif balance_factor > 1:
				# right heavy
				if current.right_child:
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
			raise ValueError('%s not found in tree.' % (node))

	def delete(self, node):
		pass

	# def rebalance_necessary(self, node):
	# 	return balance_factor(node) >= 1 

	def left_rotation(self, node):
		# o    // node 
		#  \
		#   o  // node.right_child
		#    \
		# 	  o

		# nodes right child becomes parent, node becomes left child
		new_left_child = node 
		new_parent = node.right_child

		new_parents_parent = node.parent 

		if node.data > new_parents_parent.data:
			new_parents_parent.right_child = new_parent
		else: 
			new_parents_parent.left_child = new_parent

		new_parent.left_child = new_left_child
		new_left_child.parent = new_parent


	def right_rotation(self, node):
		# 	  o // node
		#    /
		#   o   // node.left_child
		#  /
		# o

		# nodes left child becomes parent, node becomes right child

		new_right_child = node 
		new_parent = node.left_child

		new_parents_parent = node.parent
		if new_parents_parent is None:
			# new_parent is becoming the tree's root
			self.root = new_parent
		else:
			# check to see if this is the left or right child of the parent node
			if node.data > new_parents_parent.data:
				new_parents_parent.right_child = new_parent
			else: 
				new_parents_parent.left_child = new_parent

		new_parent.right_child = new_right_child
		new_right_child.parent = new_parent


if __name__ == "__main__":
	pass


