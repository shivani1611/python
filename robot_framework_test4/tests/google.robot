*** Settings ***
Documentation  Search For Something In Google
Library  Selenium2Library
Resource  ../resources/google_res.robot

*** Variables ***
${URL} =  http://www.google.com
${BROWSER} =  chrome
${SEARCH_TERM} =  "Ferrari 458"

*** Test Cases ***
TC: Search For Something
    Access Google  ${URL}  ${BROWSER}
    Place A Search  ${SEARCH_TERM}
    Close Browser

*** Keywords ***

