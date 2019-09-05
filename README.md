**Initial Setup**
Make sure pipenv is installed.
Run pipenv shell
To get the necessary packages, run pipenv install --skip-lock
Edit the config.py file to reconfigure where the appropriate directories are
Afterwards, run setup.sh

**Running the Program**
The main driver of this program is in run.sh and xrun.sh 
Pre-processing is done through calculate_features.py and preprocess.py
Running the models is done through run-model.sh

To start the cross-validation, run xrun.sh NameOfRun
Each NameOfRun should be unique as possible
