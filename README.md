# urlextract
Wrapper class for extracting only wanted parts from urls.

## Install
`pip install -e git+https://github.com/dealroom/urlextract.git`

## Usage
```python
>>> from urlextract import extract

>>> extract('http://www.something.com/home.html?abc')
something.com
```

## Notes

Based on [tldextract](https://github.com/john-kurkowski/tldextract).