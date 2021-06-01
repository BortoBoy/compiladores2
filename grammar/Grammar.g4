grammar Grammar;

IDENT: ([a-z]|[A-Z]|\_) ([a-z]|[A-Z]|[0-9]|\_)*;
query: "SELECT" campos "FROM" table=IDENT;
campos: "*" | campos+=IDENT ("," campos+=IDE
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlineses
