
def count_occurences(s):
    list_count = list()
    i = 0
    while i < len(s):
        c = s[i]
        new_c = c
        count = 1
        while i+1 < len(s) and new_c == s[i+1]:
            count += 1
            i += 1
            #print(i)
        list_count.append(str(count))
        list_count.append(new_c)
        #map_count[str(new_c)] = count
        i+=1
    return list_count


if __name__ == '__main__':
    s = '1'
    for i in range(15):
        a = count_occurences(str(s))
        s = ''.join(a)
        print(s)
