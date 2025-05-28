ine:
            continue  # skip blank or whitespace-only lines

        parts = line.split()
        if len(parts) == 0:
            continue  # extra guard, though usually not needed

        if re.match(r"^[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}$", parts[0], re.IGNORECASE):