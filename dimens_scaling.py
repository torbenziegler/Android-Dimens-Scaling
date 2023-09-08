import xml.etree.ElementTree as ET
import re

# Define the XML file path
xml_file_path = input('Enter the path to the dimens.xml file: ') 

# Define the new value you want to set for dp
dp_scaling_value = float(input('Enter the dp scaling value: '))

# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Loop through all dimen elements and update their values
for dimen_elem in root.findall('.//dimen'):
    # extract the number dimen
    match = re.search(r'(-?\d+(\.\d+)?)(dp|sp)', dimen_elem.text)
    
    if match:
        extracted_number = float(match.group(1))  # Extract the numeric part
        unit = match.group(3) # Extract the unit (dp or sp)
        new_value = extracted_number * dp_scaling_value
        if new_value % 1 != 0:
            new_value = round(new_value, 3)
        dimen_elem.text = f'{new_value}{unit}'
    else:
        print("No number found in the string:", dimen_elem.text)

# Save the modified XML back to the file
tree.write(xml_file_path, encoding='utf-8')

print(f'Updated dp values in {xml_file_path}')
