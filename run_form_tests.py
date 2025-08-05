#!/usr/bin/env python
"""Simple test runner for CommentForm"""
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreflowepc.test_settings')
django.setup()

if __name__ == "__main__":
    # Import after Django setup
    from casestudy.test_forms import CommentFormTest
    import unittest
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(CommentFormTest)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\n=== TEST SUMMARY ===")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    # Exit with error code if tests failed
    sys.exit(0 if result.wasSuccessful() else 1)
