local/run:
	python main.py

local/dev:
	uvicorn main:app --reload