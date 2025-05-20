


def insertion_sort(l):
    m = len(l)              
    for i in range(1,m):
        key = l[i]              # wird in l[0,..,i-1] einsortiert
        j = i
        while (j>0) and l[j-1]>key:
            l[j] = l[j-1]       # verschiebe Vorgaenger nach re.
            j -= 1
        l[j] = key              # l[0,..,i] ist sortiert
    return l


a = [53,24,-12,54,0,22,-12]
b = insertion_sort(a)   


# Laufzeitanalyse
# def insertion_sort(l):
#     m = len(l)              # O(1)
#     for i in range(1,m):    # O(m-1)-oft
#         key = l[i]            # O(1)  
#         j = i                 # O(1)
#         while (j>0) and l[j-1]>key:   # i-oft 
#             l[j] = l[j-1]             # O(1)
#             j -= 1                    # O(1)
#         l[j] = key            # O(1)
#     return l                # O(1)