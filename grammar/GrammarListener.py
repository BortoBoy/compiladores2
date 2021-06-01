# Generated from grammar/Grammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#parse.
    def enterParse(self, ctx:GrammarParser.ParseContext):
        pass

    # Exit a parse tree produced by GrammarParser#parse.
    def exitParse(self, ctx:GrammarParser.ParseContext):
        pass


    # Enter a parse tree produced by GrammarParser#sql_stmt_list.
    def enterSql_stmt_list(self, ctx:GrammarParser.Sql_stmt_listContext):
        pass

    # Exit a parse tree produced by GrammarParser#sql_stmt_list.
    def exitSql_stmt_list(self, ctx:GrammarParser.Sql_stmt_listContext):
        pass


    # Enter a parse tree produced by GrammarParser#sql_stmt.
    def enterSql_stmt(self, ctx:GrammarParser.Sql_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#sql_stmt.
    def exitSql_stmt(self, ctx:GrammarParser.Sql_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#alter_table_stmt.
    def enterAlter_table_stmt(self, ctx:GrammarParser.Alter_table_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#alter_table_stmt.
    def exitAlter_table_stmt(self, ctx:GrammarParser.Alter_table_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#analyze_stmt.
    def enterAnalyze_stmt(self, ctx:GrammarParser.Analyze_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#analyze_stmt.
    def exitAnalyze_stmt(self, ctx:GrammarParser.Analyze_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#attach_stmt.
    def enterAttach_stmt(self, ctx:GrammarParser.Attach_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#attach_stmt.
    def exitAttach_stmt(self, ctx:GrammarParser.Attach_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#begin_stmt.
    def enterBegin_stmt(self, ctx:GrammarParser.Begin_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#begin_stmt.
    def exitBegin_stmt(self, ctx:GrammarParser.Begin_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#commit_stmt.
    def enterCommit_stmt(self, ctx:GrammarParser.Commit_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#commit_stmt.
    def exitCommit_stmt(self, ctx:GrammarParser.Commit_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#rollback_stmt.
    def enterRollback_stmt(self, ctx:GrammarParser.Rollback_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#rollback_stmt.
    def exitRollback_stmt(self, ctx:GrammarParser.Rollback_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#savepoint_stmt.
    def enterSavepoint_stmt(self, ctx:GrammarParser.Savepoint_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#savepoint_stmt.
    def exitSavepoint_stmt(self, ctx:GrammarParser.Savepoint_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#release_stmt.
    def enterRelease_stmt(self, ctx:GrammarParser.Release_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#release_stmt.
    def exitRelease_stmt(self, ctx:GrammarParser.Release_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#create_index_stmt.
    def enterCreate_index_stmt(self, ctx:GrammarParser.Create_index_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#create_index_stmt.
    def exitCreate_index_stmt(self, ctx:GrammarParser.Create_index_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#indexed_column.
    def enterIndexed_column(self, ctx:GrammarParser.Indexed_columnContext):
        pass

    # Exit a parse tree produced by GrammarParser#indexed_column.
    def exitIndexed_column(self, ctx:GrammarParser.Indexed_columnContext):
        pass


    # Enter a parse tree produced by GrammarParser#create_table_stmt.
    def enterCreate_table_stmt(self, ctx:GrammarParser.Create_table_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#create_table_stmt.
    def exitCreate_table_stmt(self, ctx:GrammarParser.Create_table_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#column_def.
    def enterColumn_def(self, ctx:GrammarParser.Column_defContext):
        pass

    # Exit a parse tree produced by GrammarParser#column_def.
    def exitColumn_def(self, ctx:GrammarParser.Column_defContext):
        pass


    # Enter a parse tree produced by GrammarParser#type_name.
    def enterType_name(self, ctx:GrammarParser.Type_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#type_name.
    def exitType_name(self, ctx:GrammarParser.Type_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#column_constraint.
    def enterColumn_constraint(self, ctx:GrammarParser.Column_constraintContext):
        pass

    # Exit a parse tree produced by GrammarParser#column_constraint.
    def exitColumn_constraint(self, ctx:GrammarParser.Column_constraintContext):
        pass


    # Enter a parse tree produced by GrammarParser#signed_number.
    def enterSigned_number(self, ctx:GrammarParser.Signed_numberContext):
        pass

    # Exit a parse tree produced by GrammarParser#signed_number.
    def exitSigned_number(self, ctx:GrammarParser.Signed_numberContext):
        pass


    # Enter a parse tree produced by GrammarParser#table_constraint.
    def enterTable_constraint(self, ctx:GrammarParser.Table_constraintContext):
        pass

    # Exit a parse tree produced by GrammarParser#table_constraint.
    def exitTable_constraint(self, ctx:GrammarParser.Table_constraintContext):
        pass


    # Enter a parse tree produced by GrammarParser#foreign_key_clause.
    def enterForeign_key_clause(self, ctx:GrammarParser.Foreign_key_clauseContext):
        pass

    # Exit a parse tree produced by GrammarParser#foreign_key_clause.
    def exitForeign_key_clause(self, ctx:GrammarParser.Foreign_key_clauseContext):
        pass


    # Enter a parse tree produced by GrammarParser#conflict_clause.
    def enterConflict_clause(self, ctx:GrammarParser.Conflict_clauseContext):
        pass

    # Exit a parse tree produced by GrammarParser#conflict_clause.
    def exitConflict_clause(self, ctx:GrammarParser.Conflict_clauseContext):
        pass


    # Enter a parse tree produced by GrammarParser#create_trigger_stmt.
    def enterCreate_trigger_stmt(self, ctx:GrammarParser.Create_trigger_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#create_trigger_stmt.
    def exitCreate_trigger_stmt(self, ctx:GrammarParser.Create_trigger_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#create_view_stmt.
    def enterCreate_view_stmt(self, ctx:GrammarParser.Create_view_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#create_view_stmt.
    def exitCreate_view_stmt(self, ctx:GrammarParser.Create_view_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#create_virtual_table_stmt.
    def enterCreate_virtual_table_stmt(self, ctx:GrammarParser.Create_virtual_table_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#create_virtual_table_stmt.
    def exitCreate_virtual_table_stmt(self, ctx:GrammarParser.Create_virtual_table_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#with_clause.
    def enterWith_clause(self, ctx:GrammarParser.With_clauseContext):
        pass

    # Exit a parse tree produced by GrammarParser#with_clause.
    def exitWith_clause(self, ctx:GrammarParser.With_clauseContext):
        pass


    # Enter a parse tree produced by GrammarParser#cte_table_name.
    def enterCte_table_name(self, ctx:GrammarParser.Cte_table_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#cte_table_name.
    def exitCte_table_name(self, ctx:GrammarParser.Cte_table_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#recursive_cte.
    def enterRecursive_cte(self, ctx:GrammarParser.Recursive_cteContext):
        pass

    # Exit a parse tree produced by GrammarParser#recursive_cte.
    def exitRecursive_cte(self, ctx:GrammarParser.Recursive_cteContext):
        pass


    # Enter a parse tree produced by GrammarParser#common_table_expression.
    def enterCommon_table_expression(self, ctx:GrammarParser.Common_table_expressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#common_table_expression.
    def exitCommon_table_expression(self, ctx:GrammarParser.Common_table_expressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#delete_stmt.
    def enterDelete_stmt(self, ctx:GrammarParser.Delete_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#delete_stmt.
    def exitDelete_stmt(self, ctx:GrammarParser.Delete_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#delete_stmt_limited.
    def enterDelete_stmt_limited(self, ctx:GrammarParser.Delete_stmt_limitedContext):
        pass

    # Exit a parse tree produced by GrammarParser#delete_stmt_limited.
    def exitDelete_stmt_limited(self, ctx:GrammarParser.Delete_stmt_limitedContext):
        pass


    # Enter a parse tree produced by GrammarParser#detach_stmt.
    def enterDetach_stmt(self, ctx:GrammarParser.Detach_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#detach_stmt.
    def exitDetach_stmt(self, ctx:GrammarParser.Detach_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#expr.
    def enterExpr(self, ctx:GrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#expr.
    def exitExpr(self, ctx:GrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#raise_function.
    def enterRaise_function(self, ctx:GrammarParser.Raise_functionContext):
        pass

    # Exit a parse tree produced by GrammarParser#raise_function.
    def exitRaise_function(self, ctx:GrammarParser.Raise_functionContext):
        pass


    # Enter a parse tree produced by GrammarParser#literal_value.
    def enterLiteral_value(self, ctx:GrammarParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by GrammarParser#literal_value.
    def exitLiteral_value(self, ctx:GrammarParser.Literal_valueContext):
        pass


    # Enter a parse tree produced by GrammarParser#insert_stmt.
    def enterInsert_stmt(self, ctx:GrammarParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#insert_stmt.
    def exitInsert_stmt(self, ctx:GrammarParser.Insert_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#upsert_clause.
    def enterUpsert_clause(self, ctx:GrammarParser.Upsert_clauseContext):
        pass

    # Exit a parse tree produced by GrammarParser#upsert_clause.
    def exitUpsert_clause(self, ctx:GrammarParser.Upsert_clauseContext):
        pass


    # Enter a parse tree produced by GrammarParser#pragma_stmt.
    def enterPragma_stmt(self, ctx:GrammarParser.Pragma_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#pragma_stmt.
    def exitPragma_stmt(self, ctx:GrammarParser.Pragma_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#pragma_value.
    def enterPragma_value(self, ctx:GrammarParser.Pragma_valueContext):
        pass

    # Exit a parse tree produced by GrammarParser#pragma_value.
    def exitPragma_value(self, ctx:GrammarParser.Pragma_valueContext):
        pass


    # Enter a parse tree produced by GrammarParser#reindex_stmt.
    def enterReindex_stmt(self, ctx:GrammarParser.Reindex_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#reindex_stmt.
    def exitReindex_stmt(self, ctx:GrammarParser.Reindex_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#select_stmt.
    def enterSelect_stmt(self, ctx:GrammarParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#select_stmt.
    def exitSelect_stmt(self, ctx:GrammarParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#join_clause.
    def enterJoin_clause(self, ctx:GrammarParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by GrammarParser#join_clause.
    def exitJoin_clause(self, ctx:GrammarParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by GrammarParser#select_core.
    def enterSelect_core(self, ctx:GrammarParser.Select_coreContext):
        pass

    # Exit a parse tree produced by GrammarParser#select_core.
    def exitSelect_core(self, ctx:GrammarParser.Select_coreContext):
        pass


    # Enter a parse tree produced by GrammarParser#factored_select_stmt.
    def enterFactored_select_stmt(self, ctx:GrammarParser.Factored_select_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#factored_select_stmt.
    def exitFactored_select_stmt(self, ctx:GrammarParser.Factored_select_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#simple_select_stmt.
    def enterSimple_select_stmt(self, ctx:GrammarParser.Simple_select_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#simple_select_stmt.
    def exitSimple_select_stmt(self, ctx:GrammarParser.Simple_select_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#compound_select_stmt.
    def enterCompound_select_stmt(self, ctx:GrammarParser.Compound_select_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#compound_select_stmt.
    def exitCompound_select_stmt(self, ctx:GrammarParser.Compound_select_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#table_or_subquery.
    def enterTable_or_subquery(self, ctx:GrammarParser.Table_or_subqueryContext):
        pass

    # Exit a parse tree produced by GrammarParser#table_or_subquery.
    def exitTable_or_subquery(self, ctx:GrammarParser.Table_or_subqueryContext):
        pass


    # Enter a parse tree produced by GrammarParser#result_column.
    def enterResult_column(self, ctx:GrammarParser.Result_columnContext):
        pass

    # Exit a parse tree produced by GrammarParser#result_column.
    def exitResult_column(self, ctx:GrammarParser.Result_columnContext):
        pass


    # Enter a parse tree produced by GrammarParser#join_operator.
    def enterJoin_operator(self, ctx:GrammarParser.Join_operatorContext):
        pass

    # Exit a parse tree produced by GrammarParser#join_operator.
    def exitJoin_operator(self, ctx:GrammarParser.Join_operatorContext):
        pass


    # Enter a parse tree produced by GrammarParser#join_constraint.
    def enterJoin_constraint(self, ctx:GrammarParser.Join_constraintContext):
        pass

    # Exit a parse tree produced by GrammarParser#join_constraint.
    def exitJoin_constraint(self, ctx:GrammarParser.Join_constraintContext):
        pass


    # Enter a parse tree produced by GrammarParser#compound_operator.
    def enterCompound_operator(self, ctx:GrammarParser.Compound_operatorContext):
        pass

    # Exit a parse tree produced by GrammarParser#compound_operator.
    def exitCompound_operator(self, ctx:GrammarParser.Compound_operatorContext):
        pass


    # Enter a parse tree produced by GrammarParser#update_stmt.
    def enterUpdate_stmt(self, ctx:GrammarParser.Update_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#update_stmt.
    def exitUpdate_stmt(self, ctx:GrammarParser.Update_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#column_name_list.
    def enterColumn_name_list(self, ctx:GrammarParser.Column_name_listContext):
        pass

    # Exit a parse tree produced by GrammarParser#column_name_list.
    def exitColumn_name_list(self, ctx:GrammarParser.Column_name_listContext):
        pass


    # Enter a parse tree produced by GrammarParser#update_stmt_limited.
    def enterUpdate_stmt_limited(self, ctx:GrammarParser.Update_stmt_limitedContext):
        pass

    # Exit a parse tree produced by GrammarParser#update_stmt_limited.
    def exitUpdate_stmt_limited(self, ctx:GrammarParser.Update_stmt_limitedContext):
        pass


    # Enter a parse tree produced by GrammarParser#qualified_table_name.
    def enterQualified_table_name(self, ctx:GrammarParser.Qualified_table_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#qualified_table_name.
    def exitQualified_table_name(self, ctx:GrammarParser.Qualified_table_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#vacuum_stmt.
    def enterVacuum_stmt(self, ctx:GrammarParser.Vacuum_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#vacuum_stmt.
    def exitVacuum_stmt(self, ctx:GrammarParser.Vacuum_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#filter_clause.
    def enterFilter_clause(self, ctx:GrammarParser.Filter_clauseContext):
        pass

    # Exit a parse tree produced by GrammarParser#filter_clause.
    def exitFilter_clause(self, ctx:GrammarParser.Filter_clauseContext):
        pass


    # Enter a parse tree produced by GrammarParser#window_defn.
    def enterWindow_defn(self, ctx:GrammarParser.Window_defnContext):
        pass

    # Exit a parse tree produced by GrammarParser#window_defn.
    def exitWindow_defn(self, ctx:GrammarParser.Window_defnContext):
        pass


    # Enter a parse tree produced by GrammarParser#over_clause.
    def enterOver_clause(self, ctx:GrammarParser.Over_clauseContext):
        pass

    # Exit a parse tree produced by GrammarParser#over_clause.
    def exitOver_clause(self, ctx:GrammarParser.Over_clauseContext):
        pass


    # Enter a parse tree produced by GrammarParser#frame_spec.
    def enterFrame_spec(self, ctx:GrammarParser.Frame_specContext):
        pass

    # Exit a parse tree produced by GrammarParser#frame_spec.
    def exitFrame_spec(self, ctx:GrammarParser.Frame_specContext):
        pass


    # Enter a parse tree produced by GrammarParser#frame_clause.
    def enterFrame_clause(self, ctx:GrammarParser.Frame_clauseContext):
        pass

    # Exit a parse tree produced by GrammarParser#frame_clause.
    def exitFrame_clause(self, ctx:GrammarParser.Frame_clauseContext):
        pass


    # Enter a parse tree produced by GrammarParser#simple_function_invocation.
    def enterSimple_function_invocation(self, ctx:GrammarParser.Simple_function_invocationContext):
        pass

    # Exit a parse tree produced by GrammarParser#simple_function_invocation.
    def exitSimple_function_invocation(self, ctx:GrammarParser.Simple_function_invocationContext):
        pass


    # Enter a parse tree produced by GrammarParser#aggregate_function_invocation.
    def enterAggregate_function_invocation(self, ctx:GrammarParser.Aggregate_function_invocationContext):
        pass

    # Exit a parse tree produced by GrammarParser#aggregate_function_invocation.
    def exitAggregate_function_invocation(self, ctx:GrammarParser.Aggregate_function_invocationContext):
        pass


    # Enter a parse tree produced by GrammarParser#window_function_invocation.
    def enterWindow_function_invocation(self, ctx:GrammarParser.Window_function_invocationContext):
        pass

    # Exit a parse tree produced by GrammarParser#window_function_invocation.
    def exitWindow_function_invocation(self, ctx:GrammarParser.Window_function_invocationContext):
        pass


    # Enter a parse tree produced by GrammarParser#common_table_stmt.
    def enterCommon_table_stmt(self, ctx:GrammarParser.Common_table_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#common_table_stmt.
    def exitCommon_table_stmt(self, ctx:GrammarParser.Common_table_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#order_by_stmt.
    def enterOrder_by_stmt(self, ctx:GrammarParser.Order_by_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#order_by_stmt.
    def exitOrder_by_stmt(self, ctx:GrammarParser.Order_by_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#limit_stmt.
    def enterLimit_stmt(self, ctx:GrammarParser.Limit_stmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#limit_stmt.
    def exitLimit_stmt(self, ctx:GrammarParser.Limit_stmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#ordering_term.
    def enterOrdering_term(self, ctx:GrammarParser.Ordering_termContext):
        pass

    # Exit a parse tree produced by GrammarParser#ordering_term.
    def exitOrdering_term(self, ctx:GrammarParser.Ordering_termContext):
        pass


    # Enter a parse tree produced by GrammarParser#asc_desc.
    def enterAsc_desc(self, ctx:GrammarParser.Asc_descContext):
        pass

    # Exit a parse tree produced by GrammarParser#asc_desc.
    def exitAsc_desc(self, ctx:GrammarParser.Asc_descContext):
        pass


    # Enter a parse tree produced by GrammarParser#frame_left.
    def enterFrame_left(self, ctx:GrammarParser.Frame_leftContext):
        pass

    # Exit a parse tree produced by GrammarParser#frame_left.
    def exitFrame_left(self, ctx:GrammarParser.Frame_leftContext):
        pass


    # Enter a parse tree produced by GrammarParser#frame_right.
    def enterFrame_right(self, ctx:GrammarParser.Frame_rightContext):
        pass

    # Exit a parse tree produced by GrammarParser#frame_right.
    def exitFrame_right(self, ctx:GrammarParser.Frame_rightContext):
        pass


    # Enter a parse tree produced by GrammarParser#frame_single.
    def enterFrame_single(self, ctx:GrammarParser.Frame_singleContext):
        pass

    # Exit a parse tree produced by GrammarParser#frame_single.
    def exitFrame_single(self, ctx:GrammarParser.Frame_singleContext):
        pass


    # Enter a parse tree produced by GrammarParser#window_function.
    def enterWindow_function(self, ctx:GrammarParser.Window_functionContext):
        pass

    # Exit a parse tree produced by GrammarParser#window_function.
    def exitWindow_function(self, ctx:GrammarParser.Window_functionContext):
        pass


    # Enter a parse tree produced by GrammarParser#of_OF_fset.
    def enterOf_OF_fset(self, ctx:GrammarParser.Of_OF_fsetContext):
        pass

    # Exit a parse tree produced by GrammarParser#of_OF_fset.
    def exitOf_OF_fset(self, ctx:GrammarParser.Of_OF_fsetContext):
        pass


    # Enter a parse tree produced by GrammarParser#default_DEFAULT__value.
    def enterDefault_DEFAULT__value(self, ctx:GrammarParser.Default_DEFAULT__valueContext):
        pass

    # Exit a parse tree produced by GrammarParser#default_DEFAULT__value.
    def exitDefault_DEFAULT__value(self, ctx:GrammarParser.Default_DEFAULT__valueContext):
        pass


    # Enter a parse tree produced by GrammarParser#partition_by.
    def enterPartition_by(self, ctx:GrammarParser.Partition_byContext):
        pass

    # Exit a parse tree produced by GrammarParser#partition_by.
    def exitPartition_by(self, ctx:GrammarParser.Partition_byContext):
        pass


    # Enter a parse tree produced by GrammarParser#order_by_expr.
    def enterOrder_by_expr(self, ctx:GrammarParser.Order_by_exprContext):
        pass

    # Exit a parse tree produced by GrammarParser#order_by_expr.
    def exitOrder_by_expr(self, ctx:GrammarParser.Order_by_exprContext):
        pass


    # Enter a parse tree produced by GrammarParser#order_by_expr_asc_desc.
    def enterOrder_by_expr_asc_desc(self, ctx:GrammarParser.Order_by_expr_asc_descContext):
        pass

    # Exit a parse tree produced by GrammarParser#order_by_expr_asc_desc.
    def exitOrder_by_expr_asc_desc(self, ctx:GrammarParser.Order_by_expr_asc_descContext):
        pass


    # Enter a parse tree produced by GrammarParser#expr_asc_desc.
    def enterExpr_asc_desc(self, ctx:GrammarParser.Expr_asc_descContext):
        pass

    # Exit a parse tree produced by GrammarParser#expr_asc_desc.
    def exitExpr_asc_desc(self, ctx:GrammarParser.Expr_asc_descContext):
        pass


    # Enter a parse tree produced by GrammarParser#initial_select.
    def enterInitial_select(self, ctx:GrammarParser.Initial_selectContext):
        pass

    # Exit a parse tree produced by GrammarParser#initial_select.
    def exitInitial_select(self, ctx:GrammarParser.Initial_selectContext):
        pass


    # Enter a parse tree produced by GrammarParser#recursive__select.
    def enterRecursive__select(self, ctx:GrammarParser.Recursive__selectContext):
        pass

    # Exit a parse tree produced by GrammarParser#recursive__select.
    def exitRecursive__select(self, ctx:GrammarParser.Recursive__selectContext):
        pass


    # Enter a parse tree produced by GrammarParser#unary_operator.
    def enterUnary_operator(self, ctx:GrammarParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by GrammarParser#unary_operator.
    def exitUnary_operator(self, ctx:GrammarParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by GrammarParser#error_message.
    def enterError_message(self, ctx:GrammarParser.Error_messageContext):
        pass

    # Exit a parse tree produced by GrammarParser#error_message.
    def exitError_message(self, ctx:GrammarParser.Error_messageContext):
        pass


    # Enter a parse tree produced by GrammarParser#module_argument.
    def enterModule_argument(self, ctx:GrammarParser.Module_argumentContext):
        pass

    # Exit a parse tree produced by GrammarParser#module_argument.
    def exitModule_argument(self, ctx:GrammarParser.Module_argumentContext):
        pass


    # Enter a parse tree produced by GrammarParser#column_alias.
    def enterColumn_alias(self, ctx:GrammarParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by GrammarParser#column_alias.
    def exitColumn_alias(self, ctx:GrammarParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by GrammarParser#keyword.
    def enterKeyword(self, ctx:GrammarParser.KeywordContext):
        pass

    # Exit a parse tree produced by GrammarParser#keyword.
    def exitKeyword(self, ctx:GrammarParser.KeywordContext):
        pass


    # Enter a parse tree produced by GrammarParser#name.
    def enterName(self, ctx:GrammarParser.NameContext):
        pass

    # Exit a parse tree produced by GrammarParser#name.
    def exitName(self, ctx:GrammarParser.NameContext):
        pass


    # Enter a parse tree produced by GrammarParser#function_name.
    def enterFunction_name(self, ctx:GrammarParser.Function_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#function_name.
    def exitFunction_name(self, ctx:GrammarParser.Function_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#schema_name.
    def enterSchema_name(self, ctx:GrammarParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#schema_name.
    def exitSchema_name(self, ctx:GrammarParser.Schema_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#table_name.
    def enterTable_name(self, ctx:GrammarParser.Table_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#table_name.
    def exitTable_name(self, ctx:GrammarParser.Table_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#table_or_index_name.
    def enterTable_or_index_name(self, ctx:GrammarParser.Table_or_index_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#table_or_index_name.
    def exitTable_or_index_name(self, ctx:GrammarParser.Table_or_index_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#new_table_name.
    def enterNew_table_name(self, ctx:GrammarParser.New_table_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#new_table_name.
    def exitNew_table_name(self, ctx:GrammarParser.New_table_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#column_name.
    def enterColumn_name(self, ctx:GrammarParser.Column_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#column_name.
    def exitColumn_name(self, ctx:GrammarParser.Column_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#collation_name.
    def enterCollation_name(self, ctx:GrammarParser.Collation_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#collation_name.
    def exitCollation_name(self, ctx:GrammarParser.Collation_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#foreign_table.
    def enterForeign_table(self, ctx:GrammarParser.Foreign_tableContext):
        pass

    # Exit a parse tree produced by GrammarParser#foreign_table.
    def exitForeign_table(self, ctx:GrammarParser.Foreign_tableContext):
        pass


    # Enter a parse tree produced by GrammarParser#index_name.
    def enterIndex_name(self, ctx:GrammarParser.Index_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#index_name.
    def exitIndex_name(self, ctx:GrammarParser.Index_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#trigger_name.
    def enterTrigger_name(self, ctx:GrammarParser.Trigger_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#trigger_name.
    def exitTrigger_name(self, ctx:GrammarParser.Trigger_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#view_name.
    def enterView_name(self, ctx:GrammarParser.View_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#view_name.
    def exitView_name(self, ctx:GrammarParser.View_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#module_name.
    def enterModule_name(self, ctx:GrammarParser.Module_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#module_name.
    def exitModule_name(self, ctx:GrammarParser.Module_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#pragma_name.
    def enterPragma_name(self, ctx:GrammarParser.Pragma_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#pragma_name.
    def exitPragma_name(self, ctx:GrammarParser.Pragma_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#savepoint_name.
    def enterSavepoint_name(self, ctx:GrammarParser.Savepoint_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#savepoint_name.
    def exitSavepoint_name(self, ctx:GrammarParser.Savepoint_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#table_alias.
    def enterTable_alias(self, ctx:GrammarParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by GrammarParser#table_alias.
    def exitTable_alias(self, ctx:GrammarParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by GrammarParser#transaction_name.
    def enterTransaction_name(self, ctx:GrammarParser.Transaction_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#transaction_name.
    def exitTransaction_name(self, ctx:GrammarParser.Transaction_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#window_name.
    def enterWindow_name(self, ctx:GrammarParser.Window_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#window_name.
    def exitWindow_name(self, ctx:GrammarParser.Window_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#alias.
    def enterAlias(self, ctx:GrammarParser.AliasContext):
        pass

    # Exit a parse tree produced by GrammarParser#alias.
    def exitAlias(self, ctx:GrammarParser.AliasContext):
        pass


    # Enter a parse tree produced by GrammarParser#filename.
    def enterFilename(self, ctx:GrammarParser.FilenameContext):
        pass

    # Exit a parse tree produced by GrammarParser#filename.
    def exitFilename(self, ctx:GrammarParser.FilenameContext):
        pass


    # Enter a parse tree produced by GrammarParser#base_window_name.
    def enterBase_window_name(self, ctx:GrammarParser.Base_window_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#base_window_name.
    def exitBase_window_name(self, ctx:GrammarParser.Base_window_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#simple_func.
    def enterSimple_func(self, ctx:GrammarParser.Simple_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#simple_func.
    def exitSimple_func(self, ctx:GrammarParser.Simple_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#aggregate_func.
    def enterAggregate_func(self, ctx:GrammarParser.Aggregate_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#aggregate_func.
    def exitAggregate_func(self, ctx:GrammarParser.Aggregate_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#table_function_name.
    def enterTable_function_name(self, ctx:GrammarParser.Table_function_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#table_function_name.
    def exitTable_function_name(self, ctx:GrammarParser.Table_function_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#any_name.
    def enterAny_name(self, ctx:GrammarParser.Any_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#any_name.
    def exitAny_name(self, ctx:GrammarParser.Any_nameContext):
        pass



del GrammarParser