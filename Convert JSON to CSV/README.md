# JSON to CSV Converter

This Python program reads a JSON file containing a list of objects, dynamically extracts all unique keys, and writes the data to a CSV file. The program handles missing keys and ensures that all keys, whether present in every object or not, are included as columns in the CSV.

## How It Works

1. **Input JSON File**: The program reads the `input.json` file, which contains a list of JSON objects. Each object represents a record with key-value pairs.
   
2. **Extract Unique Keys**: The program iterates through each object and collects all unique keys present in the objects. These keys will become the **columns** in the CSV output.

3. **Generate CSV Header**: The unique keys are combined into a single row to serve as the **header** of the CSV file. The header is written as a comma-separated string of keys.

4. **Write CSV Rows**: The program loops through each object and creates a row for the CSV. For each object:
   - It retrieves the value for each key in the header. 
   - If a key is missing in an object, an empty value is inserted for that key.
   - Each row is created as a comma-separated string of values and added below the header.

5. **Output CSV File**: The program writes the header and the dynamically generated rows into a file called `output.csv`.

## Example

#### Input (`input.json`):
```json
[
    {"Name": "Alice", "age": 30, "birthyear": 1994},
    {"Name": "Bob", "birthyear": 1999},
    {"Name": "Charlie", "age": 22, "city": "New York"}
]
```
#### Output (`output.csv`):
```sql
Name,age,birthyear,city
Alice,30,1994,
Bob,,1999,
Charlie,22,,New York
```
## Features
Dynamic Header Generation: The program automatically detects all keys in the JSON objects, ensuring that the CSV columns match the data.
Handles Missing Data: If a key is missing from an object, the program fills that field with an empty value in the CSV.
CSV Formatting: The output is correctly formatted as a CSV, with comma-separated values, making it suitable for use in spreadsheet applications like Excel.

## How to Use
Place your JSON data in a file named input.json.
Run the Python script.
The script will generate an output.csv file with the converted data.

## Dependencies
Python 3.11
The json module (built-in Python library, no installation required)

## Error Handling
The program includes a try-except block to catch any errors during execution. If an error occurs (e.g., the input file doesn't exist or the data is improperly formatted), it will print the error message.
