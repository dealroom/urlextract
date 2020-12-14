# urlextract
Wrapper class for extracting only wanted parts from urls.

## Install
`pip install -e git+https://github.com/dealroom/data-urlextract.git#egg=dealroom-urlextract`

## Usage
```python
>>> from dealroom_urlextract import extract

>>> extract('http://www.something.com/home.html?abc')
something.com
```

## Notes

Based on [tldextract](https://github.com/john-kurkowski/tldextract).