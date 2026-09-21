import sys

def test_python_version():
    major = sys.version_info.major
    minor = sys.version_info.minor
    
    # Print the version so it shows up in the GitHub Actions logs!
    print(f"\nRunning on Python {major}.{minor}")
    
    # Verify it's one of the versions in our matrix
    assert (major, minor) in [(3, 10), (3, 11), (3, 12)]