class Player:

  def play(self):
    print("The player is  playing cricket.")


#Define the deriver class Bataman
class Batsman(Player):

  def play(self):
    print("The batsman is batting.")


#Define the derived class Bowter
class Bowler(Player):

  def play(self):
    print("The bowler is bowling.")


#Create dbjocts of Bausnen and Doul
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()
