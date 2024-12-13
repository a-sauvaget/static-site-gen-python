import re

from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: enumerate) -> list:
    '''Return a list of new nodes, where any text typ nodes in the input list are split into multiple node based on the syntax.'''
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        else:
            split_nodes = []
            sections = old_node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise Exception('Invalid markdown, formatted section not closed')
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    # Regular text part (outside delimiters)
                    split_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    # Delimited text part (inside delimiters)
                    split_nodes.append(TextNode(sections[i], text_type))
            new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text: str) -> list:
    '''Takes raw text and returns a list of tuples (alt text + URL).'''
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text: str) -> list:
    '''Takes raw text and returns a list of tuples (anchor text + URL).'''
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches