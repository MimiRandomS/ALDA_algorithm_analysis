from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort
from analysis.runner import AlgorithmRunner
from analysis.plotter import ResultsPlotter


def main():
    # Tamaños a probar
    # Para O(n²): sizes pequeños porque son lentos
    # Para O(n log n): sizes más grandes
    sizes_small = [100, 500, 1000, 2000, 3000]
    sizes_large = [100, 500, 1000, 2000, 5000, 10000]

    runner = AlgorithmRunner()

    # Run O(n²) algorithms con sizes pequeños
    print("=" * 50)
    print("Testing O(n²) algorithms...")
    print("=" * 50)
    runner.run_experiment(bubble_sort, "Bubble Sort", sizes_small, iterations=3)
    runner.run_experiment(insertion_sort, "Insertion Sort", sizes_small, iterations=3)

    # Run O(n log n) algorithms con sizes más grandes
    print("\n" + "=" * 50)
    print("Testing O(n log n) algorithms...")
    print("=" * 50)
    runner.run_experiment(merge_sort, "Merge Sort", sizes_large, iterations=3)
    runner.run_experiment(quick_sort, "Quick Sort", sizes_large, iterations=3)
    runner.run_experiment(heap_sort, "Heap Sort", sizes_large, iterations=3)

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

    print("\n✅ Analysis complete! Check the results/ folder for graphs.")


if __name__ == "__main__":
    main()