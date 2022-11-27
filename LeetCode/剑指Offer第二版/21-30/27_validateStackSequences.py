from typing import List
# 栈的压入、弹出序列
# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,
# 1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        instack = []
        prepos = -1
        for nowvalue in popped:
            if nowvalue not in instack:
                nowpos = pushed.index(nowvalue)
                for i in range(nowpos-prepos-1):
                    instack.append(pushed[prepos+i+1])
                prepos = nowpos
            else:
                if nowvalue != instack[-1]:
                    return False
                else:
                    instack.pop()
        return True

    def validateStackSequences2(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)  # num 入栈
            while stack and stack[-1] == popped[i]:  # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack

if __name__ == '__main__':
    sl = Solution()
    print(sl.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
