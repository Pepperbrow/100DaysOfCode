# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:22:39 2021

@author: peppe
"""
#wire protocol.  Internal rep is serialised in XML (or JSON), which can then be read by different language
#eXtensible Markup Language
#XML Schema is description of legal format of XML doc.  Example of XML:
<Person>
    <firstName>
        Simon
    </firstName>
    <lastName>
        Williams
    </lastName>
    <age>
        402
    </age>
</person>

#Element Tree allows search of XML
#Triple quoted strings ''' are strings that are over several lines

import xml.etree.ElementTree as ET
data = '''<person>
  <name>Simon</name>
  <phone type="intl">
      +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))

#Whilst XML is good for rich, hierarchical documents, JSON (Javascript Object Notation) is good for quick and dirty data extraction.

import json # JSON module
data = '''{
    "name" : "Simon",
    "phone" : {
      "type" : "intl",
      "number" : "+1 734 303 4456"
    },
    "email" : {
            "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name: ',info["name"])
print('Hide:',info["email"]["hide"])    