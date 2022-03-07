
from linked_list import LinkedList, Node


class DoublyLinkedList(LinkedList):
	SEPARATOR = "<->"

	def insert(self, node):

		if self.is_empty():
			self.head = node
		else:
			self.insert_check(node)
			curr = self.head
			while curr.nextval:
				curr = curr.nextval

			curr.nextval = node
			node.prev = curr

	def push(self):
		pass

	def delete(self):
		pass

    # def push(self):
    #     pass

	# def delete(self):
	# 	pass