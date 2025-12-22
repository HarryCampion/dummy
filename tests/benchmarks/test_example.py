import time


def expensive_operation(duration=0.001):
    """
    A dummy function that simulates some work by sleeping.
    """
    time.sleep(duration)
    return duration

def test_expensive_operation(benchmark):
    """
    Benchmark the expensive_operation function.
    The benchmark fixture is provided by pytest-benchmark.
    """
    # benchmark(function_to_call, *args, **kwargs)
    result = benchmark(expensive_operation, duration=0.002)
    
    assert result == 0.002
