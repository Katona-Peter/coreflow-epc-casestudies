# Cloudinary Setup Instructions

## Step 1: Create Cloudinary Account
1. Go to https://cloudinary.com
2. Click "Sign Up for Free"
3. Create your account with email/password
4. Verify your email if required

## Step 2: Get Your Credentials
1. After login, go to your Dashboard (https://cloudinary.com/console)
2. You'll see three important values:
   - **Cloud Name** (e.g., "dxy123abc")
   - **API Key** (e.g., "123456789012345")
   - **API Secret** (e.g., "AbCdEfGhIjKlMnOpQrStUvWxYz")

## Step 3: Update Your Local Environment
Update your `env.py` file with the actual values:

```python
# Replace these with your actual Cloudinary credentials
os.environ.setdefault("CLOUDINARY_CLOUD_NAME", "your-actual-cloud-name")
os.environ.setdefault("CLOUDINARY_API_KEY", "your-actual-api-key") 
os.environ.setdefault("CLOUDINARY_API_SECRET", "your-actual-api-secret")
```

## Step 4: Update Heroku Environment Variables
In your Heroku Dashboard:
1. Go to your app → Settings → Config Vars
2. Add these three variables:
   - `CLOUDINARY_CLOUD_NAME` = your-cloud-name
   - `CLOUDINARY_API_KEY` = your-api-key
   - `CLOUDINARY_API_SECRET` = your-api-secret

## Step 5: Run Migration and Upload Images
After updating the credentials:

```bash
# Create and apply migration
python manage.py makemigrations
python manage.py migrate

# Upload images to Cloudinary (edit upload_to_cloudinary.py first)
python upload_to_cloudinary.py

# Load case study data
python manage.py load_case_study_data

# Test locally
python manage.py runserver
```

## Step 6: Deploy to Heroku
```bash
git add .
git commit -m "Added Cloudinary integration for reliable image hosting"
git push origin main
# Then deploy via Heroku Dashboard
```

## Benefits of Cloudinary:
- ✅ **Reliable image hosting** - works in development and production
- ✅ **Automatic image optimization** - faster loading times
- ✅ **CDN delivery** - global content delivery network
- ✅ **Image transformations** - resize, crop, format conversion
- ✅ **Free tier** - 25GB storage and 25GB monthly bandwidth

## Free Tier Limits:
- 25GB total storage
- 25GB monthly bandwidth
- 25,000 images/videos
- Basic transformations included

This should be more than enough for your case study project!
