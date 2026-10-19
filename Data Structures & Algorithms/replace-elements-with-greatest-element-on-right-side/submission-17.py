class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greater = {len(arr)-1:-1}
        greatest = -1
        new_arr=[]
        for i in range(len(arr)-1,-1,-1):
            if greatest >= 0:
                greater[i]=greatest
            if arr[i] > greatest:
                greatest = arr[i]
        
        print(greater)

        for k,v in reversed(greater.items()):
            new_arr.append(v)
            
        return new_arr