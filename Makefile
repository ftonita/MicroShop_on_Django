SRC = TestShop/manage.py

TARGET = runserver

all: imports
	@python3 $(SRC) $(TARGET)
	
imports:
	@pip install --no-cache-dir -r requirements.txt
	@pip install --no-cache-dir -r requirements.txt
	@echo "Modules have been imported"
