class Invoice:
    """Class modelled after EDI++ file structure."""
    header = {
        "document_type": "FZ",
        "document_status": 1,
        "tax_registeration_status_code": 0,
        "document_number": 0,
        "suppliers_document_number": "",
        "document_number_users_extension": "",
        "document_number_full": "",
        "corrected_document_number": "",
        "corrected_document_date": "",
        "order_id": "",
        "target_warehouse": "",
        "contractor_id": "",
        "contractor_name_short": "",
        "contractor_name_full": "",
        "contractor_city": "",
        "contractor_zip_code": "",
        "contractor_address": "",
        "contractor_tax_id": "",
        "document_category": "",
        "document_subcategory": "",
        "issue_location": "",
        "issue_date": "",
        "sale_date": "",
        "receipt_date": "",
        "number_of_entries": 0,
        "net_prices": True,
        "active_price": "netto",
        "net_value": 0.0,
        "vat_value": 0.0,
        "gross_value": 0.0,
        "cost": 0.0,
        "discount_name": "",
        "discount_percentage": 0.0,
        "payment_method": "",
        "payment_due": "",
        "amount_paid_upon_receipt": "",
        "amount_left_to_pay": 0.0,
        "value_rounding_method": 0,  # TODO: Choice
        "vat_rounding_method": 0,  # TODO: Choice
        "vat_autocalculation": 1,
        "special_or_extended_document_status": 0,
        "issuer_name": "",
        "recipient_name": "",
        "basis_for_issue": "",
        "issued_packaging_value": 0.0,
        "returned_packaging_value": 0.0,
        "currency": "PLN",
        "exchange_rate": 1.0,
        "remarks": "",
        "comments": "",
        "document_subtitle": "",
        "unused": "",
        "document_import_status": 0,
        "export_document": False,
        "transaction_type": 0,
        "card_payment_name": "",
        "card_payment_amount": 0.0,
        "credit_payment_name": "",
        "credit_payment_amount": 0.0,
        "contractor_country": "Polska",
        "contractor_country_prefix": "PL",
        "contractor_eu_membership": True
    }
    body = list()


    def to_epp(self):
        result = ""
        result += "[NAGLOWEK]"
        result += "\n"
        result += ",".join([str(self.header[k]) if not isinstance(self.header[k], bool) else {False: '0', True: '1'}[self.header[k]] for k in self.header])
        result += "\n\n"
        result += "[ZAWARTOSC]"
        result += "\n"
        for item in self.body:
            result += ",".join([str(item[k]) for k in item])
            result += "\n"
        result += "\n\n"
        return result
