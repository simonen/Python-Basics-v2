start_int = int(input())
end_int = int(input())
#count = 0
a_type = ''
d_type = ''
for a in range(start_int, end_int + 1):
    count_c = 0
    count_d = 0
    for b in range(start_int, end_int + 1):
        for c in range(start_int, end_int + 1):
            if (b + c) % 2 == 0:
                count_c = 1
            else:
                continue
            for d in range(start_int, end_int + 1):
                if (a + d) % 2 != 0 and a > d:
                    count_d = 1
                else:
                    continue
                if count_c + count_d == 2:
                    print(f"{a}{b}{c}{d}", end=" ")
                    count_d = 0
                    #count += 1
#print(count)

