import re

count_of_barcodes = int(input())

for barcode in range(count_of_barcodes):
    current_barcode = input()
    pattern = r"\@#+([A-Z][A-Za-z0-9]{4,}[A-Z])\@\#+"
    result = re.findall(pattern, current_barcode)
    if result:
        extract_numbers = re.findall("\d", current_barcode)
        if extract_numbers:
            print(f"Product group: {''.join(extract_numbers)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
