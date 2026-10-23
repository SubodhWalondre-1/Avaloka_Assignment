import heapq


def can_attend_all(events):
    """Return True when no two meetings overlap."""
    meetings = sorted(events)

    for i in range(1, len(meetings)):
        if meetings[i][0] < meetings[i - 1][1]:
            return False

    return True


def min_rooms_required(events):
    """Return the minimum number of rooms needed for all meetings."""
    rooms = []

    for start, end in sorted(events):
        if rooms and rooms[0] <= start:
            heapq.heapreplace(rooms, end)
        else:
            heapq.heappush(rooms, end)

    return len(rooms)


if __name__ == "__main__":
    meetings = [(9, 11), (10, 12), (12, 13)]
    print(can_attend_all(meetings))    # False
    print(min_rooms_required(meetings))  # 2
