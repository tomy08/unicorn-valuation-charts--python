### Unicorn Valuation Graphs with Python

This project is a Python script designed to generate valuation graphs for unicorn companies based on different fields such as company, industry, country, and continent. It utilizes CSV data from a file named "data.csv" and generates bar charts using the provided data.

### Installation

To use this project, you'll need to have Python installed on your system. Additionally, ensure you have the necessary dependencies installed, including `matplotlib` for plotting.

You can install `matplotlib` using pip:

```bash
pip install matplotlib
```

### Usage

1. Clone or download the project repository.
2. Place your data file named "data.csv" in the project directory.
3. Run the `main()` function in the `unicorn_valuation.py` script.

### Example Usage

```python
python unicorn_valuation.py
```

### Input Options

- Company
- Industry
- Country
- Continent

### Example

If you choose 'company' as the field, the script will generate a bar chart showing the valuation of each company. Companies with less than $15 billion valuation will not be displayed.

### Data Source

The data used for this project was obtained from [Kaggle](https://www.kaggle.com/datasets/mysarahmadbhat/unicorn-companies?select=Unicorn_Companies.csv).
