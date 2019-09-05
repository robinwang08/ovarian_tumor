
pipenv run python xrun.py --trials 10 --description $1 --model v1 --form t1 --label outcome --hyperparameters xhyperparameters.json
pipenv run python xrun.py --trials 10 --description $1 --model v1 --form t2 --label outcome --hyperparameters xhyperparameters.json
pipenv run python xrun.py --trials 10 --description $1 --model v1 --form features --label outcome --hyperparameters xhyperparameters.json