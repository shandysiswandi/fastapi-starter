run:
	@uvicorn main:app --reload

lint:
	@ruff check .

format:
	@ruff format .

test:
	@pytest