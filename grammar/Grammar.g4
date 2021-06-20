grammar Grammar;

// lexer
SELECT: 'select';
FROM: 'from';
STAR: '*';
SEMI_COLUMN: ';';
COMMA: ',';
POINT: '.';
EQUALS: '=';
RIGHT_JOIN: 'right join';
LEFT_JOIN: 'left join';
ON: 'on';
AS: 'as';
IDENT: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;
WS: ( ' ' |'\t' | '\r' | '\n') -> skip;
LINE_COMMENT: '#' ~[\r\n]* -> skip;

// parser
script: (simple_select_command | select_with_join_command)*;
select_base_field: (table = IDENT POINT)? field = IDENT (AS alias = IDENT)?;
select_base_table: table = IDENT (AS alias = IDENT)?;
select_base: SELECT ((select_base_field (',' select_base_field)*)|STAR) FROM select_base_table;
join_type: RIGHT_JOIN | LEFT_JOIN;
join_base: join_type select_base_table ON left_table = IDENT POINT left_field = IDENT EQUALS right_table = IDENT POINT right_field = IDENT;
simple_select_command: select_base SEMI_COLUMN;
select_with_join_command: select_base join_base SEMI_COLUMN;
