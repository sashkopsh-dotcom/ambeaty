"""Проверка локальной статической страницы без внешних зависимостей."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.text = [], [], []
        self.images, self.headings = [], []
        self.lang = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'h1':
            self.headings.append(tag)
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

    def handle_data(self, value):
        self.text.append(value)


page = Page()
html = (DIST / 'index.html').read_text(encoding='utf-8')
page.feed(html)
assert page.lang == 'fr', 'HTML language must be French'
assert len(page.headings) == 1, 'Expected a single H1'
assert all(count == 1 for count in Counter(page.ids).values()), 'Duplicate IDs'
for target in page.links:
    parts = urlsplit(target)
    if parts.scheme:
        assert parts.scheme in ('https', 'mailto', 'tel'), target
        continue
    if target.startswith('#'):
        assert target[1:] in page.ids, f'Missing anchor: {target}'
    else:
        assert (DIST / unquote(parts.path)).is_file(), f'Missing asset: {target}'
for img in page.images:
    assert 'alt' in img and 'width' in img and 'height' in img, img
visible = ''.join(page.text)
assert not re.search('[А-Яа-яЁё]', visible), 'Russian text found in page'
assert not re.search(r'\b(TODO|TBD|Lorem ipsum|minceur|amincissement|amaigrissement)\b', visible, re.I), 'Draft or excluded weight-loss copy found'
assert 'https://wa.me/33629126645' in page.links
assert 'tel:+33629126645' in page.links
assert 'mailto:ambeautyconcept74@gmail.com' in page.links
for filename in ('confidentialite.html',):
    extra = Page()
    extra.feed((DIST / filename).read_text(encoding='utf-8'))
    assert extra.lang == 'fr' and len(extra.headings) == 1, filename
    assert not re.search('[А-Яа-яЁё]', ''.join(extra.text)), filename
    assert all(count == 1 for count in Counter(extra.ids).values()), filename
    for target in extra.links:
        parts = urlsplit(target)
        if parts.scheme:
            assert parts.scheme in ('https', 'mailto', 'tel'), target
        elif target.startswith('#'):
            assert target[1:] in extra.ids, target
        else:
            resource = DIST / unquote(parts.path)
            assert resource.is_file(), target
            if parts.fragment and resource.suffix == '.html':
                linked = Page()
                linked.feed(resource.read_text(encoding='utf-8'))
                assert parts.fragment in linked.ids, target
    for img in extra.images:
        assert all(key in img for key in ('alt', 'width', 'height')), img
import json
schema = json.loads(re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', html, re.S).group(1))
assert schema['@type'] == 'BeautySalon'
assert schema['name'] == 'AM Beauty Concept'
assert schema['telephone'] == '+33629126645'
assert schema['email'] == 'ambeautyconcept74@gmail.com'
assert schema['address'] == {'@type': 'PostalAddress', 'streetAddress': '36 Avenue Paul Béchet', 'postalCode': '74300', 'addressLocality': 'Cluses', 'addressCountry': 'FR'}
assert (DIST / 'assets/social-preview.jpg').is_file()
for document in ROOT.glob('*.md'):
    text = document.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if urlsplit(target).scheme or target.startswith('#'):
            continue
        assert (document.parent / unquote(target.split('#')[0])).exists(), (document.name, target)
print(f'OK: French HTML, {len(page.ids)} unique IDs, {len(page.links)} links/assets, {len(page.images)} images, project document links.')
