build:
	docker-compose build

down:
	docker-compose down --volumes --remove-orphans

run:
	make down && docker-compose up

run-scaled:
	make down && docker-compose up --scale spark-worker=2

run-d:
	make down && docker-compose up -d

stop:
	docker-compose stop

submit:
	docker exec da-spark-master spark-submit --master spark://spark-master:7077 --deploy-mode client ./apps/$(app)

submit-cluster:
	docker exec da-spark-master spark-submit --master spark://spark-master:7077 --deploy-mode cluster ./apps/$(app)

rm-results:
	rm -r book_data/results/*
