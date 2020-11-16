import tldextract

def extract(url: str):
    """Extract the correct formatting for a passed url.

    'http://www.something.com/home.html?abc'->'something.com'
    'https://app.example.co.uk/something.html'->'app.example.co.uk'

    Args:
        url (str): Any url-like string
    Raises:
        Exception: if suffix is not valid (i.e. .com, .co, etc.)
    Returns:
        str: cleaned url with only wanted parts.
    """
    if isinstance(url, str):
        subdomain, domain, suffix = tldextract.extract(url)
        # Exclude www subdomain, keep the rest
        # Check if format is valid
        if domain and suffix:
            if subdomain:
                if subdomain=='www':
                    subdomain = ''
                if 'www.' in subdomain:
                    subdomain = subdomain.replace('www.','')
            if subdomain:
                return subdomain+'.'+domain+'.'+suffix
            return domain+'.'+suffix
        else:
            raise Exception('Invalid url format: %s Check url suffix.'%(url))
    else:
        raise Exception('URL must me string.')