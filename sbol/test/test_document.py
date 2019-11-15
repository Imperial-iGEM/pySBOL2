import unittest
from sbol.document import *
from sbol.moduledefinition import *
from sbol.componentdefinition import *
from sbol.constants import *


MODULE_LOCATION = os.path.dirname(os.path.abspath(__file__))
TEST_LOCATION = os.path.join(MODULE_LOCATION, 'resources', 'crispr_example.xml')


class TestDocument(unittest.TestCase):

    def test_empty_len0(self):
        doc = Document()
        # print(doc)
        self.assertEqual(0, len(doc), "Length of document should be 0")

    def test_addGetTopLevel_uri(self):
        doc = Document()
        # Tutorial doesn't drop final forward slash, but this isn't right.
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        cas9 = ComponentDefinition('Cas9', BIOPAX_PROTEIN)
        doc.addModuleDefinition(crispr_template)
        doc.addComponentDefinition(cas9)

        # Note: tutorial has 1.0.0 instead of 1 but this doesn't work
        crispr_template_2 = doc.getModuleDefinition('http://sbols.org/CRISPR_Example/CRISPR_Template/1')
        cas9_2 = doc.getComponentDefinition('http://sbols.org/CRISPR_Example/Cas9/1')
        self.assertEqual(crispr_template, crispr_template_2)
        self.assertEqual(cas9, cas9_2)

    def test_addGetTopLevel_displayId(self):
        doc = Document()
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        cas9 = ComponentDefinition('Cas9', BIOPAX_PROTEIN)
        doc.addModuleDefinition(crispr_template)
        doc.addComponentDefinition(cas9)

        crispr_template_2 = doc.moduleDefinitions['CRISPR_Template']
        cas9_2 = doc.componentDefinitions['Cas9']
        self.assertEqual(crispr_template, crispr_template_2)
        self.assertEqual(cas9, cas9_2)

    def test_addGetTopLevel_indexing(self):
        doc = Document()
        # Tutorial doesn't drop final forward slash, but this isn't right.
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        cas9 = ComponentDefinition('Cas9', BIOPAX_PROTEIN)
        doc.addModuleDefinition(crispr_template)
        doc.addComponentDefinition(cas9)

        crispr_template_2 = doc.moduleDefinitions[0]
        cas9_2 = doc.componentDefinitions[0]
        self.assertEqual(crispr_template, crispr_template_2)
        self.assertEqual(cas9, cas9_2)

    def test_iteration(self):
        doc = Document()
        doc.read(TEST_LOCATION)
        i = 0
        for obj in doc:
            i += 1
            print(obj)
        self.assertEqual(len(doc), 31)
        # print(doc)

    def test_identity(self):
        # The sbol:identity relation should not be written out when
        # serializing SBOL.
        doc = Document()
        doc.read(TEST_LOCATION)
        result = doc.writeString()
        self.assertNotIn('sbol:identity', result)


if __name__ == '__main__':
    unittest.main()
