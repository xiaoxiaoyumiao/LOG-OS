# Installation

## Installation

The package itself can be easily installed by

```text
pip install nltk
```

But those corpora and models it's depending on need to be downloaded separately. They can be downloaded by python script:

```python
nltk.download() # interactive installation for all data
nltk.download("punkt") # download certain package
```

To customize where to store the `nltk` data, an environment variable named `NLTK_DATA` should be configured to the custom data path \(usually named `nltk_data` \).

The download process can be also run from command line:

```bash
# -d to specify path, but ensure $NLTK_DATA is set properly
python -m nltk.downloader -d /usr/local/share/nltk_data all
```

Sometimes we have to manually download the data due to connection issues or something. All packages can be download from \(ref: \[2\]\). Packages are provided in .zip and must be extracted to a proper location under the `NLDK_DATA` directory. If you are downloading a certain package following instructions from `nltk`  python script error like:

```python
import nltk
from nltk.tokenize import word_tokenize
sent = nltk.word_tokenize(sent)

# output:

...

LookupError: 
**********************************************************************
  Resource punkt not found.
  Please use the NLTK Downloader to obtain the resource:

  >>> import nltk
  >>> nltk.download('punkt')
  
  For more information see: https://www.nltk.org/data.html

  Attempted to load tokenizers/punkt/PY3/english.pickle
  
...
```

Then it's easy to know where to put the downloaded `punkt` data by looking at the attempted lookup path. In this case, just make a directory `tokenizers` under `NLDK_DATA` directory and extract `punkt` content there.

## Reference

\[1\] NLTK Documentation: [https://www.nltk.org/data.html](https://www.nltk.org/data.html)

\[2\] NLTK data download page: [http://www.nltk.org/nltk\_data/](http://www.nltk.org/nltk_data/)

