import re
from htmlnode import ParentNode
from inline_markdown import text_to_children

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

def block_to_html_node(block: str) -> ParentNode:
    '''Return a HTMLNode depending of the type of block.'''
    block_type = block_to_block_type(block)
    if block_type == "paragraph":
        return paragraph_to_html_node(block)
    if block_type == "heading":
        return heading_to_html_node(block)
    if block_type == "code":
        return code_to_html_node(block)
    if block_type == "ordered_list":
        return olist_to_html_node(block)
    if block_type == "unordered_list":
        return ulist_to_html_node(block)
    if block_type == "quote":
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")

def paragraph_to_html_node(block: str) -> ParentNode:
    '''Format a paragraph block to a ParentNode'''
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block: str) -> ParentNode:
    '''Format a heading block to a ParentNode'''
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block: str) -> ParentNode:
    '''Format a code block to a ParentNode'''
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def olist_to_html_node(block: str) -> ParentNode:
    '''Format a olist block to a ParentNode'''
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block: str) -> ParentNode:
    '''Format a ulist block to a ParentNode'''
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block: str) -> ParentNode:
    '''Format a quote block to a ParentNode'''
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def markdown_to_html_node(markdown: str) -> ParentNode:
    '''Convert a full markdown document into a single parent HTMLNode.'''
    markdown_blocks = markdown_to_blocks(markdown)
    children_node = []    

    for block in markdown_blocks:
        html_node = block_to_html_node(block)
        children_node.append(html_node)

    return ParentNode("div", children_node, None)