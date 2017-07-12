# Google Spreadsheet api tutorial
===================


# Requirements

- Python 2.7
- virtualenvwrapper


# Install

1. clone git repository

```
  git clone ...
```

2. install requirements

```
mkvirtualenv -a `pwd` google-spreadshet-api -p `which python`
pip install -r requirements.txt
```

3. get client_secret.json from [this website]()

- if you get the file, just move the file to the home directory of your project

```
mv path/to/download_foler/client_secret.json path/to/your/project/client_secret.json
```

4. set enviromental variables

```
export SPREADSHEET_ID = 'spreadsheet id you want to write in'
```

# Execute (or Deploy)

- Everything is ready. Try to write some link in your spreadsheet

```
python app.py
```




