class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        participants = set()

        for i in range(1, n + 1):
            participants.add(i)

        trusted = set()

        for t in trust:
            person, vote = t

            if person in participants:
                participants.remove(person)
            
            trusted.add(vote)

        if len(participants) != 1 or len(trusted) != 1:
            return -1
        
        judge = participants.pop()
        trusted_person = trusted.pop()

        if judge != trusted_person:
            return -1
        
        return judge