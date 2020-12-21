import tldextract

def extract(url: str):
    """Extract the correct formatting for a passed url.

    >>> extract('http://www.something.com/home.html?abc')
    'something.com'
    >>> extract('https://app.example.co.uk/something.html')
    'app.example.co.uk'

    Args:
        url (str): Any url-like string
    Raises:
        Exception: if suffix is not valid (i.e. .com, .co, etc.)
    Returns:
        str: cleaned url with only wanted parts.
    """
    if isinstance(url, str):
        subdomain, domain, suffix = tldextract.extract(url.lower())
        # Exclude www subdomain, keep the rest
        # Check if format is valid
        if domain and suffix:
            if subdomain:
                if subdomain=='www':
                    subdomain = ''
                if 'www.' in subdomain:
                    subdomain = subdomain.replace('www.','')
            website = domain+'.'+suffix
            if subdomain:
                website = subdomain+'.'+website
            return website.lower().strip()
        else:
            raise Exception('Invalid url format: %s Check url suffix.'%(url))
    else:
        raise Exception('URL must be string.')

def extract_with_path(url: str):
    """Extract the correct formatting for a passed url including the path
    and change all '/' into '@'.

    >>> extract_with_path('http://www.something.com/home/asd.html?abc')
    'something.com@home@asd.html'
    >>> extract_with_path('https://app.example.co.uk/en/about/something.html')
    'app.example.co.uk@en@about@something.html'

    Args:
        url (str): Any url-like string
    Raises:
        Exception: if suffix is not valid (i.e. .com, .co, etc.)
    Returns:
        str: cleaned url with only wanted parts.
    """
    url = url.lower().strip()
    base = extract(url)
    path = url.split(base)[-1]
    if len(path) > 0:
        path = path.split('?')[0]
        if path[-1] == '/':
            path = path[:-1]
        path = path.replace('/','@')
    return base + path
