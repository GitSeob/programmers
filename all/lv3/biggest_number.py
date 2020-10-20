from collections import deque
        from itertools import permutations

        def solution(numbers):
            n_dic = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
            for n in numbers:
                n_dic[int(str(n)[0])].append(str(n))

            res = ''

            for i in range(9, 0, -1):
                if len(n_dic[i]) == 0:
                    continue
                elif len(n_dic[i]) == 1:
                    res += n_dic[i][0]
                else:
                    i_list = permutations(n_dic[i], len(n_dic[i]))
                    mix_list = []
                    for perm in i_list:
                        tmp = ''.join(perm)
                        mix_list.append(tmp)
                    res += max(mix_list)
            if n_dic[0] != []:
                return res + '0'
            return res
