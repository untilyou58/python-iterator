def data_pipeline():
    result = None
    while True:
        value = yield result
        if value is None:
            return  # use return instead of break
        result = process_data(value)


def process_data(data):
    # Process the data here
    return data * 2


# Usage
pipeline = data_pipeline()
next(pipeline)  # Start the pipeline

data_points = [1, 2, 3, 4, 5]
results = []

for data in data_points:
    result = pipeline.send(data)
    results.append(result)

try:
    pipeline.send(None)  # Close the pipeline
except StopIteration:
    pass  # Suppress the exception

print(results)  # [2, 4, 6, 8, 10]

# Output:
# [2, 4, 6, 8, 10]
