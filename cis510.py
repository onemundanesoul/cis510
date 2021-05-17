import pandas as pd

def remove_list_item(*, the_list, the_item):
  #the_list because list is a Python function
  '''
  Use three apostrophes to mark off larger comments.
  '''
  new_list = [item for item in the_list if item != the_item]
  return new_list

def plot_x_by_class_y(*, table, x_column, y_column):
  assert isinstance(table, pd.core.frame.DataFrame), f'table is not a dataframe but instead a {type(table)}'
  assert x_column in table.columns, f'unrecognized column: {x_column}. Check spelling and case.'
  assert y_column in table.columns, f'unrecognized column: {y_column}. Check spelling and case.'
  assert table[y_column].nunique()<=5, f'y_column must be of 5 categories or less but has {table[y_column].nunique()}'

  pd.crosstab(table[x_column], table[y_column]).plot(kind='bar', figsize=(15,8), grid=True, logy=True)
  return None

def mcc(*, tp, fp, tn, fn):
  mcc_score = ((tp*tn)-(fp*fn))/((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))**.5
  return mcc_score

def wrangle_text(*, essay):
  doc = nlp(essay)
  doc_filter = [token for token in doc if token.is_alpha==True and token.is_stop==False and token.is_oov==False]
  doc_str = [token.text.lower() for token in doc_filter]
  return doc_str
