# news-recommendation
This is a web app that:
- Built with React.
- Collect news from multiple news sources and apply ML(tf-idf) to remove duplicates,
- Service Oriented, multiple backend servces commucating through jsonrpc, 
- Automatically recommend news based on user click logs. 

Click here to see the demo




## pylint
specify which python version to use
```
python2 -m pylint cloudAMQP_client.py
```


To modify a file in place (with aggressive level 2):

```
autopep8 --in-place --aggressive --aggressive <filename>
```

## mongodb

start/stop
```bash
brew services start mongodb
brew services stop mongodb
```
