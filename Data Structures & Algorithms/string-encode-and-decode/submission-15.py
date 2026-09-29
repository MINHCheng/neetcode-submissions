class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs)==1 and strs[0]=='':
            return '#'
        return '|'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        elif s == '#':
            return ['']
        else:
            dec_op = s.split('|')
            return dec_op
