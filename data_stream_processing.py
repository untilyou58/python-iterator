import time


class DataStream:
    def __init__(self, data_source, batch_size=100):
        self.data_source = data_source
        self.batch_size = batch_size

    def __iter__(self):
        return self

    def __next__(self):
        batch = []
        for _ in range(self.batch_size):
            try:
                item = next(self.data_source)
                batch.append(self.process_item(item))
            except StopIteration:
                if not batch:
                    raise StopIteration
                return batch
        return batch

    def process_item(self, item):
        # Process the item here
        time.sleep(0.01)  # Simulate processing time
        return item * 2


# Usage
data = range(1000)  # Big data source
stream = DataStream(iter(data))

for batch in stream:
    print(f"Processed batch: {batch[:5]}...")  # Show only the first 5 items

# Output:
# Processed batch: [0, 2, 4, 6, 8]...
# Processed batch: [200, 202, 204, 206, 208]...
# Processed batch: [400, 402, 404, 406, 408]...
# Processed batch: [600, 602, 604, 606, 608]...
# Processed batch: [800, 802, 804, 806, 808]...
# Processed batch: [1000, 1002, 1004, 1006, 1008]...
# Processed batch: [1200, 1202, 1204, 1206, 1208]...
# Processed batch: [1400, 1402, 1404, 1406, 1408]...
# Processed batch: [1600, 1602, 1604, 1606, 1608]...
# Processed batch: [1800, 1802, 1804, 1806, 1808]...
