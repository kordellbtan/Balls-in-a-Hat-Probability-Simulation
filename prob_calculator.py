import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self,**kwargs):
    # Create list of physical ball identities
    self.contents = list()
    for ball,count in kwargs.items():
      for i in range(count):
        self.contents.append(ball)
    #print(self.contents)

  def draw(self,num_draws):
    ball_drawn = []
    backup_hat = copy.deepcopy(self.contents)
    for d in range(num_draws):
      try:
        drawn = random.choice(self.contents)
        print('Drew a',drawn,'ball.')
        ball_drawn.append(drawn)
        del self.contents[self.contents.index(drawn)]
      except:
        self.contents = copy.copy(backup_hat)
        drawn = random.choice(self.contents)
        print('Drew a',drawn,'ball.')
        ball_drawn.append(drawn)
        del self.contents[self.contents.index(drawn)]
    return ball_drawn
  

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  # Save a copy of the hat contents to rerun experiment
  hat_test = copy.copy(hat)

  test = tuple()
  for balls,count in expected_balls.items():
    test += balls,count
  
  unique_balls = int(len(test)/2)
  passed_exp = 0

  for draws in range(num_experiments):
    print('New Experiment')
    hat = copy.deepcopy(hat_test)
    exp = hat.draw(num_balls_drawn)
    print('Results',exp)

    error = unique_balls
    for b in range(unique_balls):
      b *= 2
      ball_exp = test[b]
      count_exp = test[b+1]

      for i in range(count_exp):
        print('Unique Balls:',unique_balls)
        print(ball_exp,count_exp)
        if ball_exp in exp:
          del exp[exp.index(ball_exp)]
          print('Removing',ball_exp)
          print(exp)
        else:
          print('None left')
          error += 1

    if error == unique_balls:
      passed_exp += 1
    print('Successful Tests:',passed_exp)

        
      
      


  return passed_exp/num_experiments
