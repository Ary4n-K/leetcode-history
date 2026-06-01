class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        c = 0
        n = len(cost)
        for i in range(1,n+1):
            if i%3!=0:
                c+=cost[i-1]
        return c

