from selenium.webdriver.common.keys import Keys
import selenium
import sys

def main( ):
  driver = ( selenium.webdriver.Firefox( ) )
  driver.get( "http://www.python.org" )

  assert "Python" in driver.title

  # link the element to the element on the page named "q"
  elem = driver.find_element_by_name( "q" )

  # clear the element since it is a text box
  elem.clear( )

  # write the following search in the text box"
  elem.send_keys( "pycon" )

  # press the enter key
  elem.send_keys( Keys.RETURN )

  # assert the results
  assert "No results found" not in driver.page_source

  # close the driver
  #driver.close( )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
