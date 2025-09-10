def messy_read_and_process(file_path, callback):
    import string

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
    except Exception as e:
        print("Oops!!! Something bad happened!!!")
        callback(e, None)
        return

    final_output = []
    for line in data.splitlines():
        # Strip whitespace and skip empty lines
        stripped = line.strip()
        if not stripped:
            continue
        # Lowercase and split into words
        words = [
            word.strip(string.punctuation)
            for word in stripped.lower().split()
            if word.strip(string.punctuation)
        ]
        combined = "_".join(words)
        final_output.append(combined)

    result_string = "\n".join(final_output) + ("\n" if final_output else "")
    callback(None, result_string)
