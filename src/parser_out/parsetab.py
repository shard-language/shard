
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftSTARSLASHPERCENTleftEQUALPLUS_EQUALMINUS_EQUALSTAR_EQUALSLASH_EQUALPERCENT_EQUALrightPOSITIVENEGATIVEBYTE DOUBLE DWORD EQUAL FLOAT IDENTIFIER LPAR MINUS MINUS_EQUAL NUMBER PERCENT PERCENT_EQUAL PLUS PLUS_EQUAL QWORD RPAR SEMI SLASH SLASH_EQUAL STAR STAR_EQUAL WORDprogram : statement_liststatement_list : statement\n                      | statement SEMI statement_liststatement : empty\n                 | expression\n                 | declarationempty :expression : NUMBERexpression : IDENTIFIERexpression : PLUS expression %prec POSITIVE\n                  | MINUS expression %prec NEGATIVEexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression STAR expression\n                  | expression SLASH expression\n                  | expression PERCENT expressionexpression : LPAR expression RPARexpression : IDENTIFIER EQUAL expression\n                  | IDENTIFIER PLUS_EQUAL expression\n                  | IDENTIFIER MINUS_EQUAL expression\n                  | IDENTIFIER STAR_EQUAL expression\n                  | IDENTIFIER SLASH_EQUAL expression\n                  | IDENTIFIER PERCENT_EQUAL expressiondeclaration : BYTE IDENTIFIER\n                   | WORD IDENTIFIER\n                   | DWORD IDENTIFIER\n                   | QWORD IDENTIFIER\n                   | FLOAT IDENTIFIER\n                   | DOUBLE IDENTIFIER'
    
_lr_action_items = {'SEMI':([0,3,4,5,6,7,8,18,30,31,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,],[-7,18,-4,-5,-6,-8,-9,-7,-10,-11,-24,-25,-26,-27,-28,-29,-12,-13,-14,-15,-16,-18,-19,-20,-21,-22,-23,-17,]),'$end':([0,1,2,3,4,5,6,7,8,18,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,],[-7,0,-1,-2,-4,-5,-6,-8,-9,-7,-10,-11,-24,-25,-26,-27,-28,-29,-3,-12,-13,-14,-15,-16,-18,-19,-20,-21,-22,-23,-17,]),'NUMBER':([0,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'IDENTIFIER':([0,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,],[8,8,8,8,33,34,35,36,37,38,8,8,8,8,8,8,8,8,8,8,8,8,]),'PLUS':([0,5,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,40,41,42,43,44,45,46,47,48,49,50,51,],[9,19,-8,-9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-10,-11,19,-12,-13,-14,-15,-16,-18,-19,-20,-21,-22,-23,-17,]),'MINUS':([0,5,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,40,41,42,43,44,45,46,47,48,49,50,51,],[10,20,-8,-9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-10,-11,20,-12,-13,-14,-15,-16,-18,-19,-20,-21,-22,-23,-17,]),'LPAR':([0,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'BYTE':([0,18,],[12,12,]),'WORD':([0,18,],[13,13,]),'DWORD':([0,18,],[14,14,]),'QWORD':([0,18,],[15,15,]),'FLOAT':([0,18,],[16,16,]),'DOUBLE':([0,18,],[17,17,]),'STAR':([5,7,8,30,31,32,40,41,42,43,44,45,46,47,48,49,50,51,],[21,-8,-9,-10,-11,21,21,21,-14,-15,-16,-18,-19,-20,-21,-22,-23,-17,]),'SLASH':([5,7,8,30,31,32,40,41,42,43,44,45,46,47,48,49,50,51,],[22,-8,-9,-10,-11,22,22,22,-14,-15,-16,-18,-19,-20,-21,-22,-23,-17,]),'PERCENT':([5,7,8,30,31,32,40,41,42,43,44,45,46,47,48,49,50,51,],[23,-8,-9,-10,-11,23,23,23,-14,-15,-16,-18,-19,-20,-21,-22,-23,-17,]),'RPAR':([7,8,30,31,32,40,41,42,43,44,45,46,47,48,49,50,51,],[-8,-9,-10,-11,51,-12,-13,-14,-15,-16,-18,-19,-20,-21,-22,-23,-17,]),'EQUAL':([8,],[24,]),'PLUS_EQUAL':([8,],[25,]),'MINUS_EQUAL':([8,],[26,]),'STAR_EQUAL':([8,],[27,]),'SLASH_EQUAL':([8,],[28,]),'PERCENT_EQUAL':([8,],[29,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,18,],[2,39,]),'statement':([0,18,],[3,3,]),'empty':([0,18,],[4,4,]),'expression':([0,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,],[5,30,31,32,5,40,41,42,43,44,45,46,47,48,49,50,]),'declaration':([0,18,],[6,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.pyc',16),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.pyc',20),
  ('statement_list -> statement SEMI statement_list','statement_list',3,'p_statement_list','parser.pyc',21),
  ('statement -> empty','statement',1,'p_statement','parser.pyc',25),
  ('statement -> expression','statement',1,'p_statement','parser.pyc',26),
  ('statement -> declaration','statement',1,'p_statement','parser.pyc',27),
  ('empty -> <empty>','empty',0,'p_empty','parser.pyc',31),
  ('expression -> NUMBER','expression',1,'p_expression_value','parser.pyc',35),
  ('expression -> IDENTIFIER','expression',1,'p_expression_variable_value','parser.pyc',39),
  ('expression -> PLUS expression','expression',2,'p_expression_unary','parser.pyc',43),
  ('expression -> MINUS expression','expression',2,'p_expression_unary','parser.pyc',44),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binary','parser.pyc',48),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binary','parser.pyc',49),
  ('expression -> expression STAR expression','expression',3,'p_expression_binary','parser.pyc',50),
  ('expression -> expression SLASH expression','expression',3,'p_expression_binary','parser.pyc',51),
  ('expression -> expression PERCENT expression','expression',3,'p_expression_binary','parser.pyc',52),
  ('expression -> LPAR expression RPAR','expression',3,'p_expression_group','parser.pyc',56),
  ('expression -> IDENTIFIER EQUAL expression','expression',3,'p_expression_assignment_variable','parser.pyc',60),
  ('expression -> IDENTIFIER PLUS_EQUAL expression','expression',3,'p_expression_assignment_variable','parser.pyc',61),
  ('expression -> IDENTIFIER MINUS_EQUAL expression','expression',3,'p_expression_assignment_variable','parser.pyc',62),
  ('expression -> IDENTIFIER STAR_EQUAL expression','expression',3,'p_expression_assignment_variable','parser.pyc',63),
  ('expression -> IDENTIFIER SLASH_EQUAL expression','expression',3,'p_expression_assignment_variable','parser.pyc',64),
  ('expression -> IDENTIFIER PERCENT_EQUAL expression','expression',3,'p_expression_assignment_variable','parser.pyc',65),
  ('declaration -> BYTE IDENTIFIER','declaration',2,'p_declaration_variable','parser.pyc',69),
  ('declaration -> WORD IDENTIFIER','declaration',2,'p_declaration_variable','parser.pyc',70),
  ('declaration -> DWORD IDENTIFIER','declaration',2,'p_declaration_variable','parser.pyc',71),
  ('declaration -> QWORD IDENTIFIER','declaration',2,'p_declaration_variable','parser.pyc',72),
  ('declaration -> FLOAT IDENTIFIER','declaration',2,'p_declaration_variable','parser.pyc',73),
  ('declaration -> DOUBLE IDENTIFIER','declaration',2,'p_declaration_variable','parser.pyc',74),
]
