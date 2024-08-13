def get_stats(numbers):
    mean = sum(numbers) / len(numbers)
    median = sorted(numbers)[len(numbers) // 2]
    return mean, median

mean, median = get_stats([1,2,3,4,5])
print(f"Mean:{mean}, Median:{median}")