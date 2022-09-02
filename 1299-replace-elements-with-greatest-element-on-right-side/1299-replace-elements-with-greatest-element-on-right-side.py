class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # count=0
        # for i in arr:
        #     arr[count]=0
        #     if count<len(arr)-1:
        #         for j in range(count+1,len(arr)):
        #             arr[count]=max(arr[j],arr[count])
        #     else:
        #         arr[count]=-1
        #     count+=1
        # return arr
                    
        m = -1
        i = len(arr) -1 
        while i >= 0:
            temp = arr[i]
            arr[i] = m
            if temp > m:
                m = temp
            i-= 1
        return arr

        