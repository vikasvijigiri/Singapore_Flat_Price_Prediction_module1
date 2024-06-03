# Singapore Flat Resale Price Prediction

## Overview

This project aims to predict the resale price of flats in Singapore using machine learning techniques, particularly Random Forest Regression. The dataset used for this project contains various features related to the properties such as the town, flat type, floor area, and more.

## Dataset

The dataset consists of the following columns:

1. **month**: The month of the transaction.
2. **town**: The town where the property is located.
3. **flat_type**: The type of flat (e.g., 3-room, 4-room).
4. **block**: The block number of the property.
5. **street_name**: The street name of the property.
6. **storey_range**: The range of storeys where the property is located.
7. **floor_area_sqm**: The floor area of the property in square meters.
8. **flat_model**: The model of the flat (e.g., Improved, Model A).
9. **lease_commence_date**: The year when the lease commenced.
10. **remaining_lease**: The remaining lease of the property.
11. **resale_price**: The resale price of the property (target variable).
12. **month_1**: A processed feature representing the month.
13. **year_1**: A processed feature representing the year.
14. **storey_range_first_two**: A processed feature representing the first two characters of the storey range.

## Model Details

- **Algorithm**: Random Forest Regression
- **Preprocessing**: Outlier removal, extensive visualization of some columns.
- **Performance Metrics**: Mean Absolute Error, Root Mean Squared Error, R-squared.
- **Evaluation Technique**: Cross-validation

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/singapore-flat-resale-price-prediction.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Jupyter notebooks:

    ```bash
    jupyter notebook
    ```

4. Follow the instructions in the notebooks to explore the data, preprocess it, train the model, and make predictions.


## Author

[Vikas](https://github.com/vikasvijigiri)
