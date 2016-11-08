from Blackjack import Blackjack
from os        import system
from time      import sleep
from re        import match

class Game:
  def __init__( self ):
    pass

  def clear_screen( self ):
    system( "clear" )

  def display_title( self ):
    print( )
    print( "Supreme Blackjack by Armond" )
    print( "---------------------------\n" )

  def display_table( self, bj ):
    print( "Player Balance: ${0:.2f}".format( float( bj.display_balance( ) ) ) )
    print( "Player Hand: ", sep = ( ' ' ), end = ( '' ) )
    bj.display_players_hand( )

    print( "\n\nDealer Hand: ", sep = ( ' ' ), end = ( '' ) )
    bj.display_dealers_hand( )
   
  def refresh_screen( self, bj ):
    self.clear_screen( )
    self.display_title( )
    self.display_table( bj )

  def determine_winner( self, bj ):
    winner = ( None )

    player_count = ( bj.calculate_hand( "human" ) )
    dealer_count = ( bj.calculate_hand( "computer" ) )

    if( player_count == ( 21 ) 
    and dealer_count != ( 21 ) ):
      self.winner = ( "human" )
    elif( dealer_count == ( 21 )
    and player_count != ( 21 ) ):
      self.winner = ( "computer" )
    elif( dealer_count == ( 21 ) and player_count == ( 21 ) ):
      self.winner = ( "tie" )
    elif( player_count > ( 21 )
    and dealer_count < ( 21 ) ):
      self.winner = ( "computer" )
    elif( dealer_count > ( 21 )
    and player_count < ( 21 ) ):
      self.winner = ( "human" )
    elif( player_count > ( dealer_count ) ):
      self.winner = ( "human" )
    elif( player_count < ( dealer_count ) ):
      self.winner = ( "computer" )
    elif( player_count == ( dealer_count ) ):
      self.winner = ( "tie" )
    else:
      raise Exception( "Error: Invalid card count!" )
    return( winner )

  def start( self ):
    bj = ( Blackjack( "armond", 500.00 ) )

    bj.renew_deck( )
    is_play_again = ( True )
    amount = ( 0 )

    while( is_play_again == ( True ) ):
      self.refresh_screen( bj )
      self.is_play_again = ( True )

      if( bj.balance < ( 5 ) ):
        print( "\nNo more funds. Thanks for playing!" )
        is_play_again = ( False )
        break

      self.amount = ( input( "\n\nWager Amount? (0 to quit): $" ) )
      self.amount = ( self.amount.strip( ) )

      while( match( "^([0-9]{1,5})(\.{0,1})([0-9]{0,2})$", str( self.amount ) ) == ( None ) ):
        self.amount = ( input( "\nWager Amount? (0 to quit): $" ) )
        self.amount = ( self.amount.strip( ) )

      self.amount = ( float( self.amount ) )

      if( self.amount <= ( 0.0 ) ):
        is_play_again = ( False )
        break

      if( self.amount > ( bj.balance ) ):
        print( "\nCannot wager beyond your available balance!" )
        sleep( 2 )
        continue

      bj.balance -= ( self.amount )

      self.refresh_screen( bj )
 
      if( bj.deck_card_count( ) <= ( 12 ) ):
        bj.renew_deck( )

      bj.reset_hands( )

      bj.deal_cards( who = "all", amount = 2 )

      is_done = ( False )
      while( is_done == ( False ) ): 
        self.refresh_screen( bj )
        action = ( bj.perform_action( who = ( "human" ) ) )
        if( action == ( 'S' ) ):
          is_done = ( True )
          break
        elif( action == ( 'H' ) ):
          bj.deal_cards( who = ( "human" ), amount = ( 1 ) )
          count = ( bj.calculate_hand( "human" ) )
          if( count > ( 21 ) ):
            action = ( 'S' )
            is_done = ( True )
            break

      self.refresh_screen( bj )

      if( bj.calculate_hand( "human" ) <= ( 21 ) ):
        is_done = ( False )
        while( is_done == ( False ) ): 
          self.refresh_screen( bj )
          action = ( bj.perform_action( who = ( "computer" ) ) )
          if( action == ( 'S' ) ):
            is_done = ( True )
            break
          elif( action == ( 'H' ) ):
            bj.deal_cards( who = ( "computer" ), amount = ( 1 ) )
            count = ( bj.calculate_hand( "computer" ) )
            if( count > ( 21 ) ):
              action = ( 'S' )
              is_done = ( True )
              break
  
      self.refresh_screen( bj )

      winner = ( self.determine_winner( bj ) )

      print( )
      if( self.winner == ( "human" ) ):
        print( "\nCongratulations. You won ${0:.2f}!".format( self.amount ) )
        bj.balance += ( self.amount * ( 2 ) )
        bj.my_is_player_lose = ( False )
        bj.my_is_player_tie = ( False )
      elif( self.winner == ( "computer" ) ):
        print( "\nSorry, you lose!" )
        bj.my_is_player_lose = ( True )
        bj.my_is_player_tie = ( False )
      elif( self.winner == ( "tie" ) ):
        print( "Tie game!" )
        bj.balance += ( self.amount )
        bj.my_is_player_tie = ( True )
        bj.my_is_player_lose = ( False )
      else:
        raise Exception( "Error: Invalid winning scenario!" )
      print( )

      sleep( 3 )

      self.refresh_screen( bj )

    print( "\nFinal Player Balance: ${0:.2f}\n".format( bj.balance ) )

    return
