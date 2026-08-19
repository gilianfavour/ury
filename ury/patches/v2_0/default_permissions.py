import frappe
from ury.permissions import apply_default_permissions


def execute():
	print("Configuring ury role permissions...")
	apply_default_permissions()
	frappe.clear_cache()
