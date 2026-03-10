from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort
from analysis.runner import AlgorithmRunner
from analysis.plotter import ResultsPlotter 


def main():
    # Sizes to test
    # For O(n²): small sizes because they are slow
    # For O(n log n): larger sizes
    sizes_small = [100, 500, 1000, 2000, 3000]
    sizes_large = [100, 500, 1000, 2000, 5000, 10000]

    runner = AlgorithmRunner()

    # Run O(n²) algorithms with smalls sizes
    print("=" * 50)
    print("Testing O(n²) algorithms...")
    print("=" * 50)
    runner.run_experiment(bubble_sort, "Bubble Sort", sizes_small, iterations=3)
    runner.run_experiment(insertion_sort, "Insertion Sort", sizes_small, iterations=3)

    # Run O(n log n) algorithms with big sizes
    print("\n" + "=" * 50)
    print("Testing O(n log n) algorithms...")
    print("=" * 50)
    runner.run_experiment(merge_sort, "Merge Sort", sizes_large, iterations=3)
    runner.run_experiment(quick_sort, "Quick Sort", sizes_large, iterations=3)
    runner.run_experiment(heap_sort, "Heap Sort", sizes_large, iterations=3)

    # Worst case comparison: Quick Sort O(n²) vs Bubble Sort O(n²)
    print("\n" + "=" * 50)
    print("Testing WORST CASE: Quick Sort vs Bubble Sort...")
    print("=" * 50)
    sizes_worst_case = [100, 200, 300, 400, 500]  # Mucho más pequeños
    runner.run_worst_case_experiment(quick_sort, "Quick Sort", sizes_worst_case, iterations=3)
    runner.run_worst_case_experiment(bubble_sort, "Bubble Sort", sizes_worst_case, iterations=3)

    # Best case analysis
    print("\n" + "=" * 50)
    print("Testing BEST CASE scenarios...")
    print("=" * 50)
    runner.run_best_case_experiment(insertion_sort, "Insertion Sort", sizes_large, iterations=3)
    runner.run_best_case_experiment(merge_sort, "Merge Sort", sizes_large, iterations=3)

    # Save results
    runner.save_results()

    # Generate plots
    print("\n" + "=" * 50)
    print("Generating plots...")
    print("=" * 50)
    df = runner.get_dataframe()
    plotter = ResultsPlotter(df)

    plotter.plot_all_algorithms()
    plotter.plot_quadratic_vs_nlogn()
    plotter.plot_individual()
    plotter.plot_best_case_comparison()
    plotter.plot_worst_case_comparison()

    print("\n✅ Analysis complete! Check the results/ folder for graphs.")


if __name__ == "__main__":
    main()