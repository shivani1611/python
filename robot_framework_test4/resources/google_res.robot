*** Settings ***
Library  Selenium2Library

*** Variables ***


*** Keywords ***
Access Google
    [Arguments]  ${URL}  ${BROWSER}
    Open Browser  ${URL}  ${BROWSER}


Place A Search
    [Arguments]  ${SEARCH_TERM}
    Log  Placing Search
