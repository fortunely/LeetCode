# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        cur1 = l1
        cur2 = l2
        l3 = None

        if cur1.val <= cur2.val:
            l3 = cur1
            cur1 = cur1.next
        else:
            l3 = cur2
            cur2 = cur2.next

        l3.next = None
        cur3 = l3

        print 'temp1'
        show_list(l3)

        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val:
                cur3.next = cur1
                cur1 = cur1.next
            else:
                cur3.next = cur2
                cur2 = cur2.next

            cur3 = cur3.next

        print 'temp2'
        show_list(l3)

        while cur1 != None:
            cur3.next = cur1
            cur1 = cur1.next
            cur3 = cur3.next

        print 'temp3'
        show_list(l3)

        while cur2 != None:
            cur3.next = cur2
            cur2 = cur2.next
            cur3 = cur3.next

        print 'temp4'
        show_list(l3)

        cur3.next = None

        return l3


def show_list(list):
    while list != None:
        print str(list.val) + ' ',
        list = list.next
    print ''


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
show_list(l1)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
show_list(l2)
s = Solution()
l3 = s.mergeTwoLists(l1, l2)
show_list(l3)