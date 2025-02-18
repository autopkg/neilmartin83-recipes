import os
import xml.etree.ElementTree as ET
from autopkglib import Processor, ProcessorError  # AutoPkg base classes

__all__ = ["AddXMLTagProcessor"]

class AddXMLTagProcessor(Processor):
    """
    AutoPkg processor that adds a new XML tag inside a specified parent element.
    """
    description = __doc__
    input_variables = {
        "input_path": {
            "required": True,
            "description": "Path to the XML file to modify."
        },
        "parent_xpath": {
            "required": True,
            "description": "XPath of the parent element where the new tag will be added."
        },
        "new_element": {
            "required": True,
            "description": "Name of the new XML tag to add."
        },
        "text": {
            "required": False,
            "description": "Optional text content for the new tag."
        }
    }
    
    output_variables = {}
    
    def main(self):
        input_path = self.env["input_path"]
        parent_xpath = self.env["parent_xpath"]
        new_element = self.env["new_element"]
        text = self.env.get("text", "")
        
        if not os.path.exists(input_path):
            raise ProcessorError(f"XML file not found: {input_path}")
        
        # Load the XML file
        tree = ET.parse(input_path)
        root = tree.getroot()
        
        # Find the parent element
        parent = root.find(parent_xpath)
        if parent is None:
            raise ProcessorError(f"Parent element not found for XPath: {parent_xpath}")
        
        # Create the new element
        new_tag = ET.Element(new_element)
        new_tag.text = text
        
        # Append the new element
        parent.append(new_tag)
        
        # Save the modified XML
        tree.write(input_path, encoding="UTF-8", xml_declaration=True)
        
        self.output(f"Added <{new_element}> to {parent_xpath} in {input_path}")

if __name__ == "__main__":
    processor = AddXMLTagProcessor()
    processor.execute_shell()
