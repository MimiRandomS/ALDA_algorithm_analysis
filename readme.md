# Algorithm Analysis - Sorting Algorithms

Comparison of 5 sorting algorithms with Big-O analysis and experimental validation.

## Algorithms
- Bubble Sort - $O(n^2)$
- Insertion Sort - $O(n^2)$
- Merge Sort - $O(n \log n)$
- Quick Sort - $O(n \log n)$
- Heap Sort - $O(n \log n)$

## Setup
```bash
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

### Si da error de ejecución de scripts

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Run Tests
```bash
pytest tests/
```

## Theory
$$
T(n) = 2T\left(\frac{n}{2}\right) + O(n)
$$

