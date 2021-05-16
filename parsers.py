from datetime import datetime as dt
from Invoice import Invoice
import xml.etree.ElementTree as ET
from utils import date_parser, datetime_parser, date_to_str, datetime_to_str, quote


def parser_1(document):
    invoice_list = []
    metadata = dict()
    metadata["communication_date"] = date_to_str(date_parser(document.attrib["Date"]))
    for invoice in document:
        
        for entry in invoice.findall("InvoiceLine"):
            invoice.body.append(
                    
            )        
        invoice.header["number_of_entries"] = len(invoice.body)

    return metadata, invoice_list


def parser_2(document):
    invoice_list = []
    metadata = dict()
    metadata["communication_date"] = date_to_str(datetime_parser(document.attrib["date"]))
    for item in document:
        invoice = Invoice()
        invoice.header["suppliers_document_number"] = quote(item.find("inv_number_string").text)
        invoice.header["document_number_full"] = quote(item.find("inv_number_string").text)
        invoice.header["net_value"] = item.find("inv_price_net").text
        invoice.header["vat_value"] = item.find("inv_tax").text
        invoice.header["gross_value"] = item.find("inv_price").text
        invoice.header["issue_date"] = item.find("inv_date").text
        invoice.header["sale_date"] = item.find("inv_sell_date").text
        invoice.header["contractor_name_short"] = quote(item.find("inv_bill_company").text)
        invoice.header["contractor_name_full"] = quote(item.find("inv_bill_company").text)
        invoice.header["contractor_tax_id"] = quote(item.find("inv_bill_vat").text) if item.find("inv_bill_vat").text else None
        invoice.header["contractor_city"] = quote(item.find("inv_bill_city").text)
        invoice.header["contractor_country"] = quote(item.find("inv_bill_country").text)
        invoice.header["contractor_address"] = quote(item.find("inv_bill_street").text)
        invoice.header["contractor_zip_code"] = quote(item.find("inv_bill_code").text)
        invoice_list.append(invoice)
    return metadata, invoice_list
