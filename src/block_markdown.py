def markdown_to_blocks(markdown: str) -> list:
    '''Convert raw mardown string (full document) into a list of block strings.'''
    markdown_blocks = []

    blocks = markdown.split("\n\n")

    for block in blocks:
        block = block.strip()
        if block:
            markdown_blocks.append(block)

    return markdown_blocks