import re

def clean_content_for_word_count(content):
    """
    Cleans HTML and MkDocs-specific syntax from content to prepare it for an
    accurate word count.
    """
    text = content

    # 1. Remove HTML tags, leaving the content inside
    text = re.sub(r'<[^>]+>', ' ', text)

    # 2. Remove specific patterns that are known to be noise and not words.
    # This is more targeted and safer than trying to remove all punctuation.
    patterns = [
        r'\{[^}]*\}',      # {.annotate}, {:target="_blank"}, etc.
        r'<!--.*?-->',     # HTML comments
        r'\[\^[^\]]+\]:?', # Footnote references like [^1]
        r'\(\d+\)',        # In-text annotation numbers like (1), (2)
        r'\b\d+\.',        # Numbered list markers like "1.", "2."
    ]
    for pattern in patterns:
        text = re.sub(pattern, ' ', text)

    # 3. Handle specific abbreviations
    text = re.sub(r'\bi\.e\.', 'ie', text)
    text = re.sub(r'\be\.g\.', 'eg', text)

    # 4. Use re.findall to extract anything that looks like a word.
    # A "word" is defined as a sequence of alphanumeric characters that can
    # contain internal hyphens or apostrophes (e.g., "well-being", "I'm").
    # This correctly includes numbers like "2023" in the count.
    words = re.findall(r"[\w'-]+", text)

    # 5. As a safeguard, filter out any "words" that are just stray punctuation,
    # which can sometimes be matched by the regex.
    final_words = [word for word in words if word.strip("'-")]

    return len(final_words)


def on_page_content(html, page, **kwargs):
    if html:
        word_count = clean_content_for_word_count(html)
        page.meta['word_count'] = word_count
    return html