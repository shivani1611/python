*** Settings ***
Documentation  This is some basic info about the whole suite
Resource  ../resources/amazon.robot
Resource  ../resources/common.robot

Suite Setup  Insert Testing Data
Test Setup  common.Begin Web Test
Test Teardown  common.End Web Test
Suite Teardown  Cleanup Testing Data

*** Variables ***

*** Test Cases ***
Search For A Product
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    amazon.Search For Products

User Must Sign In To Check Out
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    amazon.Search For Products
    amazon.Select Product from Search Results
    amazon.Add Product To Cart
    amazon.Begin Checkout

