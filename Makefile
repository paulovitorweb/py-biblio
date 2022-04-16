#
# Run api for development
dev:
	uvicorn src.pybiblio.api.main:app --reload

#
# Run tests
test:
	pytest

#
# Run lint
lint:
	flake8
	@echo "No lint problems found"

#
# Run lint and tests
check:
	make lint
	make test