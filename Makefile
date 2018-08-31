# Run tests
test:  # Being the first, this is the default target
	pytest -v

# Run tests and show coverage
test-cov:
	pytest --cov=aw

# Run setup sccript
install:
	./setup.sh
