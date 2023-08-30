#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value=value
  def get_value(self):
    return self._value
  def set_value(self, value):
    if(type(value)==str):
      self._value=value
    else:
      print('The value must be a string.')
  value=property(get_value, set_value)
  
  def is_sentence(self):
    return self.true_or_false('.')
  
  def is_question(self):
    return self.true_or_false('?')

  def is_exclamation(self):
    return self.true_or_false('!')

  def true_or_false(self, punctuation):
    if(self.value[len(self.value)-1]==punctuation):
      return True
    else: 
      return False
    
  def count_sentences(self):
    if(self.value!=''):
      count=self.value.count('. ')+self.value.count('! ')+self.value.count('? ')+1
    else:
      count = 0
    return count

new_sentence = MyString('Hello. My name is nicole! bye?')
new_sentence.count_sentences()