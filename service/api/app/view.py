import psycopg2
import pandas as pd
import sys
import json


from flask import Flask,jsonify, Response
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def recommend_for_similarity ():
    con = psycopg2.connect(host='globo-db',port=5432, database='postgres', user='postgres', password='')
    cur = con.cursor()
    psql="""select user_id, user_name, recommended_link  from globo.artigo_recomen_similarity order by user_name"""
    cur.execute(psql)
    result = cur.fetchall()
    list_results = []
    for row in result:
        dic = { "UserId":row[0],
                "CLienteName":row[1],
                "ArticleSimilarity": row[2]
                }
        list_results.append(dic)
    return list_results

def recommend_for_popular():
    con = psycopg2.connect(host='globo-db',port=5432, database='postgres', user='postgres', password='')
    cur = con.cursor()
    psql="""select user_id, user_name, recommended_link  from globo.artigo_recomen_popularity  order by user_name"""
    cur.execute(psql)
    result = cur.fetchall()
    list_results = []
    for row in result:
        dic = { "UserId":row[0],
                "CLienteName":row[1],
                "ArticlePopularity": row[2]
                }
        list_results.append(dic)
    return list_results

def accesses_article():
    con = psycopg2.connect(host='globo-db',port=5432, database='postgres', user='postgres', password='')
    cur = con.cursor()
    psql="""select recommended_link, count(*) accesses  from globo.artigo_recomen_popularity group by recommended_link order by recommended_link limit 10"""
    cur.execute(psql)
    result = cur.fetchall()
    list_results = []
    for row in result:
        dic = { "Article":row[0],
                "Accesses":row[1]
                }
        list_results.append(dic)
    return list_results


def delete_tables():
    con = psycopg2.connect(host='globo-db',port=5432, database='postgres', user='postgres', password='')
    cur = con.cursor()
    psql="""TRUNCATE globo.artigo_recomen_popularity, globo.artigo_recomen_similarity"""
    cur.execute(psql)
    
@app.route('/',methods=['GET'])
def helloIndex():
    return 'API Globo Recomendação de Produtos'

@app.route('/list_recommend_for_similarity/globoplay.com',methods=['GET', 'POST'])
def list_recommend_for_similarity():
    recom_product = recommend_for_similarity()
    return Response(json.dumps(recom_product), status=200)

@app.route('/list_recommend_for_popularity/globoplay.com',methods=['GET', 'POST'])
def list_recommend_for_popular():
    pop_products = recommend_for_popular()
    return Response(json.dumps(pop_products), status=200)

@app.route('/list_accesses_article/globoplay.com',methods=['GET', 'POST'])
def list_article():
    article = accesses_article()
    return Response(json.dumps(article), status=200)

@app.route('/delete/globoplay.com',methods=['POST'])
def delete_products():
    delete_tables()
    return "delete"

if __name__ == '__main__':  
    app.run(host='globo-api', port='5003', debug=True)
