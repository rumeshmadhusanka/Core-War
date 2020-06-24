from extract import resolve_writes


# should import resolve_writes
class Memory:
    def __init__(self, size):
        self.size = size
        self.memory = [0 for _ in range(size)]
        self.pending_writes = []

    def __len__(self):
        return self.size

    def get_cyclic_idx(self, idx):
        return idx % self.size

    def __getitem__(self, idx):
        cyclic_idx = self.get_cyclic_idx(idx)
        return self.memory[cyclic_idx]

    def __setitem__(self, idx, value):
        cyclic_idx = self.get_cyclic_idx(idx)
        self.pending_writes.append([cyclic_idx, value])

    def writes(self):
        dic = dict()
        for i in self.pending_writes:
            if i[0] not in dic:
                dic[i[0]] = [i[1]]
            else:
                dic[i[0]].append(i[1])
        return dic

    def commit(self):
        d = self.writes()
        for key in d.keys():
            base = self.__getitem__(key)
            xs = d[key]
            post_value = resolve_writes(base, xs)
            self.memory[key] = post_value

    def load(self, data, offset):
        j = 0
        for i in range(offset, offset + len(data)):
            cyclic_offset = i % self.size
            self.memory[cyclic_offset] = data[j]
            j += 1
