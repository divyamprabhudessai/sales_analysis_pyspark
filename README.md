# Simple Sales Analysis with PySpark

A beginner-friendly project that demonstrates basic sales analysis using PySpark.

## What You'll Learn
- How to load data into PySpark
- Basic data transformations
- Simple aggregations
- Basic data visualization

## Project Structure
```
.
├── data/                   # Sample sales data
│   └── sales.csv          # Simple sales dataset
├── simple_analysis.py     # Main analysis script
└── requirements.txt       # Project dependencies
```

## Setup Instructions

1. Create a virtual environment:
   ```bash
   py -m venv venv
   venv\Scripts\activate
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis:
   ```bash
   py simple_analysis.py
   ```

## Sample Data
Our sales data contains:
- date: Sale date
- product: Product name
- quantity: Number of items sold
- price: Price per item
- total: Total sale amount 