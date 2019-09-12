import unittest
from sbol.moduledefinition import ModuleDefinition
from sbol.componentdefinition import ComponentDefinition
from sbol.document import Document
from sbol.property import LiteralProperty


class TestExtensions(unittest.TestCase):

    def testExtensionClass(self):
        class ModuleDefinitionExtension(ModuleDefinition):
            def __init__(self, id = 'example'):
                ModuleDefinition.__init__(self, id)
                id_x = 'http://dnaplotlib.org#xCoordinate'
                id_y = 'http://dnaplotlib.org#yCoordinate'
                # Initialize property value to 10
                self.x_coordinate = LiteralProperty(id_x, '0', '1', '10')
                # Initialize property value to 10
                self.y_coordinate = LiteralProperty(id_y, '0', '1', 10)

        doc = Document()
        doc.addNamespace('http://dnaplotlib.org#', 'dnaplotlib')
        md = ModuleDefinitionExtension('md_example')
        md_id = md.identity
        md.y_coordinate = 5
        self.assertEquals(md.x_coordinate, '10')
        self.assertEquals(md.y_coordinate, 5)
        doc.addExtensionObject(md)
        # TODO we might want to use a second document here...
        doc.readString(doc.writeString())
        md = doc.getExtensionObject(md_id)
        self.assertEquals(md.x_coordinate, '10')
        self.assertEquals(md.y_coordinate, 5)

    def test_add_custom_annotation(self):
        # Based on pySBOL slide deck from Bryan
        cd = ComponentDefinition('cd0')
        cd_id = 'http://sys-bio.org#annotationProperty'
        cd.annotation = LiteralProperty(cd, cd_id, '0', '1')
        cd.annotation.set('This is a test property')
        doc = Document()
        doc.add(cd)
        doc1 = Document()
        doc1.readString(doc.writeString())
        cd1 = doc1.get(cd_id)
        self.assertEquals('This is a test property', cd1.annotation)

