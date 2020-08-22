import json
import os


class ReorderList:
    
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def rorder_list(self, head: ListNode) -> None:

        fast, slow = head, head
        if(head == None or head.next == None):
            return head

        # get mid of node list
        while(fast.next):
            fast = fast.next.next
            if(not fast):
                break
            slow = slow.next

        #reverse the right node
        right_nodes = slow.next
        prev_node = right_nodes
        # split into halves
        slow.next = None
        curr_node = right_nodes.next
        # remove mid -> mid + 1 relation
        prev_node.next = None
        while(curr_node):
            temp_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp_node
        # ReorderList.print_nodes(self, prev_node)
        # ReorderList.print_nodes(self, head)
        # Merge both rows
        right_nodes = prev_node
        left_nodes = head
        while(right_nodes and left_nodes):
            next_left_node = left_nodes.next
            next_right_node = right_nodes.next
            left_nodes.next = right_nodes
            right_nodes.next = next_left_node
            left_nodes = next_left_node
            right_nodes = next_right_node
        return head
        

    # O(n) space O(n) time
    def rorder_list_02(self, head: ListNode) -> None:
        node_list = []
        iter_node = head
        while(iter_node != None):
            node_list.append(iter_node)
            iter_node = iter_node.next
        n = len(node_list)
        for i, val in enumerate(node_list):
            if(i == n//2):
                val.next = None
                break
            temp_node = val.next
            val.next = node_list[n-i-1]
            node_list[n-i-1].next = temp_node
            print(i, val.val, val.next.val)
        return head

    def print_nodes(self, head):
        prev_node = head
        while(prev_node):
            print(prev_node.val)
            prev_node = prev_node.next

ans = ReorderList()
node_len = 6
head = ans.ListNode(1, None)
prev_node = head
for i in range(1, node_len):
    curr_node = ans.ListNode(i+1, None)
    prev_node.next = curr_node
    prev_node = curr_node

#ans.print_nodes(head)
ans.rorder_list(head)
print("-----------------")
ans.print_nodes(head)