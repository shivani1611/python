from selenium import webdriver

driver = webdriver.Firefox( )

for i in range( 0, 100, 1 ):
  driver.get( "http://www.python.org" )
  driver.get( "http://www.google.com" )
  driver.get( "http://www.ebay.com" )
  driver.get( "http://www.oracle.com" )

driver.close( )
