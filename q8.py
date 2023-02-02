class solution:
 def sum_of_three(self, n):
        n, result, i = sorted(n), [], 0
        while i < len(n) - 2:
            j, k = i + 1, len(n) - 1
            while j < k:
                if n[i] + n[j] + n[k] < 0:
                    j += 1
                elif n[i] + n[j] + n[k] > 0:
                    k -= 1
                else:
                    result.append([n[i], n[j], n[k]])
                    j, k = j + 1, k - 1
                    while j < k and n[j] == n[j - 1]:
                        j += 1
                    while j < k and n[k] == n[k + 1]:
                        k -= 1
            i += 1
            while i < len(n) - 2 and n[i] == n[i - 1]:
                i += 1
        return result

print(solution().sum_of_three([-25, -10, -7, -3, 2, 4, 8, 10]))
