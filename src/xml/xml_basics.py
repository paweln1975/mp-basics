"""
lxml library training
>>> import sys; sys.tracebacklimit = 0
>>> from lxml import etree
>>> xml_string = "<a><b>hello</b></a>"
>>> v = return_type(xml_string)
>>> v
<class 'lxml.etree._Element'>

>>> dump_xml(xml_string)
<a>
  <b>hello</b>
</a>

>>> text_xml ='<country>' \
'<name>United Stated of America</name>' \
'<capital>Washington</capital>' \
'    <states>' \
'      <state size="70">California</state>' \
'      <state size="170">Texas</state>' \
'      <state size="270">Florida</state>' \
'      <state size="370">Hawaii</state>' \
'   </states>' \
'</country>'
>>> accessing_attributes(text_xml)
<capital>Washington</capital>
California 70
Texas 170
Florida 270
Hawaii 370

>>> text_xml = '<a attr="123"><b>hello</b><c/></a>'
>>> print(get_attr_value(text_xml, 'attr'))
uu123
>>> text_xml = '<root a1="aba" a2="caba"/>'
>>> print(get_attr_value(text_xml, 'a3'))
None

"""
from lxml import etree



def return_type(s: str):
    root = etree.fromstring(s)
    return type(root)  #

def dump_xml(s: str):
    root = etree.fromstring(s)
    return etree.dump(root)

def accessing_attributes(s: str):
    root = etree.fromstring(s)
    etree.dump(root[1], pretty_print=True, with_tail=False)
    states = root[2]
    for state in states:
        print(state.text, state.get('size'))


def get_attr_value(xml_str: str, attr_name: str) -> str:
    root = etree.fromstring(xml_str)
    return root.get(attr_name)