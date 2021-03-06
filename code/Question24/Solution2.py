'''
利用递归的思想，先递归到尽头获取头节点，然后返回的过程逐步重新构建链表
注意！是递归到尾节点进行操作 想明白这一点对于理解 head.next = none 非常重要
https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/fan-zhuan-lian-biao-yi-dong-de-shuang-zhi-zhen-jia/
'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        '''
        这里实际是引用 python传递的也是地址 除非是简单变量
        '''
        start = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return start