gcloud --quiet app deploy app.yaml
python manage.py collectstatic
npm install popper.js --prefix static