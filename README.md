## ***Desafio***
O Projeto tem como objetivo disponibilizar os dados disponíveis no Banco de dados Postgres através de uma API Rest

### *Serviço Globo*
```
.
├── Makefile
├── README.md
├── SOLUTION.md
├── service
│   ├── src
│   │   ├── raw
│   │   │   ├── clientes.csv
│   │   ├── processed
│   │   │   ├──artigo_recomendados_por_similaridade.csv
│   │   │   ├──artigos_recomendados_por_popularidade.csv
│   │   ├── create_table.sql
│   ├── api
│   │   ├── app
│   │   │   ├── requirements.txt
│   │   │   ├── Dockerfile
│   │   │   ├── view.py
│   ├── pgadmin
│   │   ├── pgadmin4.db
│   ├── notebooks
│   │   ├── recomendar_artigos.ipynb
│   ├── Dockerfile
│   ├── docker-compose.yml
```


----------


#### Arquitetura utilizada: 

![arquitetura](https://user-images.githubusercontent.com/28897059/65170634-7e574280-da1f-11e9-80d9-19fd761d7c3f.png)



----------


#### Inicialização
Comandos para realizar o Build das imagens que serão utilizados.

```bash
make step
```

Comandos para rodar os serviços que serão utilizados.

```bash
make run
```
Jupyter para visualizar o modelo criado de recomendação.

```bash
make jupyter
```
***Password:*** `bigdatageo123`


----------


####  ***API***

##### POST `/<url>/exemplo`:
Exemplo de retorno:
```
[{"UserId": "3", "NomeCLiente": "Alice", "Produto_Recomendado": "168868"}, {"UserId": "13", "NomeCLiente": "Eduardo", "Produto_Recomendado": "338351"}]
```
Post da lista de artigo recomendados.

```bash
curl -X POST 'http://localhost:5003/list_recommend_for_similarity/globoplay.com'
```
Post da lista de artigo mais populares.

```bash
curl -X POST 'http://localhost:5003/list_recommend_for_popularity/globoplay.com'
```

Post da lista dos artigos mais visualizados.

```bash
curl -X POST 'http://localhost:5003/list_accesses_article/globoplay.com'
```

##### DELETE `/`:
Post referente ao delete das informações utilizadas.

```bash
curl -X POST 'http://localhost:5003/delete/globoplay.com'
```

##### GET `/<url>/exemplo`:

Exemplo de retorno:
```json
// 20190918172257
// http://localhost:5003/list_recommend_for_similarity/globoplay.com

[
  {
    "UserId": "3",
    "NomeCLiente": "Alice",
    "Produto_Recomendado": "168868"
  },
  {
    "UserId": "13",
    "NomeCLiente": "Alice",
    "Produto_Recomendado": "338351"
  }
]
```

Get da lista de artigo recomendados.

```bash
http://localhost:5003/list_recommend_for_similarity/globoplay.com
```
Get da lista de artigo mais populares.

```bash
http://localhost:5003/list_recommend_for_popularity/globoplay.com
```

Get da lista dos artigos mais visualizados.

```bash
http://localhost:5003/list_accesses_article/globoplay.com
```

----------