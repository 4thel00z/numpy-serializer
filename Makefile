build:
	python3 setup.py sdist bdist_wheel
upload:
	./scripts/upload.zsh
