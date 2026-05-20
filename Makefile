run:
	@python3 -m src
clean:
	rm -rf .mypy_cache
	rm -rf src/__pycache__
	rm -rf src/.mypy_cache
	rm -rf llm_sdk/__pycache__
	rm -rf llm_sdk/llm_sdk/__pycache__