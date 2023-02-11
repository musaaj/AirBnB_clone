def parse_line(line: str):
    """parse a given string into tokens

    Args:
        line: str

    Description:
        this function splits a given string by space characters or 
        '"'. Characters withing 2 '"' are considered single tokens

    Returns: list of strings
    """
    if line and isinstance(line, str):
        line = line.strip()
        length = len(line)
        token = '';
        result = []
        i = 0;
        while i < length:
            if line[i] == ' ':
                i += 1
                continue
            if line[i] in '"':
                i += 1
                while i < length and line[i] != '"':
                    token += line[i]
                    i += 1
                result.append(token)
                token = ''
                i += 1
            elif i < length:
                while i < length and line[i] != ' ':
                    token += line[i]
                    i += 1
                result.append(token)
                i += 1
                token = ''
        return result
    else:
        return []
