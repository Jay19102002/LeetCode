# Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
# Output: 3
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 2 (0 + 1 >= 1)
# - Assign worker 1 to task 1 (3 >= 2)
# - Assign worker 2 to task 0 (3 >= 3)

def maxTasksAssigned(tasks, workers, pills, strength):
    def cannot_complete(numTasks: int, p = pills)-> bool:
        cnt = 0 
        jobs = deque()
        
        for i in range(numTasks - 1, -1, -1): 
            while cnt < numTasks:
                if tasks[cnt] > workers[i] + strength: break
                jobs.append(tasks[cnt])
                cnt += 1
            
            if not jobs:
                return True
            
            if workers[i] >= jobs[0]:
                jobs.popleft()
            elif p > 0:
                jobs.pop()
                p -= 1
            else:
                return True
        return False


    tasks.sort()
    workers.sort(reverse = True)
    n = min(len(tasks), len(workers)) + 1
    return bisect_left(range(n), True, key = cannot_complete) - 1

task = [3, 2, 1]
worker = [0, 3, 3]
pills = 1
strength = 1
print(maxTasksAssigned(task, worker, pills, strength))  