class MyList(list):
    def __getitem__(self, offset):
        print(f'<indexing {list(self)} at {offset}>')
        return list.__getitem__(self, offset - 1)
