# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1=[]
        
        while(l1):
            num1.append(l1.val)
            l1 = l1.next
        
        number1 = ""
        for i in range(0,len(num1)):
            number1 = number1+ str(num1[len(num1)-1-i])
            
    
        num2=[]
        value = l2.val
        while(l2):
            num2.append(l2.val)
            l2 = l2.next
        
        number2 = ""
        for i in range(0,len(num2)):
            number2 = number2+ str(num2[len(num2)-1-i])
            
        
        no1 = int(number1)
        no2 = int(number2)
        
        sumOut = no1+no2
        
        result = list(map(int, str(sumOut)[0::]))
        temp = None
        for val in result:
            node = ListNode(val)
            node.next = temp
            temp = node
            
        return node