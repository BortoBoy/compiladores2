# Generated from grammar/Grammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#parse.
    def visitParse(self, ctx:GrammarParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#sql_stmt_list.
    def visitSql_stmt_list(self, ctx:GrammarParser.Sql_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#sql_stmt.
    def visitSql_stmt(self, ctx:GrammarParser.Sql_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#alter_table_stmt.
    def visitAlter_table_stmt(self, ctx:GrammarParser.Alter_table_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#analyze_stmt.
    def visitAnalyze_stmt(self, ctx:GrammarParser.Analyze_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#attach_stmt.
    def visitAttach_stmt(self, ctx:GrammarParser.Attach_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#begin_stmt.
    def visitBegin_stmt(self, ctx:GrammarParser.Begin_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#commit_stmt.
    def visitCommit_stmt(self, ctx:GrammarParser.Commit_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#rollback_stmt.
    def visitRollback_stmt(self, ctx:GrammarParser.Rollback_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#savepoint_stmt.
    def visitSavepoint_stmt(self, ctx:GrammarParser.Savepoint_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#release_stmt.
    def visitRelease_stmt(self, ctx:GrammarParser.Release_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#create_index_stmt.
    def visitCreate_index_stmt(self, ctx:GrammarParser.Create_index_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#indexed_column.
    def visitIndexed_column(self, ctx:GrammarParser.Indexed_columnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#create_table_stmt.
    def visitCreate_table_stmt(self, ctx:GrammarParser.Create_table_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#column_def.
    def visitColumn_def(self, ctx:GrammarParser.Column_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#type_name.
    def visitType_name(self, ctx:GrammarParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#column_constraint.
    def visitColumn_constraint(self, ctx:GrammarParser.Column_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#signed_number.
    def visitSigned_number(self, ctx:GrammarParser.Signed_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#table_constraint.
    def visitTable_constraint(self, ctx:GrammarParser.Table_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#foreign_key_clause.
    def visitForeign_key_clause(self, ctx:GrammarParser.Foreign_key_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#conflict_clause.
    def visitConflict_clause(self, ctx:GrammarParser.Conflict_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#create_trigger_stmt.
    def visitCreate_trigger_stmt(self, ctx:GrammarParser.Create_trigger_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#create_view_stmt.
    def visitCreate_view_stmt(self, ctx:GrammarParser.Create_view_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#create_virtual_table_stmt.
    def visitCreate_virtual_table_stmt(self, ctx:GrammarParser.Create_virtual_table_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#with_clause.
    def visitWith_clause(self, ctx:GrammarParser.With_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#cte_table_name.
    def visitCte_table_name(self, ctx:GrammarParser.Cte_table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#recursive_cte.
    def visitRecursive_cte(self, ctx:GrammarParser.Recursive_cteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#common_table_expression.
    def visitCommon_table_expression(self, ctx:GrammarParser.Common_table_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#delete_stmt.
    def visitDelete_stmt(self, ctx:GrammarParser.Delete_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#delete_stmt_limited.
    def visitDelete_stmt_limited(self, ctx:GrammarParser.Delete_stmt_limitedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#detach_stmt.
    def visitDetach_stmt(self, ctx:GrammarParser.Detach_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expr.
    def visitExpr(self, ctx:GrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#raise_function.
    def visitRaise_function(self, ctx:GrammarParser.Raise_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#literal_value.
    def visitLiteral_value(self, ctx:GrammarParser.Literal_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#insert_stmt.
    def visitInsert_stmt(self, ctx:GrammarParser.Insert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#upsert_clause.
    def visitUpsert_clause(self, ctx:GrammarParser.Upsert_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#pragma_stmt.
    def visitPragma_stmt(self, ctx:GrammarParser.Pragma_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#pragma_value.
    def visitPragma_value(self, ctx:GrammarParser.Pragma_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#reindex_stmt.
    def visitReindex_stmt(self, ctx:GrammarParser.Reindex_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#select_stmt.
    def visitSelect_stmt(self, ctx:GrammarParser.Select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#join_clause.
    def visitJoin_clause(self, ctx:GrammarParser.Join_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#select_core.
    def visitSelect_core(self, ctx:GrammarParser.Select_coreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#factored_select_stmt.
    def visitFactored_select_stmt(self, ctx:GrammarParser.Factored_select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#simple_select_stmt.
    def visitSimple_select_stmt(self, ctx:GrammarParser.Simple_select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#compound_select_stmt.
    def visitCompound_select_stmt(self, ctx:GrammarParser.Compound_select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#table_or_subquery.
    def visitTable_or_subquery(self, ctx:GrammarParser.Table_or_subqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#result_column.
    def visitResult_column(self, ctx:GrammarParser.Result_columnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#join_operator.
    def visitJoin_operator(self, ctx:GrammarParser.Join_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#join_constraint.
    def visitJoin_constraint(self, ctx:GrammarParser.Join_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#compound_operator.
    def visitCompound_operator(self, ctx:GrammarParser.Compound_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#update_stmt.
    def visitUpdate_stmt(self, ctx:GrammarParser.Update_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#column_name_list.
    def visitColumn_name_list(self, ctx:GrammarParser.Column_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#update_stmt_limited.
    def visitUpdate_stmt_limited(self, ctx:GrammarParser.Update_stmt_limitedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#qualified_table_name.
    def visitQualified_table_name(self, ctx:GrammarParser.Qualified_table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#vacuum_stmt.
    def visitVacuum_stmt(self, ctx:GrammarParser.Vacuum_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#filter_clause.
    def visitFilter_clause(self, ctx:GrammarParser.Filter_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#window_defn.
    def visitWindow_defn(self, ctx:GrammarParser.Window_defnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#over_clause.
    def visitOver_clause(self, ctx:GrammarParser.Over_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#frame_spec.
    def visitFrame_spec(self, ctx:GrammarParser.Frame_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#frame_clause.
    def visitFrame_clause(self, ctx:GrammarParser.Frame_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#simple_function_invocation.
    def visitSimple_function_invocation(self, ctx:GrammarParser.Simple_function_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#aggregate_function_invocation.
    def visitAggregate_function_invocation(self, ctx:GrammarParser.Aggregate_function_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#window_function_invocation.
    def visitWindow_function_invocation(self, ctx:GrammarParser.Window_function_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#common_table_stmt.
    def visitCommon_table_stmt(self, ctx:GrammarParser.Common_table_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#order_by_stmt.
    def visitOrder_by_stmt(self, ctx:GrammarParser.Order_by_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#limit_stmt.
    def visitLimit_stmt(self, ctx:GrammarParser.Limit_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ordering_term.
    def visitOrdering_term(self, ctx:GrammarParser.Ordering_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#asc_desc.
    def visitAsc_desc(self, ctx:GrammarParser.Asc_descContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#frame_left.
    def visitFrame_left(self, ctx:GrammarParser.Frame_leftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#frame_right.
    def visitFrame_right(self, ctx:GrammarParser.Frame_rightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#frame_single.
    def visitFrame_single(self, ctx:GrammarParser.Frame_singleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#window_function.
    def visitWindow_function(self, ctx:GrammarParser.Window_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#of_OF_fset.
    def visitOf_OF_fset(self, ctx:GrammarParser.Of_OF_fsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#default_DEFAULT__value.
    def visitDefault_DEFAULT__value(self, ctx:GrammarParser.Default_DEFAULT__valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#partition_by.
    def visitPartition_by(self, ctx:GrammarParser.Partition_byContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#order_by_expr.
    def visitOrder_by_expr(self, ctx:GrammarParser.Order_by_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#order_by_expr_asc_desc.
    def visitOrder_by_expr_asc_desc(self, ctx:GrammarParser.Order_by_expr_asc_descContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expr_asc_desc.
    def visitExpr_asc_desc(self, ctx:GrammarParser.Expr_asc_descContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#initial_select.
    def visitInitial_select(self, ctx:GrammarParser.Initial_selectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#recursive__select.
    def visitRecursive__select(self, ctx:GrammarParser.Recursive__selectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#unary_operator.
    def visitUnary_operator(self, ctx:GrammarParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#error_message.
    def visitError_message(self, ctx:GrammarParser.Error_messageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#module_argument.
    def visitModule_argument(self, ctx:GrammarParser.Module_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#column_alias.
    def visitColumn_alias(self, ctx:GrammarParser.Column_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#keyword.
    def visitKeyword(self, ctx:GrammarParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#name.
    def visitName(self, ctx:GrammarParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_name.
    def visitFunction_name(self, ctx:GrammarParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#schema_name.
    def visitSchema_name(self, ctx:GrammarParser.Schema_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#table_name.
    def visitTable_name(self, ctx:GrammarParser.Table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#table_or_index_name.
    def visitTable_or_index_name(self, ctx:GrammarParser.Table_or_index_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#new_table_name.
    def visitNew_table_name(self, ctx:GrammarParser.New_table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#column_name.
    def visitColumn_name(self, ctx:GrammarParser.Column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#collation_name.
    def visitCollation_name(self, ctx:GrammarParser.Collation_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#foreign_table.
    def visitForeign_table(self, ctx:GrammarParser.Foreign_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#index_name.
    def visitIndex_name(self, ctx:GrammarParser.Index_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#trigger_name.
    def visitTrigger_name(self, ctx:GrammarParser.Trigger_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#view_name.
    def visitView_name(self, ctx:GrammarParser.View_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#module_name.
    def visitModule_name(self, ctx:GrammarParser.Module_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#pragma_name.
    def visitPragma_name(self, ctx:GrammarParser.Pragma_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#savepoint_name.
    def visitSavepoint_name(self, ctx:GrammarParser.Savepoint_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#table_alias.
    def visitTable_alias(self, ctx:GrammarParser.Table_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#transaction_name.
    def visitTransaction_name(self, ctx:GrammarParser.Transaction_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#window_name.
    def visitWindow_name(self, ctx:GrammarParser.Window_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#alias.
    def visitAlias(self, ctx:GrammarParser.AliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#filename.
    def visitFilename(self, ctx:GrammarParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#base_window_name.
    def visitBase_window_name(self, ctx:GrammarParser.Base_window_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#simple_func.
    def visitSimple_func(self, ctx:GrammarParser.Simple_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#aggregate_func.
    def visitAggregate_func(self, ctx:GrammarParser.Aggregate_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#table_function_name.
    def visitTable_function_name(self, ctx:GrammarParser.Table_function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#any_name.
    def visitAny_name(self, ctx:GrammarParser.Any_nameContext):
        return self.visitChildren(ctx)



del GrammarParser