*** Settings ***
Library  Selenium2Library

*** Keywords ***
Begin Web Test
    Open Browser  about:blank  chrome

End Web Test
    Close Browser

Insert Testing Data
    Log  I am setting up the test data...

Cleanup Testing Data
    Log  I am cleaning up the test data...
