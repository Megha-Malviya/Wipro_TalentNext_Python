try:
    file_name = input("Enter the file name: ")
    if not file_name.endswith(".txt"):
        file_name = file_name + ".txt"

    with open(file_name, "r") as f:
        # Read all non-empty lines while preserving blank line separators
        raw_lines = f.readlines()

    # Normalize lines
    lines = [line.strip() for line in raw_lines]

    items = 0
    free_items = 0
    amount = 0
    discount = 0

    # Stage: 1 = items, 2 = free+discount
    stage = 1
    for line in lines:
        if line == "":
            stage += 1
            continue

        parts = line.split()
        # Some lines may have extra spaces; merge everything except last as name
        name = " ".join(parts[:-1])
        value = parts[-1]

        if stage == 1:
            if value.lower() == "free":
                free_items += 1
            else:
                items += 1
                amount += int(value)
        elif stage >= 2:
            if value.lower() == "free":
                free_items += 1
            elif name.lower() == "discount":
                discount = int(value)
            else:
                items += 1
                amount += int(value)

    final_amount = amount - discount

    print("No of items purchased:", items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("File not found")
