# NumPy Laboratory Practice

This repository contains solutions to the 43 questions in the **NumPy Laboratory Practice** sheet.

## What's inside

- `numpy_lab_practice.ipynb` — notebook version, with one exercise per sectioned code cell and outputs saved after running.
- `numpy_lab_solutions.py` — the same solutions in a single Python script.
- `requirements.txt` — the library needed to run the examples.

## Setup

Python 3.9 or newer is suitable for these examples. From this folder, install NumPy with:

```bash
python -m pip install -r requirements.txt
```

To run the Python file:

```bash
python numpy_lab_solutions.py
```

To open the notebook:

```bash
jupyter notebook numpy_lab_practice.ipynb
```

You can also open the notebook directly in Google Colab or upload it to GitHub and use its notebook preview.

## Topics covered

1. Array creation and properties
2. Array arithmetic
3. Indexing and slicing
4. 2-D array indexing and slicing
5. Reshaping and transpose
6. Matrix operations
7. Universal functions
8. `np.where()`
9. Statistical operations
10. Sorting and unique values
11. Integrated lab questions

## Notes

- The exercises are numbered to match the practice sheet.
- Random examples use fixed seeds so results can be reproduced.
- Question 38 uses `np.in1d()` because the question specifically asks for it. In newer NumPy versions, `np.isin()` is the recommended replacement.
- For Question 42, the maximum and minimum are calculated from the matrix multiplication result.
- No file-handling or interactive array input/output exercises are included.

## License

This repository is shared for learning and practice. You may adapt the examples for your own study notes.
