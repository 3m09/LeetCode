def minWindow(self, s: str, t: str) -> str:
        from collections import deque
        import sys
        if len(t) > len(s):
            return ''
        t_map = {}
        for c in t:
            if c in t_map:
                t_map[c] += 1
            else:
                t_map[c] = 1
        found = deque()
        l = -1
        r = 0
        cnt = len(t)
        ans_l_r = (0, len(s)-1)
        for idx, c in enumerate(s):
            #print(f'{c} not in map')
            if c in t_map:
                t_map[c] -= 1
                found.append((c,idx))
                l = idx if l == -1 else l
                if t_map[c] < 0 and s[l] == c:
                    while( t_map[found[0][0]] < 0 ):
                        t_map[found[0][0]] += 1
                        found.popleft()
                        #print(f'found after popleft: {found}')
                    l = found[0][1]
                    #print(f'Updated l to {l}')
                elif t_map[c] >= 0:
                    cnt -= 1
                    # found.append((c,idx))
                    #print(f'found: {found}')
                if cnt == 0:
                    #print(f'All chars found between {l} and {idx}')
                    if (idx - l) < (ans_l_r[1] - ans_l_r[0]):
                        #print(f'Updated ans_l_r from {ans_l_r} to {(l, idx)}')
                        ans_l_r = ( l, idx )
                    if found:
                        cur_l_chr, _ = found.popleft()
                        #print(f'found after popleft: {found}')
                        t_map[cur_l_chr] += 1
                    cnt = 1
                    while( found and t_map[found[0][0]] < 0 ):
                        t_map[found[0][0]] += 1
                        found.popleft()
                        #print(f'found after popleft: {found}')
                    l = found[0][1] if found else -1
                    #print(f'Updated l to {l}')
        #print(f'ans_l_r: {ans_l_r}')
        return s[ans_l_r[0]:ans_l_r[1]+1]