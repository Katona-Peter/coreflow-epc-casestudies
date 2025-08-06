#!/usr/bin/env python
"""
Test Cloudinary connection and find correct cloud name
"""

import cloudinary
import cloudinary.api
import requests

def test_cloudinary_credentials():
    print("=== Testing Cloudinary Credentials ===")
    
    # Test different possible cloud names
    possible_cloud_names = [
        'dxy6qkvvr',
        'dxy6qkvvr-cloudinary',  
        'coreflow-epc',
        'coreflow-epc-casestudies',
        'peter-katona',
        'default-cloud-name'
    ]
    
    api_key = '475639282489246'
    api_secret = 'JwqWJehhIo8klbtUrG4ZAuaean0'
    
    for cloud_name in possible_cloud_names:
        try:
            print(f"\nTesting cloud_name: {cloud_name}")
            
            cloudinary.config(
                cloud_name=cloud_name,
                api_key=api_key,
                api_secret=api_secret,
                secure=True
            )
            
            # Test API call
            result = cloudinary.api.ping()
            print(f"✅ SUCCESS! Cloud name '{cloud_name}' is valid!")
            print(f"Response: {result}")
            return cloud_name
            
        except Exception as e:
            print(f"❌ Failed with '{cloud_name}': {str(e)}")
    
    print("\n❌ None of the cloud names worked.")
    print("\nTo find your correct cloud name:")
    print("1. Go to https://cloudinary.com/console")
    print("2. Log in with your account")
    print("3. Look for 'Cloud name' on the dashboard")
    print("4. It should be visible near your API credentials")
    
    return None

if __name__ == "__main__":
    test_cloudinary_credentials()
