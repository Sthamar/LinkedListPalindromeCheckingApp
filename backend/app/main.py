from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import json

app = FastAPI()

# define the linked list Node
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


# function to convert a list of values into a linked list
def create_linked_list(values: List[int]) -> ListNode:
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

@app.post("/check_palindrome")
async def check_palindrome(linked_list: List[int]):
    head = create_linked_list(linked_list)
    slow, fast = head, head
    steps = []
    
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
        
    if fast:
        slow = slow.next
    
    while slow:
        current_step = {
            "node": slow.val,
            "stack_top": stack[-1] if stack else None,
            "is_palindrome": False
        }
        
        if stack.pop() != slow.val:
            current_step["is_palinrome"] = False
            return {"is_palindrome": False, "steps": steps}
        current_step["is_palindrome"] = True
        steps.append(current_step)
        slow = slow.next
        
        return {"is_palindrome": True, "steps": steps}