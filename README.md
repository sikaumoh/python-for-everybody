# Python For Everybody

> This is a documentation of my python lessons.

---

### Table of Contents

- [Data Structure](#data-structure)
- [Web Access](#web-access)
- [Database Access](#database-access)
- [Author Info](#author-info)

---

## Data Structure

Data Structures are the ways to organize data, read them, and work with them. These are the types of data structures: lists, tuples, and dictionaries.

```python
    # list
    list = [1, 2, 3]

    # tuple
    tuple = (1, 2, 3)

    # dictionary
    dictionary = {a: 1, b: 2, c: 3}
```

[Back To The Top](#python-for-everybody)

---

## Web Access
Web Access section is about web crawling on html, and xml based sites.
Download [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) to make it easy reading html tags.

#### Crawling HTML Sites
```python
    # For crawling html sites
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    # Ignore SSl certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Opening url content
    url = 'https://en.wikipedia.org/wiki/Anime'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
```

#### Crawling XML Sites
```python
  import urllib.request, urllib.parse, urllib.error
  import ssl

  # Ignore SSL certificate errors
  ctx = ssl.create_default_context()
  ctx.check_hostname = False
  ctx.verify_mode = ssl.CERT_NONE

  # getting data
  url = 'http://py4e-data.dr-chuck.net/comments_1187247.xml'
  data = urllib.request.urlopen(url).read()
```

[Back To The Top](#python-for-everybody)

---

## Database Access

```html
    <p>dummy code</p>
```

[Back To The Top](#python-for-everybody)

---

## Author Info

- LinkedIn - [@Nsikakabasi Umoh](https://www.linkedin.com/in/nsikakabasi-umoh-05bb351b8/)

[Back To The Top](#python-for-everybody)
