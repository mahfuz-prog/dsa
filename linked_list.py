class Node:
	def __init__(self, data=None, next=None):
		# data for the node
		self.data = data

		# reference to the next node
		self.next = next


class SinglyLinkedList:
	def __init__(self, values=None):
		self.head = None
		if values is not None:
			self.create_list(values)

	def create_list(self, values):
		"""Helper method to create a linked list from a list of values."""
		if not values:
			return

		# Create the head node
		self.head = Node(values[0])
		current = self.head

		# Iterate through the remaining values and create nodes
		for value in values[1:]:
			current.next = Node(value)
			current = current.next


	# add a note to the end
	def append(self, data):
		# create the Node object
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_node


	# add element at index
	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node


	# pop
	def pop(self, idx=-1):
		if self.head is None:
			raise IndexError("Pop from empty list")

		# handle negetive indices
		if idx < 0:
			idx += len(self)
			# still the index is < 0
			if idx < 0:
				raise IndexError("Index out of range")

		# idx out of maximum range
		if idx >= len(self):
			raise IndexError("Index out of range")


		# pop elements given index or last
		current = self.head
		current_idx = 0
		prev_node = None
		while current:
			if idx == current_idx:
				if prev_node:
					prev_node.next = current.next
				else:
					self.head = current.next
				return current.data
			
			prev_node = current
			current = current.next
			current_idx += 1

	# reverse
	def reverse(self):
		# current = self.head
		# prev_node = None
		# while current:
		# 	temp = current.next
		# 	current.next = prev_node
		# 	prev_node = current
		# 	current = temp
		# self.head = prev_node

		def recursive(head):
			if head is None or head.next is None:
				return head

			new_head = recursive(head.next)

			# backtrack
			# next_head = head.next
			# next_head.next = head

			head.next.next = head
			head.next = None
			
			return new_head

		new_head = recursive(self.head)
		self.head = new_head


	# =====================================================
	# get by index
	def __getitem__(self, idx):
		# handle negetive indices
		if idx < 0:
			idx += len(self)
			# still the index is < 0
			if idx < 0:
				raise IndexError("Index out of range")

		# idx out of maximum range
		if idx >= len(self):
			raise IndexError("Index out of range")

		current = self.head
		current_idx = 0
		while current:
			if current_idx == idx:
				return current.data
			current = current.next
			current_idx += 1


	# length
	def __len__(self):
		total = 0
		current = self.head
		while current:
			total += 1
			current = current.next
		return total


	# print
	def __repr__(self):
		ele = []
		current = self.head
		while current:
			ele.append(current.data)
			current = current.next
		return f"SinglyLinkedList -> {ele}"

# create obj
lst = SinglyLinkedList()

# append data
lst.append(5)
lst.append(6)
lst.append(1)
lst.append(3)

# add data to the front
lst.prepend(2)
lst.prepend(4)

# print
print(lst)

# length of the list
print("Length ->", len(lst))

# get by index
print("Indexing ->",lst[0])

# pop
pop = lst.pop()
print("pop ->", pop)
print(lst)

lst.reverse()
print(lst)

# ==============================================
# marge 2 sorted list

a = SinglyLinkedList([1,3,5,8])
b = SinglyLinkedList([2,3,6,7])

def marge(head1, head2):
	# base case if a list end
	# we will return the other list head
	if head1 is None:
		return head2
	
	if head2 is None:
		return head1

	if head1.data <= head2.data:
		head1.next = marge(head1.next, head2)
		return head1
	else:
		head2.next = marge(head1, head2.next)
		return head2

head = marge(a.head, b.head)

while head:
	print(head.data)
	head = head.next