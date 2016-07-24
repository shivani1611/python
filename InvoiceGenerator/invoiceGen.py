#!/usr/bin/env python3

##############################################################################################
# Author: Armond Sarkisian
# Date  : 2016-07-11

##############################################################################################
from datetime import datetime
from decimal  import Decimal
import base64
import getpass
import os
import platform
import re
import sys
import time
import webbrowser

##############################################################################################
def businessName( ):
  return( "Your Business Name Here" )

##############################################################################################
def businessContactName( ):
  return( "John Smith" )

##############################################################################################
def businessStreet( ):
  return( "123 Main Street" )

##############################################################################################
def businessCity( ):
  return( "New York" )

##############################################################################################
def businessState( ):
  return( "NY" )

##############################################################################################
def businessZipCode( ):
  return( "10001" )

##############################################################################################
def businessCountry( ):
  return( "USA" )

##############################################################################################
def businessEmail( ):
  return( "your_email_address@domain.com" )

##############################################################################################
def businessPhoneNumber( ):
  return( "800-555-5555" )

##############################################################################################
def displayDate( ):
  print( "\nDate: {0}\n".format( str( getDateTime( ) )[0:10] ) )

##############################################################################################
def displayTitle( isDisplayAnimation ):

  tit = ( "\n\t\t{0} Invoice Generator\n\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n\n".format( businessName( ) ) )
  if( isDisplayAnimation == ( True ) ):
    for i in range( 0, len( tit ), 1 ):
      print( tit[i], flush = ( True ), sep = ( '' ), end = ( '' ) )
      time.sleep( 0.01 )
  else:
    print( tit )    
  return

##############################################################################################
def getDateTime( ):
  return( datetime.now( ) )

def isPlatformWindows( ):
  isWin = ( False )

  if( platform.system( ) == ( "Windows" ) ):
    isWin = ( True )
  return( isWin )

##############################################################################################
def clearScreen( ):
  WINDOWS_CLEAR = ( "cls" )
  UNIX_CLEAR    = ( "clear" )

  if( isPlatformWindows( ) ):
    os.system( WINDOWS_CLEAR )
  else:
    os.system( UNIX_CLEAR )
  return

##############################################################################################
def authenticate( ):
  dc_un = ( base64.b64decode( b"" ) )
  dc_pc = ( base64.b64decode( b"" ) )
  dc_un = ( str( dc_un.decode( "utf-8" ) ) )
  dc_pc = ( str( dc_pc.decode( "utf-8" ) ) )

  un = ( input( "Username: " ) )
  if( len( un ) > ( 50 ) ):
    print( "\n<ERROR: Username cannot exceed 50 characters!>" )
    exit( )

  pc = ( getpass.getpass( ) )
  if( len( pc ) > ( 50 ) ):
    print( "\n<ERROR: Password cannot exceed 50 characters!>" )
    exit( )

  if( ( un.lower( ) != ( dc_un.lower( ) ) ) or ( pc != ( dc_pc ) ) ):
    print( "\n<ERROR: Username and/or password incorrect. Unable to authenticate!>" )
    exit( )
  print( "\n  ==> Successfully logged in as user [\"{0}\"]\n".format( un.lower( ).capitalize( ) ) )
  return

##############################################################################################
def isValidEmail( emailStr ):
  isValid = ( False )

  if( re.match( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", emailStr ) ):
    isValid = ( True )
  return( isValid )	

##############################################################################################
def displayIntro( ):
  clearScreen( )
  displayDate( )
  displayTitle( True )

##############################################################################################
def displayOutro( ):
  clearScreen( )
  displayDate( )
  displayTitle( False )
  print( "Invoice generated successfully!\n\n  ==> Building invoice.", flush = ( True ), sep = ( '' ), end = ( '' ) )
  for i in range( 0, 12, 1 ):
    print( '.', flush = ( True ), end = ( '' ) )
    time.sleep( .5 )
  print( )

##############################################################################################
def getInput( ):
  counter          = ( 0 )
  choice           = ( "" )
  dscList          = ( [] )
  prList           = ( [] )

  choice = ( "" )
  while( choice != ( 'y' ) ):
    fn  = ( "" )
    while( ( not fn ) or ( len( fn ) < ( 2 ) ) or ( len( fn ) > ( 25 ) ) ):
      fn  = ( input( "\n[REQ] ** First Name:\t\t" ) )
      if( len( fn ) < ( 2 ) ):
        print( "\n<ERROR: First name cannot be less than 2 characters!>" )
      elif( len( fn ) > ( 25 ) ):
        print( "\n<ERROR: First name cannot exceed 25 characters!>" )
      fn = ( fn.lower( ).capitalize( ) )
    choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( fn ) ) )
    choice = ( choice.lower( ) )

  choice = ( "" )
  while( choice != ( 'y' ) ):
    mn  = ( input( "\n[OPT] Middle Name:\t\t" ) )
    if( mn ):
      if( len( mn ) > ( 25 ) ):
        print( "\n<ERROR: Middle name cannot exceed 25 characters!>" )
        mn = ( "" )
        choice = ( "" )
        continue
      mn = ( mn.lower( ).capitalize( ) )
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( mn ) ) )
      choice = ( choice.lower( ) )
    else:
      mn = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    ln  = ( "" )
    while( ( not ln ) or ( len( ln ) < ( 2 ) ) or ( len( ln ) > ( 25 ) ) ):
      ln  = ( input( "\n[REQ] ** Last Name:\t\t" ) )
      if( len( ln ) < ( 2 ) ):
        print( "\n<ERROR: Last name cannot be less than 2 characters!>" )
      elif( len( ln ) > ( 25 ) ):
        print( "\n<ERROR: Last name cannot exceed 25 characters!>" )
      ln = ( ln.lower( ).capitalize( ) )
    choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( ln ) ) )
    choice = ( choice.lower( ) )

  choice = ( "" )
  while( choice != ( 'y' ) ):
    sa  = ( input( "\n[OPT] Street Address:\t\t" ) )
    if( sa ):
      if( len( sa ) > ( 50 ) ):
        print( "\n<ERROR: Street address cannot exceed 50 characters!>" )
        sa = ( "" )
        choice = ( "" )
        continue
      sa = ( sa.lower( ).title( ) )
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( sa ) ) )
      choice = ( choice.lower( ) )
    else:
      sa = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    ci  = ( input( "\n[OPT] City:\t\t\t" ) )
    if( ci ):
      if( len( ci ) > ( 30 ) ):
        print( "\n<ERROR: City cannot exceed 30 characters!>" )
        ci = ( "" )
        choice = ( "" )
        continue
      ci = ( ci.lower( ).title( ) )
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( ci ) ) )
      choice = ( choice.lower( ) )
    else:
      ci = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    st  = ( input( "\n[OPT] State:\t\t\t" ) )
    if( st ):
      if( len( st ) > ( 15 ) ):
        print( "\n<ERROR: State cannot exceed 15 characters!>" )
        st = ( "" )
        choice = ( "" )
        continue
      st = ( st.upper( ) )
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( st ) ) )
      choice = ( choice.lower( ) )
    else:
      st = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    zc  = ( input( "\n[OPT] Zip Code:\t\t\t" ) )
    if( zc ):
      if( len( zc ) < ( 4 ) ):
        print( "\n<ERROR: Zip code cannot be less than 4 characters!>" )
        zc = ( "" )
        choice = ( "" )
        continue
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( zc ) ) )
      choice = ( choice.lower( ) )
    else:
      zc = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    co  = ( input( "\n[OPT] Country:\t\t\t" ) )
    if( co ):
      if( len( co ) > ( 25 ) ):
        print( "\n<ERROR: Country cannot exceed 25 characters!>" )
        co = ( "" )
        choice = ( "" )
        continue
      co = ( co.upper( ) )
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( co ) ) )
      choice = ( choice.lower( ) )
    else:
      co = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    op  = ( input( "\n[OPT] Office Phone:\t\t" ) )
    if( op ):
      if( len( op ) > ( 35 ) ):
        print( "\n<ERROR: Office phone cannot exceed 35 characters!>" )
        op = ( "" )
        choice = ( "" )
        continue
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( op ) ) )
      choice = ( choice.lower( ) )
    else:
      op = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    hp  = ( input( "\n[OPT] Home Phone:\t\t" ) )
    if( hp ):
      if( len( hp ) > ( 35 ) ):
        print( "\n<ERROR: Home phone cannot exceed 35 characters!>" )
        hp = ( "" )
        choice = ( "" )
        continue
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( hp ) ) )
      choice = ( choice.lower( ) )
    else:
      hp = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    mp  = ( input( "\n[OPT] Mobile Phone:\t\t" ) )
    if( mp ):
      if( len( mp ) > ( 35 ) ):
        print( "\n<ERROR: Mobile phone cannot exceed 35 characters!>" )
        mp = ( "" )
        choice = ( "" )
        continue
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( mp ) ) )
      choice = ( choice.lower( ) )
    else:
      mp = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    ap  = ( input( "\n[OPT] Alternative Phone:\t" ) )
    if( ap ):
      if( len( ap ) > ( 35 ) ):
        print( "\n<ERROR: Alternative phone cannot exceed 35 characters!>" )
        ap = ( "" )
        choice = ( "" )
        continue
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( ap ) ) )
      choice = ( choice.lower( ) )
    else:
      ap = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    em  = ( input( "\n[OPT] Email Address:\t\t" ) )
    if( em ):
      if( len( em ) > ( 50 ) ):
        print( "\n<ERROR: Email address cannot exceed 50 characters!>" )
        em = ( "" )
        choice = ( "" )
        continue
      if( isValidEmail( em ) == ( False ) ):
        print( "\n<ERROR: Invalid email address!>" )
        choice = ( "" )
        continue	  
      em = ( em.lower( ) )
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( em ) ) )
      choice = ( choice.lower( ) )
    else:
      em = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    cl  = ( input( "\n[OPT] Claim #:\t\t\t" ) )
    if( cl ):
      if( len( cl ) > ( 35 ) ):
        print( "\n<ERROR: Claim # cannot exceed 35 characters!>" )
        cl = ( "" )
        choice = ( "" )
        continue
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( cl ) ) )
      choice = ( choice.lower( ) )
    else:
      cl = ( "" )
      break

  choice = ( "" )
  while( choice != ( 'y' ) ):
    no  = ( input( "\n[OPT] Important Notes:\t\t" ) )
    if( no ):
      if( len( no ) > ( 2500 ) ):
        print( "\n<ERROR: Important notes cannot exceed 2500 characters!>" )
        no = ( "" )
        choice = ( "" )
        continue
      no = ( no.capitalize( ) )
      choice = ( input( "\n[ \"{0}\" ]\n  ==> Correct? (y/n): ".format( no ) ) )
      choice = ( choice.lower( ) )
    else:
      no = ( "" )
      break
  
  while( True ):
    counter += ( 1 )
	
    if( counter == ( 1 ) ):
      dsc = ( "" )
      while( ( not dsc ) ):
        dsc  = ( input( "\n[REQ] ** Service # {0} Description:\t".format( ( counter ) ) ) )
        if( len( dsc ) > ( 75 ) ):
          print( "\n<ERROR: Description cannot exceed 75 characters!>" )
          dsc = ( "" )
          continue
        elif( len( dsc ) < ( 3 ) ):
          print( "\n<ERROR: Description cannot be less than 3 characters!>" )
          dsc = ( "" )
          continue
    else:
      dsc  = ( input( "\n[OPT] Service # {0} Description:\t\t".format( ( counter ) ) ) )
      if( len( dsc ) > ( 75 ) ):
        print( "\n<ERROR: Description cannot exceed 75 characters!>" )
        dsc = ( "" )
        continue

    if( not dsc ):
      break

    dsc = ( dsc.title( ) )

    pr = ( "" )
    while( not pr ):
      isPriceAlphaChar = ( False )
      pr = ( input( "\n[REQ] ** Service # {0} Price:\t\t".format( ( counter ) ) ) )
      if( not pr ):
        print( "\n<ERROR: Price must be supplied!>" )
        pr = ( "" )
        continue
      for i in range( 0, len( pr ), 1 ):
        if( not pr[i] == '1' and not pr[i] == '2' and not pr[i] == '3' and not pr[i] == '4' and not pr[i] == '5' and not pr[i] == '6' and not pr[i] == '7' and not pr[i] == '8' and not pr[i] == '9' and not pr[i] == '0' and not pr[i] == '.' ):
          isPriceAlphaChar = ( True )
      if( isPriceAlphaChar == ( True ) ):
        print( "\n<ERROR: Price must only contain numbers!>" )
        pr = ( "" )
        continue
      else:
        pr = ( Decimal( pr ) )
        break

    if( ( dsc ) and ( pr ) ):
      dscList.append( dsc )
      prList.append( pr )
  return( fn, mn, ln, sa, ci, st, zc, co, op, hp, mp, ap, no, em, cl, dscList, prList )

##############################################################################################
def calculateTax( TAX, prList ):
  totalSalesTax = ( Decimal( 0.0 ) )

  for i in range( 0, len( prList ), 1 ):
    totalSalesTax += ( Decimal( Decimal( prList[i] ) * ( Decimal( TAX ) ) ) )
  return( totalSalesTax )

##############################################################################################
def calculateSubTotal( prList ):
  # variables
  subTotal = ( Decimal( 0.0 ) )

  for i in range( 0, len( prList ), 1 ):
    subTotal += ( Decimal( prList[i] ) )
  return( subTotal )

##############################################################################################
def calculateTotalPrice( totalSalesTax, subTotal ):
  return( Decimal( Decimal( totalSalesTax ) + ( Decimal( subTotal ) ) ) )

##############################################################################################
def outputToFile( outputStr, fn, ln ):
  fileName = ( "{0}-{1}.html".format( ( str( getDateTime( ) )[0:10] ), str( ln ) ) )
  try:
    with open( fileName, 'w' ) as fout:
      fout.write( outputStr )
  except IOError as e:
    print( "<ERROR: I/O {0}: {1}>!".format( e.errno, e.strerror ) )
  return( fileName )

##############################################################################################
def getWorkingDirectory( htmlFile ):
  workingDirectory = ( os.getcwd( ) )
  
  if( isPlatformWindows( ) ):
    fullPath = ( "{0}\\{1}".format( str( workingDirectory ), str( htmlFile ) ) )
  else:
    fullPath = ( "file://{0}/{1}".format( str( workingDirectory ), str( htmlFile ) ) )
  return( fullPath )

##############################################################################################
def openInvoice( url ):
  print( "\nInvoice Path:", url )
  if( isPlatformWindows == ( True ) ):
    webbrowser.open_new( url )
  else:
    if( "suse" in str( platform.linux_distribution( )[0] ).lower( ) ):
      webbrowser.get( 'firefox' ).open_new( url )
  print( "\nGoodbye!\n" )
  return

##############################################################################################
def generateHTML( TAX, totalSalesTax, subTotal, totalPrice, fn, mn, ln, sa, ci, st, zc, co, op, hp, mp, ap, no, em, cl, dscList, prList ):
  # generate HTML
  html_message =  ( " <!DOCTYPE html>\n " )
  html_message += ( " <html>\n " )
  html_message += ( " <head>\n " )

  html_message += ( " <style>\n" )
  html_message += ( " html *{ font-size: 1em !important; color: #000 !important; font-family: Arial !important; }\n " )
  html_message += ( " .page { font-size:12pt; height:900px; page-break-after:always; page-break-inside:avoid;}\n " )
  html_message += ( " table { table-layout: fixed; }\n " )
  html_message += ( " table a:link { color: #666; font-weight: bold; text-decoration:none;}\n " )
  html_message += ( " table a:visited { color: #999999; font-weight:bold; text-decoration:none;}\n " )
  html_message += ( " table a:active, table a:hover { color: #bd5a35; text-decoration:underline; }\n " )
  html_message += ( " table {font-family:Arial, Helvetica, sans-serif; color:#666; font-size:12px; text-shadow: 1px 1px 0px #fff; background:#eaebec; margin:20px; border:#ccc 1px solid; -moz-border-radius:3px; -webkit-border-radius:3px; border-radius:3px; -moz-box-shadow: 0 1px 2px #d1d1d1; -webkit-box-shadow: 0 1px 2px #d1d1d1; box-shadow: 0 1px 2px #d1d1d1;}\n " )
  html_message += ( " table th { padding:5px 5px 5px 5px; border-top:1px solid #fafafa; border-bottom:1px solid #e0e0e0; background: #ededed; background: -webkit-gradient(linear, left top, left bottom, from(#ededed), to(#ebebeb)); background: -moz-linear-gradient(top,  #ededed,  #ebebeb);}\n " )
  html_message += ( " table th:first-child { text-align: center; padding-left:5px;}\n " )
  html_message += ( " table tr:first-child th:first-child { -moz-border-radius-topleft:3px; -webkit-border-top-left-radius:3px; border-top-left-radius:3px;}\n " )
  html_message += ( " table tr:first-child th:last-child { -moz-border-radius-topright:3px; -webkit-border-top-right-radius:3px; border-top-right-radius:3px;}\n " )
  html_message += ( " table tr { text-align: left; padding-left:5px;}\n " )
  html_message += ( " table td:first-child { text-align: left; padding-left:5px; border-left: 0;}\n " )
  html_message += ( " table td { padding:5px; border-top: 1px solid #ffffff; border-bottom:1px solid #e0e0e0; border-left: 1px solid #e0e0e0; background: #fafafa; background: -webkit-gradient(linear, left top, left bottom, from(#fbfbfb), to(#fafafa)); background: -moz-linear-gradient(top,  #fbfbfb,  #fafafa);}\n " )
  html_message += ( " table td { overflow: hidden; }\n " ) 
  html_message += ( " table tr.even td { background: #f6f6f6; background: -webkit-gradient(linear, left top, left bottom, from(#f8f8f8), to(#f6f6f6)); background: -moz-linear-gradient(top,  #f8f8f8,  #f6f6f6);}\n " )
  html_message += ( " table tr:last-child td { border-bottom:0;}\n " )
  html_message += ( " table tr:last-child td:first-child { -moz-border-radius-bottomleft:3px; -webkit-border-bottom-left-radius:3px; border-bottom-left-radius:3px;}\n " )
  html_message += ( " table tr:last-child td:last-child { -moz-border-radius-bottomright:3px; -webkit-border-bottom-right-radius:3px; border-bottom-right-radius:3px;}\n " )
  html_message += ( " table tr:hover td { background: #f2f2f2; background: -webkit-gradient(linear, left top, left bottom, from(#f2f2f2), to(#f0f0f0)); background: -moz-linear-gradient(top,  #f2f2f2,  #f0f0f0);}\n " )
  html_message += ( " </style>\n " )

  html_message += ( " <title>\n " )
  html_message += ( "{0} Invoice".format( businessName( ) ) )
  html_message += ( " </title>\n " )
  html_message += ( " </head>\n " )
  html_message += ( " <body>\n " )
  html_message += ( " <div class=\"page\">\n " )
  
  html_message += ( " <table width=\"900\" align=\"center\">\n " )

  html_message += ( " <tr align=\"center\">\n " )
  html_message += ( " <th align=\"center\">\n " )
  html_message += ( "" )
  html_message += ( " </th>\n " )
  html_message += ( " <th align=\"right\">\n " )
  html_message += ( "SERVICE INVOICE" )
  html_message += ( " </th>\n " )
  html_message += ( " </tr>\n " )
  html_message += ( " <tr>\n " )
  html_message += ( " <td>\n " )
  sellerInformation = ( "" )  
  if( businessContactName( ) ):
    sellerInformation += ( businessContactName( ) + " <br>\n " )
  if( businessStreet( ) ):
    sellerInformation += ( businessStreet( ) + " <br>\n " )
  if( businessCity( ) ):
    sellerInformation += ( businessCity( ) + ", " )
  if( businessState( ) ):
    sellerInformation += ( businessState( ) + " <br>\n " )
  if( businessZipCode( ) ):
    sellerInformation += ( businessZipCode( ) + " <br>\n " )
  if( businessCountry( ) ):
    sellerInformation += ( businessCountry( ) + " <br>\n " )
  if( businessPhoneNumber( ) ):  
    sellerInformation += ( businessPhoneNumber( ) + " <br>\n " )
  if( businessEmail( ) ):
    sellerInformation += ( businessEmail( ) + " <br>\n " )
  
  html_message += ( " <table width=\"300\" >\n " )  
  html_message += ( " <tr>\n " )
  html_message += ( " <th>\n " )
  html_message += ( businessName( ).upper( ) )
  html_message += ( " </th>\n " )
  html_message += ( " </tr>\n " )
  html_message += ( " <tr>\n " )
  html_message += ( " <td>\n " )
  html_message += ( sellerInformation )
  html_message += ( " </td>\n " )
  html_message += ( " </tr>\n " )
  html_message += ( " </table>\n " )
  
  html_message += ( " </td>\n " )
  html_message += ( " <td>\n " )
  buyerInformation = ( "" )
  if( fn ):
    buyerInformation += ( fn + ' ' )
  if( mn ):
    buyerInformation += ( mn + ' ' )
  if( ln ):
    buyerInformation += ( ln + " <br>\n " )
  if( sa ):
    buyerInformation += ( sa + " <br>\n " )
  if( ci ):
    buyerInformation += ( ci + ", " )
  if( st ):
    buyerInformation += ( st + " <br>\n " )
  if( zc ):
    buyerInformation += ( zc + " <br>\n " )
  if( co ):
    buyerInformation += ( co + " <br>\n " )
  if( em ):
    buyerInformation += ( em + " <br>\n " )
  if( op ):
    buyerInformation += ( "Office: " + op + " <br>\n " )
  if( hp ):
    buyerInformation += ( "Home: " + hp + " <br>\n " )
  if( mp ):
    buyerInformation += ( "Mobile: " + mp + " <br>\n " )
  if( ap ):
    buyerInformation += ( "Alternate: " + ap + " <br>\n " )

  html_message += ( " <table width=\"300\" >\n " )
  html_message += ( " <tr>\n " )
  html_message += ( " <th align=\"center\">\n " )
  html_message += ( "CUSTOMER" )
  html_message += ( " </th>\n " )
  html_message += ( " </tr>\n " )
  html_message += ( " <tr>\n " )
  html_message += ( " <td>\n " )
  html_message += ( buyerInformation )

  if( cl ):
    html_message += ( " <br>\n " )
    html_message += ( " <b>\n Claim #: </b>\n {0}".format( str( cl ) ) )

  html_message += ( " </td>\n " )
  html_message += ( " </tr>\n " )
  html_message += ( " </table>\n " )
  
  html_message += ( " </td>\n " )
  html_message += ( " </tr>\n " )
  html_message += ( " <tr>\n " )  
  html_message += ( " <td>\n " )
  html_message += ( " <table width=\"300\" >\n " )  
  html_message += ( " <tr>\n " )
  html_message += ( " <th align=\"center\">\n " )
  html_message += ( "DESCRIPTION" )
  html_message += ( " </th>\n " )
  html_message += ( " <th align=\"center\">\n " )
  html_message += ( "PRICE" )
  html_message += ( " </th>\n " )
  html_message += ( " </tr>\n " )

  for i in range( 0, len( dscList ), 1 ):
    html_message += ( " <tr>\n " )
    html_message += ( " <td>\n " )
    html_message += ( dscList[i] )
    html_message += ( " </td>\n " )
    html_message += ( " <td>\n " )
    html_message += ( " <b>\n " )
    html_message += ( str( prList[i] ) )
    html_message += ( " </b>\n " )
    html_message += ( " </td>\n " )
    html_message += ( " </tr>\n " )

  html_message += ( " </table>\n " )
  html_message += ( " <br>\n " )
  if( no ):
    html_message += ( " <b>\n Special Notes: </b>\n {0}".format( no ) )
  else:
    html_message += ( "Special Notes: None Provided" )
  html_message += ( " <br>\n " )
  
  html_message += ( " </td>\n " )
  html_message += ( " <td>\n " )
  
  html_message += ( " <table width=\"300\" >\n " )  
  html_message += ( " <tr>\n " )
  html_message += ( " <td>\n " )
  html_message += ( "Sub Total" )
  html_message += ( " </td>\n " )
  html_message += ( " <td>\n " )
  html_message += ( " <b>\n " )
  html_message += ( str( "$%.2f" % ( subTotal ) ) )
  html_message += ( " </b>\n " )
  html_message += ( " </td>\n " )
  html_message += ( " </tr>\n " )
  html_message += ( " <tr>\n " )
  html_message += ( " <td>\n " )
  html_message += ( "Tax" )
  html_message += ( " </td>\n " )
  html_message += ( " <td>\n " )
  html_message += ( " <b>\n " )
  html_message += ( str( "%.2f%%" % ( TAX ) ) )
  html_message += ( " </b>\n " )
  html_message += ( " </td>\n " )
  html_message += ( " </tr>\n " )
  html_message += ( " <tr>\n " )
  html_message += ( " <td>\n " )
  html_message += ( "Total Price" )
  html_message += ( " </td>\n " )
  html_message += ( " <td>\n " )
  html_message += ( " <b>\n " )
  html_message += ( str( "$%.2f" % ( totalPrice ) ) )
  html_message += ( " </b>\n " )
  html_message += ( " </td>\n " )
  html_message += ( " </tr>\n " )
  html_message += ( " </table>\n " )  
  
  html_message += ( " </td>\n " )
  html_message += ( " </tr>\n " )
  html_message += ( " <tr>\n " )
  html_message += ( " <td align=\"center\">\n " )
  html_message += ( " <br>\n " )
  html_message += ( " <br>\n " )
  html_message += ( " <br>\n " )
  html_message += ( "SIGN: [___________________________________]" )  
  html_message += ( " <br>\n " )
  html_message += ( " <br>\n " )
  html_message += ( " <br>\n " )
  html_message += ( " </td>\n " )
  html_message += ( " <td align=\"center\">\n " )
  html_message += ( "DATE: <b>\n {0} </b>\n ".format( str( getDateTime( ) )[0:16] ) )  
  html_message += ( " </td>\n " )
  html_message += ( " </tr>\n " )
  html_message += ( " </table>\n " )

  html_message += ( " <table width=\"900\" align=\"center\">\n " )
  html_message += ( " <th align=\"center\">\n " )
  html_message += ( "Thank you for shopping at <u> {0} </u>. Your business is appreciated!".format( businessName( ) ) )
  html_message += ( " </th>\n " )
  #html_message += ( " <tr align=\"center\">\n " )
  #html_message += ( " <td align=\"center\">\n " )
  #html_message += ( " </td>\n " )
  #html_message += ( " </tr>\n " )
  html_message += ( " </table>\n " )  

  html_message += ( " </div>\n " )
  html_message += ( " </body>\n " )
  html_message += ( " </html>\n " )
  return( html_message )

##############################################################################################
def main( ):
  # constant(s)
  TAX              = ( Decimal( 0.09 ) )

  # variable(s)
  totalSalesTax    = ( Decimal( 0.0 ) )
  subTotal         = ( Decimal( 0.0 ) )
  totalPrice       = ( Decimal( 0.0 ) )

  # routine(s)
  displayIntro( )

  #authenticate( )

  fn, mn, ln, sa, ci, st, zc, co, op, hp, mp, ap, no, em, cl, dscList, prList = getInput( )  

  totalSalesTax    = ( calculateTax( TAX, prList ) )
  subTotal         = ( calculateSubTotal( prList ) )
  totalPrice       = ( calculateTotalPrice( totalSalesTax, subTotal ) )

  html_message = ( generateHTML( TAX, totalSalesTax, subTotal, totalPrice, fn, mn, ln, sa, ci, st, zc, co, op, hp, mp, ap, no, em, cl, dscList, prList ) )  
  htmlFile = ( outputToFile( html_message, fn, ln ) )

  url = ( str( getWorkingDirectory( htmlFile ) ) )

  displayOutro( )

  openInvoice( url )

  wait = ( input( "Press a key to exit..\n" ) )
  return

##############################################################################################
if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
