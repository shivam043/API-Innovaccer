"""
Author:Shivam Singh
Email:mavish043@gmail.com
Contact:9718496646
"""
import argparse
from flask import Flask,jsonify
import requests
from elasticsearch import Elasticsearch
from app1 import *


app = Flask(__name__)

@app.route('/api/all/tweets/',methods=['GET'])
def home():
    dic = list()
    data=requests.get('http://localhost:9200/twitter/_search')
    dic.append(data.json())
    return jsonify(dic)
@app.route('/api/tweets/user/<string:term>',methods=['GET'])
def username_search(term):
    data=requests.get('http://localhost:9200/twitter/_search/?q=screen_name:'+term)
    sample_dic = data.json()
    if not sample_dic['hits']['hits']:
        return jsonify({'Error': 'Not Found'}), 404
    return jsonify(data.json()), 200
@app.route('/api/tweets/lang/<string:term>',methods=['GET'])
def lang_search(term):
    data = requests.get('http://localhost:9200/twitter/_search/?q=lang:' + term)
    sample_dic = data.json()
    if not sample_dic['hits']['hits']:
        return jsonify({'Error': 'Not Found'}), 404
    return jsonify(data.json()), 200
@app.route('/api/tweets/text/<string:term>',methods=['GET'])
def tweet_text_search(term):
    data = requests.get('http://localhost:9200/twitter/_search/?q=text:' + term)
    sample_dic=data.json()
    if not sample_dic['hits']['hits']:
        return jsonify({'Error': 'Not Found'}), 404
    return jsonify(data.json()),200
@app.route('/api/tweets/rcount/<int:gt>/<int:lt>',methods=['GET'])
def show_retweet_count_range(gt,lt):
    es = Elasticsearch()

    result=es.search(index="twitter", body={
        "query": {
            "range": {
                "retweet_count": {
                    "gte": gt,
                    "lte": lt,
                }
            }
        }
    })

    if not result['hits']['hits']:
        return jsonify({'Error': 'Not Found'}), 404
    return jsonify(result), 200
@app.route('/api/tweets/fcount/<int:gt>/<int:lt>',methods=['GET'])
def show_followers_count_range(gt,lt):
    es = Elasticsearch()

    result=es.search(index="twitter", body={
            "query": {
                "range": {
                    "followers_count": {
                        "gte": gt,
                        "lte": lt,
                    }
                }
            }
        })

    if not result['hits']['hits']:
        return jsonify({'Error': 'Not Found'}), 404
    return jsonify(result), 200



if __name__ == '__main__':
    #app.run()

    parser = argparse.ArgumentParser(description="Welcome to ")

    parser.add_argument('--esload', dest='run_es_load', action='store_true',
                        help='Fetch tweets from twitter and load ES index ')
    args = parser.parse_args()
    if args.run_es_load:
        es_index()
    else:
        app.run(host='127.0.0.1',port=5000,debug=True)
