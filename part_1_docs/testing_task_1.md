### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      # should be '==' instead '='
      return True
    else
    # else need ':'
      return False
   

  dif highest_card(self, card1 card2):
    # 'def' is a right syntax for funtion
    # ','is missing between card1 and card2
  if card1.value > card2.value:
    return card
    # there is no argument of 'card'. it should be 'card1'
  else:
    return card2
  # whole of if blocks should be indented after function defined
  


def cards_total(self, cards):
  # the function need to be indented inside of class name on line 1
  total
  # total should be defined. As the function is for getting total number of cards, it should be interger which needs to be 0 before add any number
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # return should not be indented inside of for-loop since the function need to return total number which is adding from 0 where is out of for-loop
    # total is returning interger which is not possible to return with str. {total} needs to be in f"str".
  
```
