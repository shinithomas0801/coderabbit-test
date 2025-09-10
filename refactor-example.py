def messy_read_and_process(file_path, callback):
    try:
        f = open(file_path, 'r', encoding='utf-8')
        data = f.read()
        f.close()
    except Exception as e:
        print("Oops!!! Something bad happened!!!")
        callback(e, None)
        return

    all_lines = data.split('\n')
    final_output = []

    for i in range(len(all_lines)):
        current_line = all_lines[i]
        if current_line != "" and current_line != " " and current_line is not None:
            lower_line = current_line.lower()
            letters = list(lower_line)
            temp_word = ""
            words_arr = []
            
            for j in range(len(letters)):
                char = letters[j]
                if char == " " or char == "\t":
                    if temp_word != "":
                        words_arr.append(temp_word.replace('.', '').replace(',', '').replace('!', '').replace('?', ''))
                        temp_word = ""
                else:
                    temp_word += char
            
            if temp_word != "":
                words_arr.append(temp_word.replace('.', '').replace(',', '').replace('!', '').replace('?', ''))

            combined = ""
            for k in range(len(words_arr)):
                combined += words_arr[k]
                if k < len(words_arr) - 1:
                    combined += "_"
            
            final_output.append(combined)

    result_string = ""
    for x in range(len(final_output)):
        result_string += final_output[x] + "\n"

    callback(None, result_string)

