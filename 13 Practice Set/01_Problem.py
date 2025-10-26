virtualenv env1
virtualenv env2

.\env1.\Scripts.\activate.ps1
pip install pandas
pip install pyjokes
pip freeze > requirement.txt

deactivate

.\env2.\Scripts.\activate.ps1
pip install -r requirement.txt
