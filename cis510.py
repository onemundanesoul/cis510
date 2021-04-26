
def remove_list_item(*, the_list, the_item):
  #the_list because list is a Python function
  '''
  Use three apostrophes to mark off larger comments.
  '''
  new_list = [item for item in the_list if item != the_item]
  return new_list
