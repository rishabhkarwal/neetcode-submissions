class Solution:
    SPLIT = '±'
    def encode(self, strs: List[str]) -> str:
        if strs == []: return 'None'
        return self.SPLIT.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'None': return []
        return [''] if s == '' else s.split(self.SPLIT)

# [] -> []
# [''] -> ['']