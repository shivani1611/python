from Blackjack import Blackjack
from os        import system
from time      import sleep

class Game:
  def __init__( self ):
    pass

  def clear_screen( self ):
    system( "clear" )

  def display_title( self ):
    print( "Supreme Blackjack by Armond" )
    print( "---------------------------\n" )

  def display_table( self, bj ):
    print( "Player: ", sep = ( ' ' ), end = ( '' ) )
    bj.display_players_hand( )

    print( "\n\nDealer: ", sep = ( ' ' ), end = ( '' ) )
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
      winner = ( "human" )
    elif( dealer_count == ( 21 )
    and player_count != ( 21 ) ):
      winner = ( "computer" )
    elif( dealer_count == ( 21 ) and player_count == ( 21 ) ):
      winner = ( "tie" )
    elif( player_count > ( 21 )
    and dealer_count < ( 21 ) ):
      winner = ( "computer" )
    elif( dealer_count > ( 21 )
    and player_count < ( 21 ) ):
      winner = ( "human" )
    elif( player_count > ( dealer_count ) ):
      winner = ( "human" )
    elif( player_count < ( dealer_count ) ):
      winner = ( "computer" )
    elif( player_count == ( dealer_count ) ):
      winner = ( "tie" )
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

      self.amount = ( input( "\nHow much would you like to wager? 0 to exit: " ) )

      while( not self.amount.isdigit( ) ):
        self.amount = ( input( "\nHow much would you like to wager? 0 to exit: " ) )

      self.amount = ( int( self.amount ) )

      if( self.amount <= ( 0.0 ) ):
        is_play_again = ( False )
        break

      if( self.amount > ( bj.balance ) ):
        print( "Cannot wager beyond your available balance!" )
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
      if( winner == ( "human" ) ):
        print( "\nCongratulations. You won ${0}!".format( str( self.amount ) ) )
        bj.balance += ( self.amount * ( 2 ) )
      elif( winner == ( "computer" ) ):
        print( "\nSorry, you lose!" )
      elif( winner == ( "tie" ) ):
        print( "Tie game!" )
        bj.balance += ( self.amount )
      else:
        raise Exception( "Error: Invalid winning scenario!" )
      print( )

      sleep( 3 )

    print( "\nFinal Player Balance: ${0:.2f}\n".format( bj.balance ) )

    return
