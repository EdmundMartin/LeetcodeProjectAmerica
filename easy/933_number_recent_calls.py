

class RecentCounter:
    def __init__(self):
        self.calls = [

        ]

    def ping(self, t: int) -> int:
        new_calls = []
        for call in self.calls:
            if abs(t - call) <= 3_000:
                new_calls.append(call)
        new_calls.append(t)
        self.calls = new_calls
        return len(new_calls)


if __name__ == '__main__':
    rc = RecentCounter()
    res = rc.ping(1)
    print(res)
    res = rc.ping(2)
    print(res)
    res = rc.ping(3001)
    print(res)
    res = rc.ping(3002)
    print(res)