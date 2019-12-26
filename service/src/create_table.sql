--- Criando banco de dados e usuário que será owner do projeto recomendação

CREATE USER globo WITH PASSWORD 'globo' ;
CREATE SCHEMA IF NOT EXISTS globo AUTHORIZATION postgres;
ALTER DEFAULT PRIVILEGES IN SCHEMA globo GRANT SELECT, INSERT, UPDATE, DELETE, TRUNCATE ON TABLES TO globo;
ALTER DEFAULT PRIVILEGES IN SCHEMA globo GRANT USAGE, SELECT ON SEQUENCES  TO globo;

--- Criando tabela de artigos recomendação por similaridade

CREATE TABLE globo.artigo_recomen_similarity (
                user_id VARCHAR (500),
                user_name VARCHAR (500),  
                recommended_link VARCHAR (500)
);

copy  globo.artigo_recomen_similarity from '/src/processed/artigo_recomendados_por_similaridade.csv' with delimiter '|' csv header encoding 'windows-1251';

--- Criando tabela de artigos recomendação por popularidade

CREATE TABLE globo.artigo_recomen_popularity (
                user_id VARCHAR (500),
                user_name VARCHAR (500),  
                recommended_link VARCHAR (500)
);

copy  globo.artigo_recomen_popularity from '/src/processed/artigos_recomendados_por_popularidade.csv' with delimiter '|' csv header encoding 'windows-1251';
