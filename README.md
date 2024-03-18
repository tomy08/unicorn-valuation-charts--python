### Unicorn Valuation Graphs with Python

This project is a Python script designed to generate valuation graphs for unicorn companies based on different fields such as company, industry, country, and continent. It utilizes CSV data from a file named "data.csv" and generates bar charts using the provided data.

### Installation

To use this project, you'll need to follow this instructions:

```bash
git clone https://github.com/tomy08/unicorn-valuation-charts--python.git
cd unicorn-valuation-charts--python
source ./env/Scripts/activate
pip install -r requirements.txt
python unicorn_valuation.py
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

The data used for this project was obtained from [Kaggle](https://www.kaggle.com/datasets/mysarahmadbhat/unicorn-companies?select=Unicorn_Companies.csv). Please note that while efforts have been made to ensure data accuracy, it's essential to acknowledge that datasets from external sources can be erroneous or outdated. Users are advised to verify the data's accuracy and relevancy for their specific use case.
