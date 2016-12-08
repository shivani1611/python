*** Settings ***
Documentation  This is some basic info about the whole suite
Library  Selenium2Library

*** Variables ***


*** Test Cases ***
Should be able to search for product
    Open Browser  http://www.amazon.com  chrome
    Sleep  3s
    Input Text  id=twotabsearchtextbox  Ferrari 458
    Sleep  3s
    Click Button  css=#nav-search > form > div.nav-right > div > input
    Close Browser

*** Keywords ***
