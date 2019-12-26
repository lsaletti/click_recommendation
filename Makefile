run:
	docker-compose -f service/docker-compose.yml up
	
down:
	docker-compose -f service/docker-compose.yml down

step:
	docker-compose -f service/docker-compose.yml up --build -d

test:
	echo "make test NOT IMPLEMENTED"

jupyter:
		docker run --rm -d -p 8888:8888 --network host -v ${PWD}:/home/jovyan/work --name juspark \
                -m 5g -e GRANT_SUDO=yes -e NB_UID=$(shell id -u) -e NB_GID=$(shell id -g) \
		--user root jupyter/all-spark-notebook:latest  \
		start-notebook.sh --NotebookApp.password='sha1:e30fd9a65062:5cf9b14dd606901627704c7ad8f50b1102defb06'
