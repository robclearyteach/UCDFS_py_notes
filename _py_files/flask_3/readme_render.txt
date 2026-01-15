##
# Project Tip (/recommend)
## THEN:
## 	 	See descriptor and recommend
##
##	'readme_venv.md'
##
##	Where that file documents 
##		1. use of venv  (show commands)
#Steps to create venv
folder:
> python3 -m venv .env  
#creates the venv

#activate it 
> source ./.env/bin/activate

#see (.env) on prompt

...
# installing from requirements.txt
> pip install -r requirements.txt

<show sample output from your execution>

#flask --app app run --debug --port 8000
sample output (log)

similarly gunicorn

#gunicorn app:app
>sample output (log)





##		2. requirements.txt (generation pip freeze)
##		3. addition of gunicorn (for render)
##		4. pip install -r  (for loading a new project)