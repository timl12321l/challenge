This program uses Python 2.7

1. Open a terminal and type 'python --version' and verify if Python 2.7.x
2. Verify if an application called pip is installed by typing ' pip --version ', if not following instructions corresponding to your operating system https://www.makeuseof.com/tag/install-pip-for-python/
3. After pip is install, type ' pip install requests==2.7.0 ', you may need to prepend ' sudo ' if message shows access issue
4. Download files Page.py and APITest.py into the same directory
5. Type 'python APITest.py'
6. Verify test results in console.

The steps above will test for the following scenarios:

API testing
We will be leveraging NASA open API for the API test below.
• API that you will be testing: https://api.nasa.gov/planetary/apod
• Example of the actual good case use of the
api: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY (i.e. note that api_key query
parameters is required for a successful call)
• Please get the necessary API key for the test using https://api.nasa.gov/index.html#apply-for-an-
api-key
   
Tests to be performed:
Ensure that the API requires query parameter API_KEY
Ensure a 200 request status returns following fields in response "date", "copyright" 
Ensure response parameters url and hdurl DO NOT contain the same value
