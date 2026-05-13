class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        relations = defaultdict(list)

        
        for t in trust:
            person, trusted = t

            relations[trusted].append(person)
        
        if len(relations) != 1:
            return -1
        
        k, v = list(relations.keys())[0], list(relations.values())[0]
        if len(v) != n - 1 or k in v:
            return -1
        return k
