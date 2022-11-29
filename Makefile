all: build run
	
build:
	docker build -t testshop .

run:
	docker run -it --rm --name testshopapp -p 8000:8000 testshop