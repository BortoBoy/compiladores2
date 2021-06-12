grammar Grammar;

// lexer
SELECT: 'select';
FROM: 'from';
STAR: '*';
SEMI_COLUMN: ';';
COMMA: ',';
IDENT: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;
WS: ( ' ' |'\t' | '\r' | '\n') -> skip;

// parser
script: (select)*;
select: SELECT ((IDENT (',' IDENT)*)|STAR) FROM IDENT SEMI_COLUMN;
