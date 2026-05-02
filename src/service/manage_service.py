class ManageService:
    def get_expense_sum(self, account_id):
        self._refresh()
        df = self._merge_df
        return float(
            df[(df["account_id"] == account_id) & (df["type"] == "expense")]["amount"].sum()
        )

    def _refresh(self):
        pass

    def _merge_df(self, df):
        pass
