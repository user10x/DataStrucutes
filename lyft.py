
class DataGatherer:

    def __init__(self, limit):
        self.limit = limit
        self.data = []
        self.chunk_size = 100


    def chunk_data(self, data, chunk_size):

        for chunk in range(0, len(data), chunk_size):
            yield data[chunk:chunk+chunk_size]


    def fetch_data(self, data, limit):
        pass




dg = DataGatherer(100)


dg.fetch_data(None, limit)