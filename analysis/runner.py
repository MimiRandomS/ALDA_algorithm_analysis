import time
import random
from typing import Callable, List
import statistics
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

            median_time = statistics.median(times)
            self.results.append({
                'Algorithm': algorithm_name,
                'Size': size,
                'Time': median_time
            })
            print(f"  Size {size}: {median_time:.6f}s (avg of {iterations} runs)")

    def run_best_case_experiment(self,
                                 algorithm: Callable,
                                 algorithm_name: str,
                                 sizes: List[int],
                                 iterations: int = 5) -> None:
        """
        Run algorithm on ALREADY SORTED arrays (best case for some algorithms)
        """
        print(f"\nRunning BEST CASE experiments for {algorithm_name}...")

        for size in sizes:
            times = []
            for _ in range(iterations):
                # Best case: already sorted array
                arr = list(range(size))  # [0, 1, 2, 3, ..., size-1]
                execution_time = self.measure_time(algorithm, arr)
                times.append(execution_time)

            median_time = statistics.median(times)
            self.results.append({
                'Algorithm': f"{algorithm_name} (Best Case)",
                'Size': size,
                'Time': median_time
            })
            print(f"  Size {size}: {median_time:.6f}s (median of {iterations} runs)")

    def run_worst_case_experiment(self,
                                  algorithm: Callable,
                                  algorithm_name: str,
                                  sizes: List[int],
                                  iterations: int = 5) -> None:
        """
        Run algorithm on WORST CASE scenarios
        - Quick Sort: already sorted (pivot is always min/max)
        - Bubble Sort: reverse sorted
        """
        print(f"\nRunning WORST CASE experiments for {algorithm_name}...")

        for size in sizes:
            times = []
            for _ in range(iterations):
                if 'Quick' in algorithm_name:
                    # Worst case for Quick Sort: already sorted
                    arr = list(range(size))
                elif 'Bubble' in algorithm_name:
                    # Worst case for Bubble Sort: reverse sorted
                    arr = list(range(size, 0, -1))
                else:
                    arr = list(range(size, 0, -1))  # default reverse

                execution_time = self.measure_time(algorithm, arr)
                times.append(execution_time)

            median_time = statistics.median(times)
            self.results.append({
                'Algorithm': f"{algorithm_name} (Worst Case)",
                'Size': size,
                'Time': median_time
            })
            print(f"  Size {size}: {median_time:.6f}s (median of {iterations} runs)")

    def get_dataframe(self) -> pd.DataFrame:
        """Return results as a pandas DataFrame"""
        return pd.DataFrame(self.results)

    def save_results(self, filename: str = 'results/experimental_results.csv'):
        """Save results to CSV"""
        df = self.get_dataframe()
        df.to_csv(filename, index=False)
        print(f"\nResults saved to {filename}")