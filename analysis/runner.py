import time
import random
from typing import Callable, List
import pandas as pd
import timeit


class AlgorithmRunner:
    def __init__(self):
        self.results = []

    def generate_random_array(self, size: int) -> List[int]:
        """Generate a random array of given size"""
        return [random.randint(1, 10000) for _ in range(size)]

    def measure_time(self, algorithm: Callable, arr: List[int]) -> float:
        """Measure execution time of an algorithm on a copy of the array"""
        arr_copy = arr.copy()
        time_taken = timeit.timeit(lambda: algorithm(arr_copy.copy()), number=1)
        return time_taken

    def run_experiment(self,
                       algorithm: Callable,
                       algorithm_name: str,
                       sizes: List[int],
                       iterations: int = 5) -> None:
        """
        Run algorithm on different input sizes and record times

        Args:
            algorithm: The sorting function to test
            algorithm_name: Name for display
            sizes: List of array sizes to test
            iterations: Number of times to run each size (for averaging)
        """
        print(f"\nRunning experiments for {algorithm_name}...")

        for size in sizes:
            times = []
            for _ in range(iterations):
                arr = self.generate_random_array(size)
                execution_time = self.measure_time(algorithm, arr)
                times.append(execution_time)

            avg_time = sum(times) / len(times)
            self.results.append({
                'Algorithm': algorithm_name,
                'Size': size,
                'Time': avg_time
            })
            print(f"  Size {size}: {avg_time:.6f}s (avg of {iterations} runs)")

    def get_dataframe(self) -> pd.DataFrame:
        """Return results as a pandas DataFrame"""
        return pd.DataFrame(self.results)

    def save_results(self, filename: str = 'results/experimental_results.csv'):
        """Save results to CSV"""
        df = self.get_dataframe()
        df.to_csv(filename, index=False)
        print(f"\nResults saved to {filename}")