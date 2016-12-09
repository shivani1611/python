*** Settings ***
Resource  po/landing_page.robot
Resource  po/top_nav.robot
Resource  po/search_results.robot
Resource  po/product.robot
Resource  po/cart.robot
Resource  po/signin.robot

*** Keywords ***
Begin Web Test
    Open Browser  about:blank  chrome

Search For Products
    Go To  http://www.amazon.com
    Wait Until Page Contains  Your Amazon.com
    Input Text  id=twotabsearchtextbox  Ferrari 458
    Click Button  xpath=//*[@id="nav-search"]/form/div[2]/div/input
    Wait Until Page Contains  "Ferrari 458"

Select Product From Search Results
    Click Link  css=#result_0 a.s-access-detail-page
    Wait Until Page Contains  Back to search results

Add Product To Cart
    Click Button  id=add-to-cart-button
    Wait Until Page Contains  Added to Cart

Begin Checkout
    Click Link  Proceed to checkout (1 item)
    Page Should Contain Element  ap_email

