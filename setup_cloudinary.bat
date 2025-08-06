@echo off
echo === Cloudinary Setup and Upload ===
echo.

echo Step 1: Creating migration for Cloudinary field...
python manage.py makemigrations
echo.

echo Step 2: Applying migrations...
python manage.py migrate
echo.

echo Step 3: Loading case study data...
python manage.py load_case_study_data
echo.

echo Step 4: Uploading images to Cloudinary...
python manage.py upload_cloudinary
echo.

echo Step 5: Starting development server...
echo Open browser to http://127.0.0.1:8000 to see your images!
python manage.py runserver

pause
