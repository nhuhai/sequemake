import ply.lex as lex

# List of token names.   This is always required
tokens = [
   'MAKE_VARIABLE_NAME',
   'ASSIGNMENT_OPERATOR',
   'MAKE_LITERAL'
]

# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_MAKE_VARIABLE_NAME(t):
  r'[A-Z][^:#=\n\t/. ]+'
  return t

def t_ASSIGNMENT_OPERATOR(t):
  r'=|:=|\ ?='
  return t

def t_MAKE_LITERAL(t):
  r'.[^ \n\t]+'
  return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
ECHO_NODE_ID_SCRIPT_PATH        = src/echo_node_id.sh
CAT_NODE_IDS_SCRIPT_PATH        = src/cat_node_ids.sh
LIST_NODE_IDS_SCRIPT_PATH       = src/list_node_ids.sh
WRITE_EDGE_SCRIPT_PATH          = src/write_edges.sh
WRITE_NODE_SENTENCE_SCRIPT_PATH = src/write_node_sentences.sh
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok