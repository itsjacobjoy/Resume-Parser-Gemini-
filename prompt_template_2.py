#Linking prompt to ensure it follows JSON structure
def prompt_template_2(results):
  template = f'''
  System: Correct any errors to ensure that it follows json structure.

  input: {results}

  json output: '''

  return template