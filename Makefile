run:
	uvicorn api.main:app --reload
test:
	pytest tests/
