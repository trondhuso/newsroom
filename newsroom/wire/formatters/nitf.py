
from lxml import etree
from superdesk.publish.formatters.nitf_formatter import NITFFormatter as SuperdeskNITFFormatter

from .base import BaseFormatter


class NITFFormatter(BaseFormatter):

    MIMETYPE = 'application/xml'
    FILE_EXTENSION = 'xml'

    encoding = 'utf-8'
    formatter = SuperdeskNITFFormatter()

    def format_item(self, item, item_type='items'):
        dest = {}
        nitf = self.formatter.get_nitf(item, dest, '')
        return etree.tostring(nitf, xml_declaration=True, pretty_print=True, encoding=self.encoding)
