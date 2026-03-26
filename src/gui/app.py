import tkinter as tk
from tkinter import ttk

from src.data.repository import AccountRepo
from src.service.account_service import AccountService


class ExpenseTrackerApp:
    """
    Tkinter/ttk desktop UI for the expense tracker.

    Responsibilities:
    - Build and style the main window layout (header, actions, account list, status/details)
    - Call the service layer to load account data
    - React to user actions (button clicks and list selection) and update the UI
    - More needs to be added 
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("760x520")
        self.root.minsize(680, 460)
        self.root.configure(bg="#f3f4f6")

        #backend wiring
        self.repo = AccountRepo()
        self.service = AccountService(self.repo)

        #UI state shown to the user
        self.status_var = tk.StringVar(value="Click 'Load Accounts' to view accounts.")
        self.detail_var = tk.StringVar(value="Select an account in the list to see its balance.")

        #cache the loaded Account objects so list selection can map row index -> account
        self._loaded_accounts = []

        self._configure_styles()
        self._build_layout()

    def _configure_styles(self):
        #making the UI look consistent with centralized styling
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Header.TLabel", font=("Helvetica", 22, "bold"), foreground="#111827")
        style.configure("Subheader.TLabel", font=("Helvetica", 10), foreground="#4b5563")
        style.configure("Card.TFrame", background="#ffffff")
        style.configure("Primary.TButton", font=("Helvetica", 11, "bold"), padding=(12, 8))
        style.configure("Status.TLabel", font=("Helvetica", 10), foreground="#1f2937")

    def _build_layout(self):
        #here is layout overview:
        # container
        #   header (title + subtitle)
        #   card
        #     actions (Load Accounts)
        #     list section (accounts list + scrollbar + detail line)
        #     status line
        container = ttk.Frame(self.root, padding=24)
        container.pack(fill="both", expand=True)

        header = ttk.Frame(container)
        header.pack(fill="x", pady=(0, 14))

        title = ttk.Label(header, text="Expense Tracker", style="Header.TLabel")
        title.pack(anchor="w")
        subtitle = ttk.Label(
            header,
            text="Manage your accounts and quickly review balances.",
            style="Subheader.TLabel",
        )
        subtitle.pack(anchor="w", pady=(4, 0))

        card = ttk.Frame(container, style="Card.TFrame", padding=16)
        card.pack(fill="both", expand=True)

        actions = ttk.Frame(card)
        actions.pack(fill="x", pady=(0, 12))

        load_btn = ttk.Button(
            actions,
            text="Load Accounts",
            command=self.load_accounts,
            style="Primary.TButton",
        )
        load_btn.pack(side="left")

        list_section = ttk.Frame(card)
        list_section.pack(fill="both", expand=True)

        list_label = ttk.Label(list_section, text="Accounts", style="Subheader.TLabel")
        list_label.pack(anchor="w", pady=(0, 6))

        list_frame = ttk.Frame(list_section)
        list_frame.pack(fill="both", expand=True)

        #setting explicit colors for background/text and selection highlight
        self.listbox = tk.Listbox(
            list_frame,
            font=("Arial", 11),
            borderwidth=0,
            highlightthickness=1,
            highlightcolor="#d1d5db",
            highlightbackground="#d1d5db",
            activestyle="none",
            bg="#ffffff",
            fg="#111827",
            selectbackground="#2563eb",
            selectforeground="#ffffff",
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        #user clicks an account row, and it will update the detail label (updated to change)
        self.listbox.bind("<<ListboxSelect>>", self._on_account_select)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.configure(yscrollcommand=scrollbar.set)

        detail_label = ttk.Label(list_section, textvariable=self.detail_var, style="Status.TLabel")
        detail_label.pack(anchor="w", pady=(10, 0))

        status = ttk.Label(card, textvariable=self.status_var, style="Status.TLabel")
        status.pack(anchor="w", pady=(12, 0))

    def load_accounts(self):
        # Handler for the "Load Accounts" button: asks the service for accounts,
        # then populates the listbox with account names.
        self.listbox.delete(0, tk.END)
        self._loaded_accounts = []
        self.detail_var.set("Select an account in the list to see its balance.")

        accounts = self.service.get_account(None)
        if not accounts:
            self.status_var.set("No accounts found.")
            return

        self._loaded_accounts = list(accounts)
        for acc in accounts:
            label = getattr(acc, "name", str(acc))
            self.listbox.insert(tk.END, label)

        self.status_var.set(f"Loaded {len(accounts)} account(s).")

    def _on_account_select(self, _event=None):
        #loaded Account object and show basic info (name + balance).
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = int(sel[0])
        if idx < 0 or idx >= len(self._loaded_accounts):
            return
        acc = self._loaded_accounts[idx]
        name = getattr(acc, "name", str(acc))
        balance = getattr(acc, "balance", None)
        if balance is not None:
            self.detail_var.set(f"Selected: {name}   —   Balance: ${float(balance):,.2f}")
        else:
            self.detail_var.set(f"Selected: {name}")
