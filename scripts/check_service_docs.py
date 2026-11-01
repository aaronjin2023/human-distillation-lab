#!/usr/bin/env python3
"""Check documentation schemas and synthetic fixtures; no server or model is called.
Requires jsonschema >= 4 in the selected Python environment; installs nothing.
"""
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'docs/expert-service'


def check():
    spec = json.loads((BASE / 'openapi.json').read_text())
    examples = json.loads((BASE / 'examples.json').read_text())
    assert spec['openapi'] == '3.1.1'
    assert examples['status'] == 'synthetic-documentation-fixtures-not-runtime'
    # Resolve local references only; documentation checks never fetch external URLs.
    def walk(value):
        if isinstance(value, dict):
            if '$ref' in value:
                ref = value['$ref']
                assert ref.startswith('#/'), ref
                target = spec
                for part in ref[2:].split('/'):
                    target = target[part.replace('~1', '/').replace('~0', '~')]
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(spec)
    for schema in spec['components']['schemas'].values():
        Draft202012Validator.check_schema(schema)
    ids = []
    for path, methods in spec['paths'].items():
        for operation in methods.values():
            ids.append(operation['operationId'])
            parameters = [spec['components']['parameters'][p['$ref'].split('/')[-1]] for p in operation['parameters']]
            for parameter in parameters:
                if parameter['in'] == 'path':
                    assert '{' + parameter['name'] + '}' in path
            assert '500' in operation['responses'] and '410' in operation['responses']
    assert len(ids) == len(set(ids)) == 6
    for collection, expected in [('valid', True), ('invalid', False)]:
        for example in examples[collection]:
            schema = {'$ref': '#/components/schemas/' + example['schema'], 'components': spec['components']}
            validator = Draft202012Validator(schema, format_checker=FormatChecker())
            errors = list(validator.iter_errors(example['value']))
            assert (not errors) == expected, (example['name'], [e.message for e in errors])
    return {'status': 'passed', 'scope': 'JSON-Schema-and-synthetic-fixtures-only',
            'schemas': len(spec['components']['schemas']), 'operations': len(ids),
            'valid_examples': len(examples['valid']), 'rejected_examples': len(examples['invalid']),
            'runtime_tested': False, 'full_openapi_meta_schema_tested': False}


if __name__ == '__main__':
    print(json.dumps(check(), ensure_ascii=False))
