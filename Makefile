tests:
	py.test app/*

coverage:
	py.test --cov-config .coveragerc --cov app/* app/* --cov-report term-missing
