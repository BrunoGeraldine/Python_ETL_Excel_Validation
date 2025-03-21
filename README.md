![image](https://github.com/user-attachments/assets/e14f36bb-1bb4-4ded-bdbe-8bdf7b8771b1)


# Campaign Data Validator
Data engineering project where I will validate tables in .csv or .xlsx format.

![image](https://github.com/user-attachments/assets/21a7448e-dff0-458a-b475-733ee3dd4f41)




## Overview
Campaign Data Validator is a Python-based application that validates sales campaign data from a CSV file using **Pydantic** for data validation and **Streamlit** for an interactive user interface. The tool ensures that all input data follows predefined constraints and allows users to download the validated dataset.

![image](https://github.com/user-attachments/assets/9a031e63-727d-4fc5-8bbb-4bd717d1b1e1)


## Features
- **Data Validation**: Ensures that all records meet the specified constraints.
- **CSV Upload**: Users can upload CSV files for validation.
- **Error Reporting**: Displays errors found in the dataset.
- **Validated Data Export**: Allows users to download a clean, validated CSV file.
- **Interactive UI**: Built with **Streamlit** for ease of use.

## Technologies Used
- **Python**
- **Pandas**
- **Streamlit**
- **Pydantic**

## Installation
To set up and run the project locally, follow these steps:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Data Model
The application validates data against the following schema:

```python
class SalesSpreadsheet(BaseModel):
    Organizer: int
    Year_Month: str
    Day_of_Week: str
    Day_Type: str
    Goal: str
    Date: str
    AdSet_name: Optional[str]
    Amount_spent: float
    Link_clicks: Optional[float]
    Impressions: Optional[float]
    Conversions: Optional[float]
    Segmentation: str
    Ad_Type: str
    Phase: str
```

## Example CSV Structure
| Organizer | Year_Month | Day_of_Week | Day_Type | Goal    | Date       | AdSet_name | Amount_spent | Link_clicks | Impressions | Conversions | Segmentation | Ad_Type | Phase |
|-----------|-----------|-------------|----------|---------|------------|------------|--------------|-------------|-------------|-------------|-------------|---------|-------|
| 123       | 2024-03   | Monday      | Business | Sales   | 2024-03-01 | AdGroup A  | 250.00       | 45          | 12000       | 3           | Audience A  | Banner  | Launch |

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License
This project is licensed under the MIT License.

## Reference:
[![image](https://github.com/user-attachments/assets/39e3216b-c937-487b-821f-80c3fe23cdbe)](https://docs.pydantic.dev/latest/api/types/)

