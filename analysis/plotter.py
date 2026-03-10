import pandas as pd
import matplotlib.pyplot as plt


class ResultsPlotter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_all_algorithms(self, save_path: str = 'results/graphs/comparison_all.png'):
        """Plot all algorithms on the same graph"""
        plt.figure(figsize=(12, 7))

        for algorithm in self.df['Algorithm'].unique():
            data = self.df[self.df['Algorithm'] == algorithm]
            plt.plot(data['Size'], data['Time'],
                     marker='o', linewidth=2, markersize=6,
                     label=algorithm)

        plt.xlabel('Input Size (n)', fontsize=12)
        plt.ylabel('Execution Time (seconds)', fontsize=12)
        plt.title('Sorting Algorithms - Time Complexity Comparison', fontsize=14, fontweight='bold')
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        print(f"Saved: {save_path}")
        plt.close()

    def plot_quadratic_vs_nlogn(self, save_path: str = 'results/graphs/comparison_by_complexity.png'):
        """Separate O(n²) from O(n log n) algorithms"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # O(n²) algorithms
        quadratic = ['Bubble Sort', 'Insertion Sort']
        for algorithm in quadratic:
            if algorithm in self.df['Algorithm'].values:
                data = self.df[self.df['Algorithm'] == algorithm]
                ax1.plot(data['Size'], data['Time'],
                         marker='o', linewidth=2, markersize=6,
                         label=algorithm)

        ax1.set_xlabel('Input Size (n)', fontsize=12)
        ax1.set_ylabel('Execution Time (seconds)', fontsize=12)
        ax1.set_title('O(n²) Algorithms', fontsize=13, fontweight='bold')
        ax1.legend(fontsize=10)
        ax1.grid(True, alpha=0.3)

        # O(n log n) algorithms
        nlogn = ['Merge Sort', 'Quick Sort', 'Heap Sort']
        for algorithm in nlogn:
            if algorithm in self.df['Algorithm'].values:
                data = self.df[self.df['Algorithm'] == algorithm]
                ax2.plot(data['Size'], data['Time'],
                         marker='o', linewidth=2, markersize=6,
                         label=algorithm)

        ax2.set_xlabel('Input Size (n)', fontsize=12)
        ax2.set_ylabel('Execution Time (seconds)', fontsize=12)
        ax2.set_title('O(n log n) Algorithms', fontsize=13, fontweight='bold')
        ax2.legend(fontsize=10)
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        print(f"Saved: {save_path}")
        plt.close()

    def plot_best_case_comparison(self, save_path: str = 'results/graphs/best_case_comparison.png'):
        """Compare best case vs average case for relevant algorithms"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Insertion Sort: best case O(n) vs average case O(n²)
        insertion_avg = self.df[self.df['Algorithm'] == 'Insertion Sort']
        insertion_best = self.df[self.df['Algorithm'] == 'Insertion Sort (Best Case)']

        if not insertion_avg.empty:
            ax1.plot(insertion_avg['Size'], insertion_avg['Time'],
                     marker='o', linewidth=2.5, markersize=8,
                     label='Average Case O(n²)', color='#E63946')

        if not insertion_best.empty:
            ax1.plot(insertion_best['Size'], insertion_best['Time'],
                     marker='s', linewidth=2.5, markersize=8,
                     label='Best Case O(n)', color='#06D6A0')

        ax1.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Time (seconds)', fontsize=12, fontweight='bold')
        ax1.set_title('Insertion Sort - Best vs Average Case', fontsize=14, fontweight='bold')
        ax1.legend(fontsize=11)
        ax1.grid(True, alpha=0.4, linestyle='--')

        # Merge Sort: best case = average case (always O(n log n))
        merge_avg = self.df[self.df['Algorithm'] == 'Merge Sort']
        merge_best = self.df[self.df['Algorithm'] == 'Merge Sort (Best Case)']

        if not merge_avg.empty:
            ax2.plot(merge_avg['Size'], merge_avg['Time'],
                     marker='o', linewidth=2.5, markersize=8,
                     label='Average Case O(n log n)', color='#118AB2')

        if not merge_best.empty:
            ax2.plot(merge_best['Size'], merge_best['Time'],
                     marker='s', linewidth=2.5, markersize=8,
                     label='Best Case O(n log n)', color='#073B4C')

        ax2.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Time (seconds)', fontsize=12, fontweight='bold')
        ax2.set_title('Merge Sort - Best vs Average Case', fontsize=14, fontweight='bold')
        ax2.legend(fontsize=11)
        ax2.grid(True, alpha=0.4, linestyle='--')

        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        print(f"Saved: {save_path}")
        plt.close()

    def plot_worst_case_comparison(self, save_path: str = 'results/graphs/worst_case_comparison.png'):
        """Compare Quick Sort worst case O(n²) vs Bubble Sort O(n²)"""
        plt.figure(figsize=(12, 7))

        quick_worst = self.df[self.df['Algorithm'] == 'Quick Sort (Worst Case)']
        bubble_worst = self.df[self.df['Algorithm'] == 'Bubble Sort (Worst Case)']

        if not quick_worst.empty:
            plt.plot(quick_worst['Size'], quick_worst['Time'],
                     marker='o', linewidth=2.5, markersize=8,
                     label='Quick Sort (Worst Case) - O(n²)', color='#F77F00')

        if not bubble_worst.empty:
            plt.plot(bubble_worst['Size'], bubble_worst['Time'],
                     marker='s', linewidth=2.5, markersize=8,
                     label='Bubble Sort (Worst Case) - O(n²)', color='#D62828')

        plt.xlabel('Input Size (n)', fontsize=14, fontweight='bold')
        plt.ylabel('Execution Time (seconds)', fontsize=14, fontweight='bold')
        plt.title('Worst Case Comparison: Quick Sort vs Bubble Sort (both O(n²))',
                  fontsize=16, fontweight='bold', pad=20)
        plt.legend(fontsize=12, loc='upper left')
        plt.grid(True, alpha=0.4, linestyle='--')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        print(f"Saved: {save_path}")
        plt.close()

    def plot_individual(self, save_dir: str = 'results/graphs/'):
        """Create individual plot for each algorithm"""
        for algorithm in self.df['Algorithm'].unique():
            data = self.df[self.df['Algorithm'] == algorithm]

            plt.figure(figsize=(10, 6))
            plt.plot(data['Size'], data['Time'],
                     marker='o', linewidth=2, markersize=8,
                     color='#2E86AB')

            plt.xlabel('Input Size (n)', fontsize=12)
            plt.ylabel('Execution Time (seconds)', fontsize=12)
            plt.title(f'{algorithm} - Experimental Analysis', fontsize=14, fontweight='bold')
            plt.grid(True, alpha=0.3)
            plt.tight_layout()

            filename = f"{save_dir}{algorithm.lower().replace(' ', '_')}.png"
            plt.savefig(filename, dpi=300)
            print(f"Saved: {filename}")
            plt.close()