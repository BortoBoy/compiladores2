grammar sqlToMongo

STRING: ([a-z]|[A-Z]|[0-9]|\_)+;

query: "SELECT" campos "FROM" table;
campos: "*" | campo (",", campo)*;
campo: IDENT
table: IDENT