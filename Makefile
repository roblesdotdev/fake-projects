run:
	uvicorn fake_projects.app:app --reload
format:
	black *.py fake_projects/*.py