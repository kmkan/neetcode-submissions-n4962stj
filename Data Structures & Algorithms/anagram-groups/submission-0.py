class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            cat = tuple(sorted(s))
            groups[cat] = groups.get(cat, [])
            groups[cat].append(s)

        return list(groups.values())