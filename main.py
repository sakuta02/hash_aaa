class HashTable:
    def __init__(self):
        self.cap = 8
        self.t = [[] for i in range(self.cap)]
        self.cnt = 0

    def h(self, key):
        x = 0
        for c in key:
            x = (x * 31 + ord(c)) % 1000000007
        return x % self.cap

    def resize(self):
        old = self.t
        self.cap *= 2
        self.t = [[] for i in range(self.cap)]
        for b in old:
            for p in b:
                self.t[self.h(p[0])].append(p)

    def put(self, key, val):
        b = self.t[self.h(key)]

        for p in b:
            if p[0] == key:
                p[1] = val
                return

        b.append([key, val])
        self.cnt += 1

        if self.cnt / self.cap > 0.75:
            self.resize()

    def get(self, key):
        for p in self.t[self.h(key)]:
            if p[0] == key:
                return p[1]
        return None

    def delete(self, key):
        b = self.t[self.h(key)]
        for i in range(len(b)):
            if b[i][0] == key:
                val = b[i][1]
                b.pop(i)
                self.cnt -= 1
                return val
        return None


ht = HashTable()
q = int(input())
ans = []

for _ in range(q):
    s = input().split()
    cmd = s[0]

    if cmd == "put":
        ht.put(s[1], int(s[2]))

    elif cmd == "get":
        r = ht.get(s[1])
        if r is None:
            ans.append("Error")
        else:
            ans.append(str(r))

    elif cmd == "del":
        r = ht.delete(s[1])
        if r is None:
            ans.append("Error")
        else:
            ans.append(str(r))

    elif cmd == "size":
        ans.append(str(ht.cnt))

print("\n".join(ans))
