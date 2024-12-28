import json

if __name__ == '__main__':
    try:
        # Read the JSON file
        with open('input.json', 'r') as f:
            data = json.loads(f.read())

        # Get all unique keys from the JSON objects
        all_keys = set()
        for obj in data:
            all_keys.update(obj.keys())
        all_keys = list(all_keys)  # Convert to a list for consistent order

        # Create the CSV header
        output = ','.join(all_keys)

        # Create the CSV rows dynamically
        for obj in data:
            row = [str(obj.get(key, "")) for key in all_keys]  # Use .get() to handle missing keys
            output += f'\n{",".join(row)}'

        # Write to the CSV file
        with open('output.csv', 'w') as f:
            f.write(output)

    except Exception as ex:
        print(f'Error: {str(ex)}')