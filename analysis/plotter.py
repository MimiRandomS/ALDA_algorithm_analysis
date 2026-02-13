import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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