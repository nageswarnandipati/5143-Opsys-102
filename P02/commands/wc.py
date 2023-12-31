def wc(file_path, flags, content=None):
    """
    count number of lines/words/characters in file
    Command: wc 
    
    Options:
    -l	: count number of lines in file
    -m	: count number of characters in file
    -w	: count number of words in file
    """
    result_str = ""
    count_lines = False
    count_words = False
    count_chars = False
    for flag in flags:
        if 'l' in flag:
            count_lines = True
        if 'm' in flag:
            count_chars = True
        if 'w' in flag:
            count_words = True
    try:
        if not content:
            with open(file_path, 'r') as file:
                content = file.read()
        
        line_count = len(content.splitlines()) if count_lines else 0
        word_count = len(content.split()) if count_words else 0
        char_count = len(content) if count_chars else 0
        
        if count_lines:
            result_str += f"Lines: {line_count}\n"
        if count_words:
            result_str += f"Words: {word_count}\n"
        if count_chars:
            result_str += f"Characters: {char_count}\n"
        return result_str[:-1]
    
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"