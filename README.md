# API-Innovaccer Challenge

### Install
=====
### Install all the dependency using `pip`
```bash
pip install -r requirements.txt
```
### Set Env Twitter OAuth
#### Use export for linux and set for windows 

```bash
export TWITTER_CONSUMER_KEY=YOUR KEY
export TWITTER_CONSUMER_SECRET=YOUR KEY
export TWITTER_ACCESS_TOKEN=YOUR KEY
export TWITTER_ACCESS_TOKEN_SECRET=YOUR KEY
```
### Installing ElasticSearch(Nosql DB)

#### Here is the [link](https://www.elastic.co/downloads/elasticsearch) to download elasticsearch
#### Follow the instructions and check elasticsearch is running or not

```bash
 Run curl http://localhost:9200/ 
 or 
 Invoke-RestMethod http://localhost:9200 with PowerShell
```
### Usage
====
### Get Help
```bash
usage: innov-api.py [-h] [--esload]

Welcome to

optional arguments:
  -h, --help  show this help message and exit
  --esload    Fetch tweets from twitter and load ES index

```
### Index ElasticSearch
#### Run the below command and start indexing twitter api data into elasticsearch
```bash
python innov-api --esload
```
### Run the server
```bash
python innov-api.py
```
```bash
Head to http://localhost/api/all/tweets/ to get all the streaming tweets and its metadata
```
### For API Documentation please refer API.pdf file
