def read_and_process(file_path, callback):
    import string

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
    except Exception as e:
        callback(e, None)
        return

    lines = data.splitlines()
    output_lines = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # Lowercase
        lowered = stripped.lower()
        # Remove punctuation (.,!?) only
        cleaned = lowered.translate(str.maketrans('', '', '.,!?'))
        # Split on whitespace
        words = cleaned.split()
        if words:
            output_lines.append('_'.join(words))

    result = '\n'.join(output_lines) + '\n' if output_lines else ''
    callback(None, result)
