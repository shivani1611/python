from random import randint
from time   import sleep

class Blackjack:

  my_deck          = ( [] )
  my_players_hand  = ( [] )
  my_dealers_hand  = ( [] )

  my_players_count = ( 0 )
  my_dealers_count = ( 0 )

  my_is_player_lose = ( False )
  my_is_player_tie  = ( False )

  def __init__( self, name, balance ):
    self.name    = ( name )
    self.balance = ( balance )
    return

  def reset_hands( self ):
    self.my_players_count = ( 0 )
    self.my_dealers_count = ( 0 )
    self.my_players_hand = []
    self.my_dealers_hand = []
    self.my_is_player_lose = ( False )
    self.my_is_player_tie = ( False )

  def reset_deck( self ):
    self.my_players_count = ( 0 )
    self.my_dealers_count = ( 0 )
    self.my_deck = []
    self.my_is_player_lose = ( False )
    self.my_is_player_tie = ( False )

  def initialize_deck( self ):
    self.reset_hands( )
    self.reset_deck( )

    # spades
    self.my_deck.append( 'AS' )
    self.my_deck.append( '2S' )
    self.my_deck.append( '3S' )
    self.my_deck.append( '4S' )
    self.my_deck.append( '5S' )
    self.my_deck.append( '6S' )
    self.my_deck.append( '7S' )
    self.my_deck.append( '8S' )
    self.my_deck.append( '9S' )
    self.my_deck.append( '10S' )
    self.my_deck.append( 'JS' )
    self.my_deck.append( 'QS' )
    self.my_deck.append( 'KS' )

    # hearts
    self.my_deck.append( 'AH' )
    self.my_deck.append( '2H' )
    self.my_deck.append( '3H' )
    self.my_deck.append( '4H' )
    self.my_deck.append( '5H' )
    self.my_deck.append( '6H' )
    self.my_deck.append( '7H' )
    self.my_deck.append( '8H' )
    self.my_deck.append( '9H' )
    self.my_deck.append( '10H' )
    self.my_deck.append( 'JH' )
    self.my_deck.append( 'QH' )
    self.my_deck.append( 'KH' )

    # clubs
    self.my_deck.append( 'AC' )
    self.my_deck.append( '2C' )
    self.my_deck.append( '3C' )
    self.my_deck.append( '4C' )
    self.my_deck.append( '5C' )
    self.my_deck.append( '6C' )
    self.my_deck.append( '7C' )
    self.my_deck.append( '8C' )
    self.my_deck.append( '9C' )
    self.my_deck.append( '10C' )
    self.my_deck.append( 'JC' )
    self.my_deck.append( 'QC' )
    self.my_deck.append( 'KC' )

    # diamonds
    self.my_deck.append( 'AD' )
    self.my_deck.append( '2D' )
    self.my_deck.append( '3D' )
    self.my_deck.append( '4D' )
    self.my_deck.append( '5D' )
    self.my_deck.append( '6D' )
    self.my_deck.append( '7D' )
    self.my_deck.append( '8D' )
    self.my_deck.append( '9D' )
    self.my_deck.append( '10D' )
    self.my_deck.append( 'JD' )
    self.my_deck.append( 'QD' )
    self.my_deck.append( 'KD' )
    return

  def shuffle_deck( self ):
    temp_deck = []
    used_elements = []

    try:
      for i in range( 0, len( self.my_deck ), 1 ):
        randnum = randint( 0, len( self.my_deck ) - 1 )
        while( randnum in used_elements ):
          randnum = randint( 0, len( self.my_deck ) - 1 )
        used_elements.append( randnum )
        temp_deck.append( self.my_deck[randnum] )
    except IndexError:
      print( "Error: Index out of bounds" )
      raise

    self.my_deck = ( temp_deck )
    return

  def renew_deck( self ):
    self.initialize_deck( )
    self.shuffle_deck( )
    return    

  def deck_card_count( self ):
    return( len( self.my_deck ) )

  def player_hand_card_count( self ):
    return( len( self.my_players_hand ) )

  def dealer_hand_card_count( self ):
    return( len( self.my_dealers_hand ) )

  def display_deck( self ):
    for i in range( 0, len( self.my_deck ), 1 ):
      print( self.my_deck[i] )
    return

  def display_balance( self ):
    return( self.balance )

  def display_players_hand( self ):
    for i in range( 0, len( self.my_players_hand ), 1 ):
      print( self.my_players_hand[i], sep = ( '' ), end = ( ' ' ) )
    self.calculate_hand( "human" ) 
    return

  def display_dealers_hand( self ):
    for i in range( 0, len( self.my_dealers_hand ), 1 ):
      if( ( self.my_is_player_lose == ( True ) ) or ( self.my_is_player_tie == ( True ) ) ):
         print( self.my_dealers_hand[i], sep = ( '' ), end = ( ' ' ) )
      elif( ( self.dealer_hand_card_count( ) <= ( 2 ) ) ): 
        if( i == ( 0 ) ):
          print( "**", sep = ( '' ), end = ( ' ' ) )
        else:
          print( self.my_dealers_hand[i], sep = ( '' ), end = ( ' ' ) )
      else:
        print( self.my_dealers_hand[i], sep = ( '' ), end = ( ' ' ) )
    print( )
    self.calculate_hand( "computer" )
    return

  def perform_action( self, who ):
    action = ( None )
    print( '\n' )

    if( who == ( "human" ) ):
      action = ( input( "(H)it or (S)tay: " ) )
      action = ( action.upper( ).strip( ) )
      while( ( action != ( 'H' ) ) and ( action != ( 'S' )  ) ):
        action = ( input( "(H)it or (S)tay: " ) )
        action = ( action.upper( ).strip( ) )
    elif( who == ( "computer" ) ):
      if( self.my_dealers_count < ( 17 ) ):
        action = ( 'H' )
      elif( self.my_dealers_count >= ( 17 ) ):
        action = ( 'S' )
      else:
        action = ( 'S' )
        raise ValueError( "Error: Incorrect count" )
    else:
      raise ValueError( "Error: Invalid player!" )

    return( action )

  def calculate_hand( self, who ):
    self.temp_deck  = ( None )
    self.temp_count = ( 0 )

    if( who == ( "human" ) ):
      self.temp_deck = ( self.my_players_hand )
    elif( who == ( "computer" ) ):
      self.temp_deck = ( self.my_dealers_hand )
    else:
      print( "Player: " + str( who ) )
      raise Exception( "Error: No such player!" )

    for i in range( 0, len( self.temp_deck ), 1 ):
      if( ( self.temp_deck[i] == ( "AS" ) )
         or ( self.temp_deck[i] == ( "AH" ) )
         or ( self.temp_deck[i] == ( "AC" ) )
         or ( self.temp_deck[i] == ( "AD" ) ) ):
        if( self.temp_count <= ( 10 ) ):
          self.temp_count += ( 11 )
        else:
          self.temp_count += ( 1 )
      elif( ( self.temp_deck[i] == ( "2S" ) )
         or ( self.temp_deck[i] == ( "2H" ) )
         or ( self.temp_deck[i] == ( "2C" ) )
         or ( self.temp_deck[i] == ( "2D" ) ) ):
          self.temp_count += ( 2 )
      elif( ( self.temp_deck[i] == ( "3S" ) )
         or ( self.temp_deck[i] == ( "3H" ) )
         or ( self.temp_deck[i] == ( "3C" ) )
         or ( self.temp_deck[i] == ( "3D" ) ) ):
          self.temp_count += ( 3 )
      elif( ( self.temp_deck[i] == ( "4S" ) )
         or ( self.temp_deck[i] == ( "4H" ) )
         or ( self.temp_deck[i] == ( "4C" ) )
         or ( self.temp_deck[i] == ( "4D" ) ) ):
          self.temp_count += ( 4 )
      elif( ( self.temp_deck[i] == ( "5S" ) )
         or ( self.temp_deck[i] == ( "5H" ) )
         or ( self.temp_deck[i] == ( "5C" ) )
         or ( self.temp_deck[i] == ( "5D" ) ) ):
          self.temp_count += ( 5 )
      elif( ( self.temp_deck[i] == ( "6S" ) )
         or ( self.temp_deck[i] == ( "6H" ) )
         or ( self.temp_deck[i] == ( "6C" ) )
         or ( self.temp_deck[i] == ( "6D" ) ) ):
          self.temp_count += ( 6 )
      elif( ( self.temp_deck[i] == ( "7S" ) )
         or ( self.temp_deck[i] == ( "7H" ) )
         or ( self.temp_deck[i] == ( "7C" ) )
         or ( self.temp_deck[i] == ( "7D" ) ) ):
          self.temp_count += ( 7 )
      elif( ( self.temp_deck[i] == ( "8S" ) )
         or ( self.temp_deck[i] == ( "8H" ) )
         or ( self.temp_deck[i] == ( "8C" ) )
         or ( self.temp_deck[i] == ( "8D" ) ) ):
          self.temp_count += ( 8 )
      elif( ( self.temp_deck[i] == ( "9S" ) )
         or ( self.temp_deck[i] == ( "9H" ) )
         or ( self.temp_deck[i] == ( "9C" ) )
         or ( self.temp_deck[i] == ( "9D" ) ) ):
          self.temp_count += ( 9 )
      elif( ( self.temp_deck[i] == ( "10S" ) )
         or ( self.temp_deck[i] == ( "10H" ) )
         or ( self.temp_deck[i] == ( "10C" ) )
         or ( self.temp_deck[i] == ( "10D" ) ) ):
          self.temp_count += ( 10 )
      elif( ( self.temp_deck[i] == ( "JS" ) )
         or ( self.temp_deck[i] == ( "JH" ) )
         or ( self.temp_deck[i] == ( "JC" ) )
         or ( self.temp_deck[i] == ( "JD" ) ) ):
          self.temp_count += ( 10 )
      elif( ( self.temp_deck[i] == ( "QS" ) )
         or ( self.temp_deck[i] == ( "QH" ) )
         or ( self.temp_deck[i] == ( "QC" ) )
         or ( self.temp_deck[i] == ( "QD" ) ) ):
          self.temp_count += ( 10 )
      elif( ( self.temp_deck[i] == ( "KS" ) )
         or ( self.temp_deck[i] == ( "KH" ) )
         or ( self.temp_deck[i] == ( "KC" ) )
         or ( self.temp_deck[i] == ( "KD" ) ) ):
          self.temp_count += ( 10 )

    if( who == ( "human" ) ):
      self.my_players_count = ( self.temp_count )
    elif( who == ( "computer" ) ):
      self.my_dealers_count = ( self.temp_count )
    else:
      raise Exception( "Error: Invalid player!" )
    return( self.temp_count )

  def deal_cards( self, who = "all", amount = ( 2 ) ):
    who = ( who.lower( ).strip( ) )

    if( who == ( "all" ) ):
      for i in range( 0, amount, 1 ):
        self.my_players_hand.append( self.my_deck.pop( ) )
        self.my_dealers_hand.append( self.my_deck.pop( ) )
    elif( who == ( "human" ) ):
      for i in range( 0, amount, 1 ):
        self.my_players_hand.append( self.my_deck.pop( ) )
    elif( who == ( "computer" ) ):
      for i in range( 0, amount, 1 ):
        self.my_dealers_hand.append( self.my_deck.pop( ) ) 
    else:
      raise Exception( "Invalid player!" )
    sleep( .3 )
    return







