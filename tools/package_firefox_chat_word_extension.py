"""Build a Firefox-compatible package from the shared Pearls extension runtime."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json
import re
import package_chat_word_extension as chrome_package


def main():
    chrome_package.main()
    output = chrome_package.OUTPUT / 'firefox'
    output.mkdir(parents=True, exist_ok=True)
    folder = output / 'Pearls Chat to Word'
    folder.mkdir(exist_ok=True)
    with ZipFile(chrome_package.OUTPUT / 'Pearls Chat to Word.zip') as source:
        for name in source.namelist():
            relative = Path(name).relative_to('Pearls Chat to Word')
            target = folder / relative
            assert target.resolve().is_relative_to(folder.resolve())
            target.parent.mkdir(parents=True, exist_ok=True)
            data = source.read(name)
            if relative.as_posix() == 'manifest.json':
                manifest = json.loads(data)
                manifest['background'] = {'scripts': ['background.js']}
                manifest['browser_specific_settings'] = {'gecko': {
                    'id': 'pearls-chat-word@pearls.local',
                    'strict_min_version': '128.0',
                    'data_collection_permissions': {'required': ['none']},
                }}
                data = json.dumps(manifest, indent=2).encode('utf-8')
            # Firefox exposes Promise-based WebExtension methods on browser.
            # Keep the shared runtime intact and bind its API name in this build.
            if relative.suffix == '.js' and relative.parent == Path('.'):
                data = re.sub(rb'\bchrome\.', b'browser.', data)
            target.write_bytes(data)
    archive = output / 'Pearls Chat to Word Firefox.xpi'
    with ZipFile(archive, 'w', ZIP_DEFLATED) as package:
        for file in sorted(folder.rglob('*')):
            if file.is_file():
                package.write(file, file.relative_to(folder).as_posix())
    print(folder / 'manifest.json')
    print(archive)


if __name__ == '__main__':
    main()
