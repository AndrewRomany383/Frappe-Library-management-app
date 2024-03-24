# Copyright (c) 2024, Andrew Romany and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class LibraryMember(Document):

	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"
