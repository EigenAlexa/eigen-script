'''
interpretor.py
Can read in files and interpret the details
https://stackoverflow.com/questions/2451821/string-formatting-named-parameters
'''
import yaml
import logging

VERBOSE_LOGGING=True
# logging.basicConfig('test.log')

def read_yaml(yaml_file):
  ''' reads yaml and returns a dictionary '''
  with open(yaml_file, 'r') as f:
    try:
      return yaml.safe_load(f)
    except yaml.YAMLError as exc:
      print(exc)
''' TODO make phrase into class'''
def get_prompts(phrase_dict):
  return list(phrase_dict['prompts'])
def get_responses(phrase_dict):
  return list(phrase_dict['responses'])
def get_name(phrase_dict):
  return phrase_dict['name']
def replace_string(string, keyword_dict):
  '''
  Replaces the stirng with the key in
  the keyword_dic
  >>> string = '{name} walked to the store'
  >>> keyword_dic = { 'name': 'Phillip' }
  >>> replace_string(string, keyword_dic)
  Phillip walked to the store
  '''
# could be improved by just iterating through the string and checking all of the curly braces
  for key, val in keyword_dict.items():

    string = string.replace('{'+key + '}', val)
  return string
def match(source_string, target_string):
  ''' returns true if the source string matches the target string and returns the dictionary of the mapping '''
# TODO probably just iterate through the words of hte source_string and see if they line up.
# Make sure to remove caps and special characters
  matching = True
  return matching
def get_keywords(string):
# TODO fill out this detail to grab the dictionary of the mapping
  return {}
def _log(string):
  ''' Logs and prints the string'''
  if VERBOSE_LOGGING:
    print(string)
  logging.info(string)
if __name__ == '__main__':

  _log('reading example file')
  yaml_dicts = read_yaml('example.yaml')[0]
  _log(yaml_dicts)
  test_phrase = 'What is Phillip doing?'
  _log("Running test phrase '{}'".format(test_phrase))
# TODO check the possible groups for matches
  possible_strings = get_prompts(yaml_dicts)
  for target_string in possible_strings:
    if match(test_phrase, target_string):
      keywords = get_keywords(test_phrase)
      break
  response_templ = get_responses(yaml_dicts)[0]
  _log('Reponse_templ" \'{}\''.format(response_templ))
  response_str = replace_string(response_templ,keywords)
  _log("Response string: '{}'".format(response_str))



