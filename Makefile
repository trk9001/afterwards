# Important: Use hard tabs only.
# Note: The first target is the default one.

# Namespace type thing
.PHONY: test install

# Run tests
test:
	pytest -v

# Run tests and show coverage
test-cov:
	pytest --cov=aw

# Clean up test by-products
clean:
	rm -f .coverage
	rm -rf .pytest_cache

# Run setup sccript
install:
	./setup.sh
