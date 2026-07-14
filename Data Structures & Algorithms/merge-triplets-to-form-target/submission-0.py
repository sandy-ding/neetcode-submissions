class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        arr = [[], [], []]

        for i in range(len(target)):
            for j, tri in enumerate(triplets):
                if tri[i] == target[i]:
                    arr[i].append(j)

        for i in arr[0]:
            for j in arr[1]:
                for x in arr[2]:
                    if max(triplets[i][0], triplets[j][0], triplets[x][0]) == target[0] and max(triplets[i][1], triplets[j][1], triplets[x][1]) == target[1] and max(triplets[i][2], triplets[j][2], triplets[x][2]) == target[2]:
                        return True

        return False
                        
