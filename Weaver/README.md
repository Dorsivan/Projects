# How to Dockerize a Celery App With RabbitMQ

**Docker and docker-compose are needed.**

### In order to use this Docker container:

1. Bring up Terminal or CMD and go to the directory Weaver

2. Once in Weaver, bring up docker with: 
	```docker-compose build```

3. When it is finished, we can use:
	```docker-compose up```

4. Go to [localhost:4555](https://localhost:4555)

5. In order to look at database data use: 
	[localhost:4555/results/1](https://localhost:4555/results/1) (any number will do)

6. In order to enter data into this database use a POST request (with Postman for example) 
	use the line ```localhost:4555/upload```, in the body you can enter:
	```
	{
	"97":"[1,2,3,4,5]"
	}
	```
	for example.
	We can now go to [localhost:4555/results/74](https://localhost:4555/results/74) and get the value of the mul of the numbers we entered.
	The numbers are arbitrary and any will do.
