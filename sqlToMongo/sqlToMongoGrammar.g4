grammar sqlToMongo

STRING: \*|[a-z]+;

query: "SELECT" campos "FROM" table;
campos: "*" | campo (",", campo)*;
campo: IDENT
table: IDENT