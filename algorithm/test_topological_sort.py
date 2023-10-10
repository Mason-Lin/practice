# 207. Course Schedule
class Solution207:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for crs in adj[course]:
                if dfs(crs) is False:
                    return False
            visited.add(course)
            cycle.remove(course)
            return True

        return all(dfs(crs) is not False for crs in range(numCourses))


def test_207():
    assert Solution207().canFinish(numCourses=2, prerequisites=[[1, 0]]) is True
    assert Solution207().canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]) is False


# 210. Course Schedule II
class Solution210:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        C = numCourses
        P = prerequisites
        adj = {i: [] for i in range(C)}
        for crs, pre in P:
            adj[crs].append(pre)
        visit, cycle = set(), set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            visit.add(crs)
            for dep in adj[crs]:
                if dfs(dep) is False:
                    return False
            res.append(crs)
            cycle.remove(crs)
            return True

        for crs in range(C):
            if dfs(crs) is False:
                return []
        return res


def test_210():
    assert Solution210().findOrder(numCourses=2, prerequisites=[[1, 0]]) == [0, 1]
    assert Solution210().findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]) in (
        [0, 2, 1, 3],
        [0, 1, 2, 3],
    )
