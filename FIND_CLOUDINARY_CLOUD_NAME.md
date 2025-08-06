# CLOUDINARY SETUP INSTRUCTIONS

## Problem: Invalid cloud_name 'dxy6qkvvr'

The Cloudinary upload is failing because the cloud name is incorrect.

## How to Find Your Correct Cloud Name:

### Method 1: Check Cloudinary Dashboard
1. Go to https://cloudinary.com/console
2. Log in with your account 
3. On the main dashboard, you'll see:
   ```
   Cloud name: [YOUR_ACTUAL_CLOUD_NAME]
   API Key: 475639282489246
   API Secret: [hidden, but we have: JwqWJehhIo8klbtUrG4ZAuaean0]
   ```

### Method 2: Check Account Settings
1. In Cloudinary dashboard, go to Settings → Account
2. Look for "Cloud name" field
3. Copy the exact value

### Method 3: Check URL Pattern
When you upload an image to Cloudinary, the URL format is:
```
https://res.cloudinary.com/[CLOUD_NAME]/image/upload/...
```

## Once You Find the Correct Cloud Name:

Update your `env.py` file:
```python
os.environ.setdefault("CLOUDINARY_CLOUD_NAME", "your-actual-cloud-name-here")
```

## Common Cloud Name Patterns:
- Usually lowercase
- May contain hyphens
- Often related to your account name or project
- Examples: "demo-account", "my-project-123", "john-smith-dev"

## Test the Fix:
After updating env.py with the correct cloud name, run:
```bash
python manage.py upload_cloudinary
```

Please check your Cloudinary dashboard and let me know what your actual cloud name is!
