import re

def markdown_to_blocks(markdown: str) -> list:
    '''Convert raw mardown string (full document) into a list of block strings.'''
    markdown_blocks = []

    blocks = markdown.split("\n\n")

    for block in blocks:
        block = block.strip()
        if block:
            markdown_blocks.append(block)

    return markdown_blocks

def block_to_block_type(block: str) -> str:
    '''Return the type of markdown block as a:
        - paragraph
        - heading
        - code
        - quote
        - unordered_list
        - ordered_list
        '''

    heading_pattern = r"\#{1,6}\s+.*"
    code_pattern = r"\`{3}[\s\S]*\`{3}"
    quote_pattern = r"(?m)^>\s+.*"
    unordered_list_pattern = r"(?m)^[\*\-]\s+.*"
    ordered_list_pattern = r"(?m)^\d+\.\s+.*"

    if re.match(heading_pattern, block):
        return "heading"
    elif re.match(code_pattern, block):
        return "code"
    elif re.match(quote_pattern, block):
        return "quote"
    elif re.match(unordered_list_pattern, block):
        return "unordered_list"
    elif re.match(ordered_list_pattern, block):
        expected = 1
        for line in block.splitlines():
            if line.strip():
                number = int(line.split('.')[0])
                if number != expected:
                    return "paragraph"
                expected += 1
        return "ordered_list"
    return "paragraph"
