class MergeSort:
    
    def sort(self, A, key=lambda x: x, reverse=False):
        B, K = A[:], [key(a) for a in A]
        self.sort_with_index(B, K, 0, len(B)-1, reverse)
        return B

    def sort_with_index(self, B, K, l, r, reverse):
        if l == r:
            return B
        m = l + (r-l)//2
        self.sort_with_index(B, K, 0, m, reverse=reverse)
        self.sort_with_index(B, K, m+1, r, reverse=reverse)
        return self.merge(B, K, l, m, r, reverse)

    def merge(self, B, K, l, m, r, reverse):
        l_ptr, r_ptr, curr_ptr = l, m+1, l
        C = B[:]
        CK = K[:]
        # print('=================')
        # print(B[l:m+1], B[m+1:r+1])
        while l_ptr <= m and r_ptr <= r:
            #print(l_ptr, r_ptr, curr_ptr)
            if CK[l_ptr] <= CK[r_ptr]:
                B[curr_ptr] = C[l_ptr]
                K[curr_ptr] = CK[l_ptr]
                l_ptr += 1
            elif CK[l_ptr] > CK[r_ptr]:
                B[curr_ptr] = C[r_ptr]
                K[curr_ptr] = CK[r_ptr]
                r_ptr += 1
            curr_ptr += 1
        while l_ptr <= m:
            B[curr_ptr] = C[l_ptr]
            K[curr_ptr] = CK[l_ptr]
            l_ptr += 1
            curr_ptr += 1
        while r_ptr <= r:
            B[curr_ptr] = C[r_ptr]
            K[curr_ptr] = CK[r_ptr]
            r_ptr += 1
            curr_ptr += 1
        #print(B[l:r+1])


            
        