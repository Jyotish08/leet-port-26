class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        c=0
        for i in range(len(arr1)):
            t=True
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    t= False        
            if t:
                c+=1
        return c

        