grammar sqlToMongo

// IDENT: ( 'a'..'z' | 'A'..'Z' |'0'..'9' |'_' ) ( 'a'..'z' | 'A'..'Z' | '0'..'9' | '_' )*;
IDENT: ([a-z]|[A-Z]|[0-9]|\_)+;
// OP: ('='| '>=' | '<=' | '>' | '<');
OP:(\=|\>|\<);


query: "SELECT" campos "FROM" table "WHERE" comparison;
campos: "*" | campo (",", campo)*;
campo: IDENT;
table: IDENT;
comparison: column operator value;
column: IDENT;
operator: OP;
value: """ IDENT """;