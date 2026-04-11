#!/usr/bin/env python3
"""
AUGMANITAI TBX TermBase eXchange Export Generator
Converts AUGMANITAI terminology data to ISO 30042 TBX-Core XML format

Creator: Andreas Ehstand
License: CC BY-NC-ND 4.0
Standards: ISO 30042, ISO 704, ISO 1087
"""

import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
from pathlib import Path
import sys


class AugmanitaiTBXGenerator:
    """Generates TBX-Core XML from AUGMANITAI term data."""

    def __init__(self, terms_json_path, multilingual_json_path=None):
        """
        Initialize TBX generator with term data sources.

        Args:
            terms_json_path: Path to augmanitai/data/terms.json
            multilingual_json_path: Path to augmanitai_multilingual.json (optional)
        """
        self.terms_json_path = Path(terms_json_path)
        self.multilingual_json_path = Path(multilingual_json_path) if multilingual_json_path else None
        self.terms = {}
        self.multilingual = {}
        self.load_data()

    def load_data(self):
        """Load term and multilingual data from JSON sources."""
        try:
            with open(self.terms_json_path, 'r', encoding='utf-8') as f:
                self.terms = json.load(f)
            print(f"Loaded {len(self.terms)} terms from {self.terms_json_path}")
        except FileNotFoundError:
            print(f"Error: {self.terms_json_path} not found")
            sys.exit(1)

        if self.multilingual_json_path and self.multilingual_json_path.exists():
            try:
                with open(self.multilingual_json_path, 'r', encoding='utf-8') as f:
                    self.multilingual = json.load(f)
                print(f"Loaded multilingual data from {self.multilingual_json_path}")
            except Exception as e:
                print(f"Warning: Could not load multilingual data: {e}")

    def create_tbx_root(self):
        """Create TBX document root element with metadata."""
        root = ET.Element('martif')
        root.set('type', 'TBX-Core')
        root.set('xml:lang', 'en')

        # TBX file header metadata
        header = ET.SubElement(root, 'teiHeader')
        file_desc = ET.SubElement(header, 'fileDesc')

        title_stmt = ET.SubElement(file_desc, 'titleStmt')
        title = ET.SubElement(title_stmt, 'title')
        title.text = 'AUGMANITAI Terminology Database'

        note = ET.SubElement(title_stmt, 'note')
        note.text = 'Complete AUGMANITAI term definitions, characteristics, and multilingual coverage'
        note.set('type', 'description')

        pub_stmt = ET.SubElement(file_desc, 'publicationStmt')
        pub_place = ET.SubElement(pub_stmt, 'p')
        pub_place.text = 'AUGMANITAI Project'

        source_desc = ET.SubElement(file_desc, 'sourceDesc')
        src_p = ET.SubElement(source_desc, 'p')
        src_p.text = f'Generated from augmanitai/data/terms.json on {datetime.now().isoformat()}'

        # Encoding description
        encoding_desc = ET.SubElement(header, 'encodingDesc')
        p = ET.SubElement(encoding_desc, 'p')
        p.text = 'ISO 30042 TBX-Core format'

        # Profile description
        profile_desc = ET.SubElement(header, 'profileDesc')
        lang_usage = ET.SubElement(profile_desc, 'langUsage')

        languages = ['en', 'de', 'zh', 'hi', 'ar']
        for lang in languages:
            lang_elem = ET.SubElement(lang_usage, 'langUsage')
            lang_elem.set('xml:lang', lang)
            lang_elem.text = {'en': 'English', 'de': 'German', 'zh': 'Mandarin Chinese',
                             'hi': 'Hindi', 'ar': 'Arabic'}.get(lang, lang)

        # Revision history
        rev_desc = ET.SubElement(header, 'revisionDesc')
        change = ET.SubElement(rev_desc, 'change')
        change.set('when', datetime.now().isoformat())
        change.text = 'Initial TBX export from AUGMANITAI terminology database'

        return root, header

    def add_conceptual_entry(self, text, term_data):
        """Create termEntry (conceptEntry) element for a term."""
        term_entry = ET.Element('termEntry')
        term_entry.set('id', term_data.get('abbreviation', term_data.get('name', '')).replace(' ', '_'))

        # Conceptual metadata
        descrip = ET.SubElement(term_entry, 'descrip')
        descrip.set('type', 'definition')
        descrip.set('xml:lang', 'en')
        descrip.text = term_data.get('definition', 'No definition available')

        # ISO 704 Characteristics
        if 'iso704_characteristics' in term_data:
            for char in term_data.get('iso704_characteristics', []):
                char_elem = ET.SubElement(term_entry, 'descrip')
                char_elem.set('type', 'iso704Characteristic')
                char_elem.text = char

        # Domain classification
        if 'domain' in term_data:
            domain_elem = ET.SubElement(term_entry, 'descrip')
            domain_elem.set('type', 'domain')
            domain_elem.text = term_data['domain']

        # Creator attribution
        if 'creator' in term_data:
            creator_elem = ET.SubElement(term_entry, 'admin')
            creator_elem.set('type', 'origination')
            creator_elem.text = term_data['creator']

        # License
        license_elem = ET.SubElement(term_entry, 'admin')
        license_elem.set('type', 'license')
        license_elem.text = term_data.get('license', 'CC BY-NC-ND 4.0')

        # Creation date
        created_elem = ET.SubElement(term_entry, 'admin')
        created_elem.set('type', 'created')
        created_elem.text = term_data.get('created', datetime.now().isoformat())

        return term_entry

    def add_language_set(self, term_entry, lang, term_value, language_data=None):
        """Add langSet element for multilingual term representation."""
        lang_set = ET.SubElement(term_entry, 'langSet')
        lang_set.set('xml:lang', lang)

        # Term information group
        tig = ET.SubElement(lang_set, 'tig')

        # Term element
        term = ET.SubElement(tig, 'term')
        term.text = term_value

        # Term type (noun)
        term_type = ET.SubElement(tig, 'termNote')
        term_type.set('type', 'partOfSpeech')
        term_type.text = 'noun'

        # Grammatical gender for German
        if lang == 'de' and language_data and 'gender' in language_data:
            gender = ET.SubElement(tig, 'termNote')
            gender.set('type', 'grammaticalGender')
            gender.text = language_data['gender']

        return lang_set

    def generate_tbx(self, output_path):
        """Generate complete TBX document from term data."""
        root, header = self.create_tbx_root()
        text = ET.SubElement(root, 'text')
        body = ET.SubElement(text, 'body')

        term_count = 0
        for term_key, term_data in self.terms.items():
            # Create term entry
            term_entry = self.add_conceptual_entry(text, term_data)

            # Add English as primary language
            eng_value = term_data.get('term', term_data.get('name', ''))
            self.add_language_set(term_entry, 'en', eng_value)

            # Add other languages if available
            if term_key in self.multilingual:
                multilang_data = self.multilingual[term_key]

                if 'de' in multilang_data:
                    de_term = multilang_data['de'].get('term', '')
                    de_data = multilang_data['de']
                    self.add_language_set(term_entry, 'de', de_term, de_data)

                if 'zh' in multilang_data:
                    zh_term = multilang_data['zh'].get('term', '')
                    self.add_language_set(term_entry, 'zh', zh_term)

                if 'hi' in multilang_data:
                    hi_term = multilang_data['hi'].get('term', '')
                    self.add_language_set(term_entry, 'hi', hi_term)

                if 'ar' in multilang_data:
                    ar_term = multilang_data['ar'].get('term', '')
                    self.add_language_set(term_entry, 'ar', ar_term)

            body.append(term_entry)
            term_count += 1

        # Pretty print and write
        self._write_pretty_xml(root, output_path)
        print(f"Generated TBX document with {term_count} termEntry elements at {output_path}")
        return term_count

    def _write_pretty_xml(self, root, output_path):
        """Write XML with proper formatting and declaration."""
        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent='  ')

        # Remove extra blank lines and fix declaration
        lines = xml_str.split('\n')
        lines = [line for line in lines if line.strip()]

        # Ensure XML declaration
        if not lines[0].startswith('<?xml'):
            lines.insert(0, '<?xml version="1.0" encoding="UTF-8"?>')

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
            f.write('\n')


def main():
    """Command-line interface for TBX generation."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Convert AUGMANITAI terminology data to TBX-Core XML format'
    )
    parser.add_argument(
        'terms_json',
        help='Path to augmanitai/data/terms.json'
    )
    parser.add_argument(
        '-m', '--multilingual',
        help='Path to augmanitai_multilingual.json',
        default=None
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file path for TBX XML',
        default='augmanitai-tbx.xml'
    )

    args = parser.parse_args()

    generator = AugmanitaiTBXGenerator(args.terms_json, args.multilingual)
    generator.generate_tbx(args.output)
    print(f"TBX export completed: {args.output}")


if __name__ == '__main__':
    main()
