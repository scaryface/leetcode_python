import json
from typing import List

class KConsecutiveNums:

    class Node:
        def __init__(self, val, left, right):
            self.val = val
            self.left = left
            self.right = right

    def nums_same_consec_diff(self, N: int, K: int) -> List[int]:
        num_arr = []
        for i in range(1, 10):
            root = KConsecutiveNums.Node(i, None, None)
            curr_node = KConsecutiveNums.__generate_tree__(self, root, K, 0, N-1)
            curr_nums = []
            KConsecutiveNums.__node_dfs__(self, curr_node, 0, curr_nums, 0, N-1)
            print("curr_nums " , curr_nums)
            num_arr.extend(curr_nums)
        return num_arr

            
    def __generate_tree__(self, root, diff, curr_height, max_height):
        curr_root = root
        #print(root.val)
        if(curr_height > max_height):
            return   
        left_val = curr_root.val - diff
        right_val = curr_root.val + diff
        if(left_val >= 0 and left_val < 10):
            root.left = KConsecutiveNums.Node(left_val, None, None)
            KConsecutiveNums.__generate_tree__(self, curr_root.left, diff, curr_height+1, max_height)
        if(right_val >= 0 and right_val < 10):
            root.right = KConsecutiveNums.Node(right_val, None, None)
            KConsecutiveNums.__generate_tree__(self, curr_root.right, diff, curr_height+1, max_height)
        return root

    def __node_dfs__(self, node, prev_num, num_arr, curr_height, max_height):
        if(node == None):
            return
        prev_num = prev_num*10 + node.val
        if(curr_height == max_height):
            num_arr.append(prev_num)
            return
        left_node = node.left
        right_node = node.right
        KConsecutiveNums.__node_dfs__(self, left_node, prev_num, num_arr, curr_height+1, max_height)
        KConsecutiveNums.__node_dfs__(self, right_node, prev_num, num_arr, curr_height+1, max_height)     
        

    
ans = KConsecutiveNums()

# Test generate tree
node = KConsecutiveNums.Node(6, None, None)
root = ans.__generate_tree__(node, 2, 0, 2)

# Test DFS
num_arr = []
ans.__node_dfs__(root, 0, num_arr, 0, 2)
print(num_arr)

print(ans.nums_same_consec_diff(3, 7))