class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        card_dict = {}
        for h in hand:
            card_dict[h] = card_dict.get(h, 0) + 1
        
        card_dict = dict(sorted(card_dict.items()))

        for j in range(len(hand) // groupSize):
            keys = list(card_dict.keys())
            cur_size = 0
            i = 0
            while i < len(keys):
                if i != 0 and abs(keys[i] - keys[i - 1]) != 1:
                    cur_size = 0
                    i += 1
                    continue
                elif cur_size == groupSize:
                    cur_size = 0
                    print(card_dict)
                    break
                else:
                    card_dict[keys[i]] -= 1
                    if card_dict[keys[i]] == 0:
                        del card_dict[keys[i]]
                    cur_size += 1
                    i += 1
        return len(card_dict) == 0