import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Hardcoded data for demonstration
subscriptions = {
    "Subscription 1": [
        {"name": "Hamna", "roles": ["Admin"], "resources": ["Resource A"]},
        {"name": "Ali", "roles": ["Viewer"], "resources": ["Resource B"]},
        {"name": "Sara", "roles": ["Editor"], "resources": ["Resource E"]},
        {"name": "Zara", "roles": ["Viewer"], "resources": ["Resource F"]},
    ],
    "Subscription 2": [
        {"name": "Omar", "roles": ["Viewer"], "resources": ["Resource C"]},
        {"name": "Ahmed", "roles": ["Admin"], "resources": ["Resource D"]},
        {"name": "Amna", "roles": ["Admin"], "resources": ["Resource G"]},
        {"name": "Lina", "roles": ["Viewer"], "resources": ["Resource H"]},
    ],
    "Subscription 3": [
        {"name": "Noor", "roles": ["Viewer"], "resources": ["Resource I"]},
        {"name": "Hadi", "roles": ["Admin"], "resources": ["Resource J"]},
    ],
    "Subscription 4": [
        {"name": "Hassan", "roles": ["Viewer"], "resources": ["Resource K"]},
        {"name": "Mona", "roles": ["Admin"], "resources": ["Resource L"]},
    ],
    "Subscription 5": [
        {"name": "Ayla", "roles": ["Viewer"], "resources": ["Resource M"]},
        {"name": "Khan", "roles": ["Admin"], "resources": ["Resource N"]},
        {"name": "Saba", "roles": ["Viewer"], "resources": ["Resource O"]},
        {"name": "Tina", "roles": ["Admin"], "resources": ["Resource P"]},
    ],
     "Subscription 6": [
        {"name": "John", "roles": ["Admin"], "resources": ["Resource X"]},
        {"name": "Jane", "roles": ["Viewer"], "resources": ["Resource Y"]},
        {"name": "Doe", "roles": ["Editor"], "resources": ["Resource Z"]},
    ],
    "Subscription 7": [
        {"name": "Michael", "roles": ["Viewer"], "resources": ["Resource P"]},
        {"name": "Emily", "roles": ["Admin"], "resources": ["Resource Q"]},
        {"name": "Chris", "roles": ["Viewer"], "resources": ["Resource R"]},
    ],
    "Subscription 8": [
        {"name": "Sophia", "roles": ["Viewer"], "resources": ["Resource S"]},
        {"name": "William", "roles": ["Admin"], "resources": ["Resource T"]},
        {"name": "Olivia", "roles": ["Admin"], "resources": ["Resource U"]},
    ],
    "Subscription 9": [
        {"name": "Ethan", "roles": ["Viewer"], "resources": ["Resource V"]},
        {"name": "Isabella", "roles": ["Admin"], "resources": ["Resource W"]},
    ],
    "Subscription 10": [
        {"name": "Alexander", "roles": ["Viewer"], "resources": ["Resource X"]},
        {"name": "Ava", "roles": ["Admin"], "resources": ["Resource Y"]},
        {"name": "Mia", "roles": ["Editor"], "resources": ["Resource Z"]},
    ],
    "Subscription 11": [
        {"name": "Luke", "roles": ["Admin"], "resources": ["Resource A1"]},
        {"name": "Leia", "roles": ["Viewer"], "resources": ["Resource B1"]},
        {"name": "Han", "roles": ["Editor"], "resources": ["Resource C1"]},
    ],
    "Subscription 12": [
        {"name": "Rey", "roles": ["Viewer"], "resources": ["Resource D1"]},
        {"name": "Kylo", "roles": ["Admin"], "resources": ["Resource E1"]},
        {"name": "Finn", "roles": ["Viewer"], "resources": ["Resource F1"]},
    ],
    "Subscription 13": [
        {"name": "Poe", "roles": ["Viewer"], "resources": ["Resource G1"]},
        {"name": "Rose", "roles": ["Admin"], "resources": ["Resource H1"]},
        {"name": "Chewbacca", "roles": ["Admin"], "resources": ["Resource I1"]},
    ],
    "Subscription 14": [
        {"name": "Yoda", "roles": ["Viewer"], "resources": ["Resource J1"]},
        {"name": "Obi-Wan", "roles": ["Admin"], "resources": ["Resource K1"]},
    ],
    "Subscription 15": [
        {"name": "Anakin", "roles": ["Viewer"], "resources": ["Resource L1"]},
        {"name": "Padmé", "roles": ["Admin"], "resources": ["Resource M1"]},
        {"name": "Darth Vader", "roles": ["Editor"], "resources": ["Resource N1"]},
    ]
}

roles = ["Admin", "Viewer", "Editor"]
resources = ["Resource A", "Resource B", "Resource C", "Resource D", "Resource E", "Resource F", "Resource G", "Resource H", "Resource I", "Resource J", "Resource K", "Resource L", "Resource M", "Resource N", "Resource O", "Resource P"]

class AzureUserManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Azure User Manager")
        self.geometry("1000x600")

        # Main frames
        self.left_frame = ttk.Frame(self, padding="10")
        self.left_frame.grid(row=1, column=0, sticky="ns")
        self.right_frame = ttk.Frame(self, padding="10")
        self.right_frame.grid(row=1, column=1, sticky="nsew")

        # Title
        title_label = ttk.Label(self, text="Azure User Manager", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Subscription checkboxes
        ttk.Label(self.left_frame, text="Subscriptions").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.subscription_vars = {}
        for idx, subscription in enumerate(subscriptions.keys()):
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(self.left_frame, text=subscription, variable=var, command=self.on_subscription_select)
            chk.grid(row=idx + 1, column=0, padx=5, pady=5, sticky="w")
            self.subscription_vars[subscription] = var

        # User list
        ttk.Label(self.right_frame, text="Users").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.user_var = tk.StringVar(value=[])
        self.user_listbox = tk.Listbox(self.right_frame, listvariable=self.user_var, selectmode=tk.SINGLE)
        self.user_listbox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.user_listbox.bind("<<ListboxSelect>>", self.on_user_select)

        # Scrollbar for user list
        self.user_scrollbar = ttk.Scrollbar(self.right_frame, orient="vertical", command=self.user_listbox.yview)
        self.user_scrollbar.grid(row=1, column=1, sticky="ns")
        self.user_listbox.config(yscrollcommand=self.user_scrollbar.set)

        # Buttons for user operations
        add_user_btn = ttk.Button(self.right_frame, text="Add User", command=self.add_user)
        add_user_btn.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        edit_user_btn = ttk.Button(self.right_frame, text="Edit User", command=self.edit_user)
        edit_user_btn.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        delete_user_btn = ttk.Button(self.right_frame, text="Delete User", command=self.delete_user)
        delete_user_btn.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        # Role management
        manage_roles_btn = ttk.Button(self.right_frame, text="Manage Roles", command=self.manage_roles)
        manage_roles_btn.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

        # Resource management
        manage_resources_btn = ttk.Button(self.right_frame, text="Manage Resources", command=self.manage_resources)
        manage_resources_btn.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

        # Search filter
        ttk.Label(self.right_frame, text="Search Users").grid(row=7, column=0, padx=5, pady=5, sticky="w")

        # Dropdown for search criteria
        self.search_criteria_var = tk.StringVar(value="Name")
        self.search_criteria_menu = ttk.Combobox(self.right_frame, textvariable=self.search_criteria_var, values=["Name", "Role", "Both"])
        self.search_criteria_menu.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

        # Search entry
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.right_frame, textvariable=self.search_var)
        self.search_entry.grid(row=9, column=0, padx=5, pady=5, sticky="ew")
        self.search_entry.bind("<KeyRelease>", self.on_search)
        self.search_entry.bind("<FocusIn>", self.clear_placeholder)
        self.search_entry.bind("<FocusOut>", self.set_placeholder)

        # Set initial placeholder text
        self.set_placeholder(None)

    def set_placeholder(self, event):
        if not self.search_var.get():
            self.search_entry.insert(0, "Search any user...")
            self.search_entry.config(foreground='grey')

    def clear_placeholder(self, event):
        if self.search_entry.get() == "Search any user...":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(foreground='black')

    def on_subscription_select(self):
        selected_subscriptions = [sub for sub, var in self.subscription_vars.items() if var.get()]
        if selected_subscriptions:
            self.update_user_list(selected_subscriptions)

    def update_user_list(self, selected_subscriptions):
        users = []
        for subscription in selected_subscriptions:
            users.extend(subscriptions[subscription])
        self.user_var.set([f"{user['name']} ({', '.join(user['roles'])})" for user in users])

    def on_user_select(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            user_info = event.widget.get(index)
            user_name = user_info.split(' (')[0]
            self.show_user_details(user_name)

    def show_user_details(self, user_name):
        for subscription, users in subscriptions.items():
            for user in users:
                if user["name"] == user_name:
                    roles = ', '.join(user["roles"])
                    resources = ', '.join(user["resources"])
                    messagebox.showinfo(f"User Details - {user_name}", f"Roles: {roles}\nResources: {resources}")
                    return

    def on_search(self, event):
        search_text = self.search_var.get().lower()
        search_criteria = self.search_criteria_var.get().lower()
        all_users = [user for sub in subscriptions.values() for user in sub]

        if search_criteria == "name":
            filtered_users = [user for user in all_users if search_text in user["name"].lower()]
            filtered_users.sort(key=lambda x: x["name"].lower())
        elif search_criteria == "role":
            filtered_users = [user for user in all_users if any(search_text in role.lower() for role in user["roles"])]
            filtered_users.sort(key=lambda x: ', '.join(x["roles"]).lower())
        elif search_criteria == "both":
            filtered_users = [user for user in all_users if search_text in user["name"].lower() or any(search_text in role.lower() for role in user["roles"])]
            filtered_users.sort(key=lambda x: (x["name"].lower(), ', '.join(x["roles"]).lower()))

        self.user_var.set([f"{user['name']} ({', '.join(user['roles'])})" for user in filtered_users])

    def add_user(self):
        subscription = self.get_selected_subscription()
        if not subscription:
            messagebox.showerror("Error", "Please select a subscription to add a user.")
            return

        name = simpledialog.askstring("Input", "Enter user name:")
        if not name:
            return

        roles = self.select_roles()
        resources = self.select_resources()

        if roles and resources:
            subscriptions[subscription].append({"name": name, "roles": roles, "resources": resources})
            self.update_user_list([subscription])

    def edit_user(self):
        subscription = self.get_selected_subscription()
        if not subscription:
            messagebox.showerror("Error", "Please select a subscription.")
            return

        selected_user = self.get_selected_user()
        if not selected_user:
            messagebox.showerror("Error", "Please select a user to edit.")
            return

        new_name = simpledialog.askstring("Input", "Edit user name:", initialvalue=selected_user["name"])
        new_roles = self.select_roles(initial_roles=selected_user["roles"])
        new_resources = self.select_resources(initial_resources=selected_user["resources"])

        if new_name and new_roles and new_resources:
            selected_user["name"] = new_name
            selected_user["roles"] = new_roles
            selected_user["resources"] = new_resources
            self.update_user_list([subscription])

    def delete_user(self):
        subscription = self.get_selected_subscription()
        if not subscription:
            messagebox.showerror("Error", "Please select a subscription.")
            return

        selected_user = self.get_selected_user()
        if not selected_user:
            messagebox.showerror("Error", "Please select a user to delete.")
            return

        if messagebox.askyesno("Confirm", f"Are you sure you want to delete user {selected_user['name']}?"):
            subscriptions[subscription].remove(selected_user)
            self.update_user_list([subscription])
    def manage_roles(self):
        subscription = self.get_selected_subscription()
        if not subscription:
            messagebox.showerror("Error", "Please select a subscription.")
            return

        selected_user = self.get_selected_user()
        if not selected_user:
            messagebox.showerror("Error", "Please select a user.")
            return

        # Dialog for managing roles
        roles_win = tk.Toplevel(self)
        roles_win.title(f"Manage Roles for {selected_user['name']} in {subscription}")

        # Current roles
        ttk.Label(roles_win, text="Current Roles:").pack(anchor='w')
        current_roles_frame = ttk.Frame(roles_win)
        current_roles_frame.pack(pady=5, anchor='w')

        for role in selected_user["roles"]:
            ttk.Label(current_roles_frame, text=role).pack(anchor='w')

        # Add new role
        def add_role():
            new_role = simpledialog.askstring("Add Role", "Enter new role:")
            if new_role and new_role not in selected_user["roles"]:
                selected_user["roles"].append(new_role)
                update_roles_list()

        # Edit role
        def edit_role():
            selected_role = roles_listbox.get(tk.ACTIVE)
            if selected_role:
                new_role_name = simpledialog.askstring("Edit Role", "Edit role name:", initialvalue=selected_role)
                if new_role_name and new_role_name != selected_role:
                    selected_user["roles"][selected_user["roles"].index(selected_role)] = new_role_name
                    update_roles_list()

        # Delete role
        def delete_role():
            selected_role = roles_listbox.get(tk.ACTIVE)
            if selected_role:
                if messagebox.askyesno("Confirm", f"Are you sure you want to delete role '{selected_role}'?"):
                    selected_user["roles"].remove(selected_role)
                    update_roles_list()

        # Roles listbox
        ttk.Label(roles_win, text="Roles:").pack(anchor='w')
        roles_var = tk.StringVar(value=selected_user["roles"])
        roles_listbox = tk.Listbox(roles_win, listvariable=roles_var)
        roles_listbox.pack(pady=5, anchor='w')

        # Buttons for managing roles
        ttk.Button(roles_win, text="Add Role", command=add_role).pack(pady=5, anchor='w')
        ttk.Button(roles_win, text="Edit Role", command=edit_role).pack(pady=5, anchor='w')
        ttk.Button(roles_win, text="Delete Role", command=delete_role).pack(pady=5, anchor='w')

        # Update roles list function
        def update_roles_list():
            roles_var.set(selected_user["roles"])
            self.update_user_list([subscription])

        # Wait for window to close
        self.wait_window(roles_win)
        
    def manage_resources(self):
        subscription = self.get_selected_subscription()
        if not subscription:
            messagebox.showerror("Error", "Please select a subscription.")
            return

        selected_user = self.get_selected_user()
        if not selected_user:
            messagebox.showerror("Error", "Please select a user.")
            return

        # Dialog for managing resources
        resources_win = tk.Toplevel(self)
        resources_win.title(f"Manage Resources for {selected_user['name']} in {subscription}")

        # Current resources
        ttk.Label(resources_win, text="Current Resources:").pack(anchor='w')
        current_resources_frame = ttk.Frame(resources_win)
        current_resources_frame.pack(pady=5, anchor='w')

        for resource in selected_user["resources"]:
            ttk.Label(current_resources_frame, text=resource).pack(anchor='w')

        # Add new resource
        def add_resource():
            new_resource = simpledialog.askstring("Add Resource", "Enter new resource:")
            if new_resource and new_resource not in selected_user["resources"]:
                selected_user["resources"].append(new_resource)
                update_resources_list()

        # Edit resource
        def edit_resource():
            selected_resource = resources_listbox.get(tk.ACTIVE)
            if selected_resource:
                new_resource_name = simpledialog.askstring("Edit Resource", "Edit resource name:", initialvalue=selected_resource)
                if new_resource_name and new_resource_name != selected_resource:
                    selected_user["resources"][selected_user["resources"].index(selected_resource)] = new_resource_name
                    update_resources_list()

        # Delete resource
        def delete_resource():
            selected_resource = resources_listbox.get(tk.ACTIVE)
            if selected_resource:
                if messagebox.askyesno("Confirm", f"Are you sure you want to delete resource '{selected_resource}'?"):
                    selected_user["resources"].remove(selected_resource)
                    update_resources_list()

        # Resources listbox
        ttk.Label(resources_win, text="Resources:").pack(anchor='w')
        resources_var = tk.StringVar(value=selected_user["resources"])
        resources_listbox = tk.Listbox(resources_win, listvariable=resources_var)
        resources_listbox.pack(pady=5, anchor='w')

        # Buttons for managing resources
        ttk.Button(resources_win, text="Add Resource", command=add_resource).pack(pady=5, anchor='w')
        ttk.Button(resources_win, text="Edit Resource", command=edit_resource).pack(pady=5, anchor='w')
        ttk.Button(resources_win, text="Delete Resource", command=delete_resource).pack(pady=5, anchor='w')

        # Update resources list function
        def update_resources_list():
            resources_var.set(selected_user["resources"])
            self.update_user_list([subscription])

        # Wait for window to close
        self.wait_window(resources_win)
        
    def get_selected_subscription(self):
        for subscription, var in self.subscription_vars.items():
            if var.get():
                return subscription
        return None

    def get_selected_user(self):
        selection = self.user_listbox.curselection()
        if not selection:
            return None
        index = selection[0]
        user_info = self.user_listbox.get(index)
        user_name = user_info.split(' (')[0]
        subscription = self.get_selected_subscription()
        for user in subscriptions[subscription]:
            if user["name"] == user_name:
                return user
        return None

    def select_roles(self, initial_roles=None):
        roles_win = tk.Toplevel(self)
        roles_win.title("Select Roles")
        selected_roles = []

        def submit():
            nonlocal selected_roles
            selected_roles = [role for role, var in role_vars.items() if var.get()]
            roles_win.destroy()

        role_vars = {}
        for role in roles:
            var = tk.BooleanVar(value=(role in initial_roles if initial_roles else False))
            chk = ttk.Checkbutton(roles_win, text=role, variable=var)
            chk.pack(anchor='w')
            role_vars[role] = var

        ttk.Button(roles_win, text="Submit", command=submit).pack()
        self.wait_window(roles_win)
        return selected_roles

    def select_resources(self, initial_resources=None):
        resources_win = tk.Toplevel(self)
        resources_win.title("Select Resources")
        selected_resources = []

        def submit():
            nonlocal selected_resources
            selected_resources = [resource for resource, var in resource_vars.items() if var.get()]
            resources_win.destroy()

        resource_vars = {}
        for resource in resources:
            var = tk.BooleanVar(value=(resource in initial_resources if initial_resources else False))
            chk = ttk.Checkbutton(resources_win, text=resource, variable=var)
            chk.pack(anchor='w')
            resource_vars[resource] = var

        ttk.Button(resources_win, text="Submit", command=submit).pack()
        self.wait_window(resources_win)
        return selected_resources

if __name__ == "__main__":
    app = AzureUserManagerApp()
    app.mainloop()
