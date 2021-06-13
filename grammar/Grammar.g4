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
IDENT: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;
WS: ( ' ' |'\t' | '\r' | '\n') -> skip;

// parser
script: (simple_select_command | select_with_join_command)*;
select_base: SELECT ((IDENT (',' IDENT)*)|STAR) FROM IDENT;
join_type: RIGHT_JOIN | LEFT_JOIN;
join_base: join_type IDENT ON IDENT POINT IDENT EQUALS IDENT POINT IDENT;
simple_select_command: select_base SEMI_COLUMN;
select_with_join_command: select_base join_base SEMI_COLUMN;
