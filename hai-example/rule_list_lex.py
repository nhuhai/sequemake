# module: rule_list_lex.py
# This module just contains the lexing rules for <rule list>
import ply.lex as lex

# List of token names.   This is always required
tokens = [
   'RESULT_BY_NODE',
   'RESULT_BY_EDGE',
   'RESULT_BY_SEQUENCE',
   'COLON',
   'MAKE_LITERAL'
]

# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_COLON(t):
  r':'
  return t

def t_RESULT_BY_NODE(t):
  r'\@NODE\d*@/[-_A-Za-z0-9.][^ /:\n]+'
  return t

def t_RESULT_BY_EDGE(t):
  r'\@EDGE@/[-_A-Za-z0-9.][^ /:\n]+'
  return t

def t_RESULT_BY_SEQUENCE(t):
  r'\@SEQUENCE@/[-_A-Za-z0-9.][^ /:\n]+'
  return t 

def t_ASSIGNMENT_OPERATOR(t):
  r'=|:=|\ ?='
  return t

def t_MAKE_LITERAL(t):
  r'[^ \n\t]+'
  return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)