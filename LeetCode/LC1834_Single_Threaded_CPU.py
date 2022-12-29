class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result = []
        heap = []
        
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks = sorted(tasks, key=lambda x : x[0])
        
        time = tasks[0][0]
        cnt = 0  

        while heap or cnt < len(tasks):
            while cnt < len(tasks) and time >= tasks[cnt][0]:
                heapq.heappush(heap, [tasks[cnt][1], tasks[cnt][2]])
                cnt += 1
            if heap:
                t, index = heapq.heappop(heap)
                time += t
                result.append(index)
            else:
                time = tasks[cnt][0]
                
        return result