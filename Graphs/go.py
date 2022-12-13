# A party is thrown. At the end of each hour, all guests who do not know at least
# Two other guests in attendance will be askes to leave.
# Given a number of guests N, and adjacency lists A & B, both length of M
# where M = N-1, find how many hours it would take before no one is asked to leave
# Assume that guests cannot re-enter the party and do not lie about who they know

def solution(N, A, B):

    if len(A) == 1 :
        return 1

    hours = 0


    guests = A + B
    for guest in guests:
        if guests.count(guest) == 1:
            guests.remove(guest)

    return hours

print(solution(7, [0,1,2,1,4,4], [1,2,0,4,5,6]))