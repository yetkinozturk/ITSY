"""
Most of this code is taken right out of lodgit:
http://dev.pocoo.org/projects/lodgeit/
"""

import re

from django.utils.html import escape

def prepare_udiff(udiff):
    return DiffRenderer(udiff).prepare()

class DiffRenderer(object):
    _chunk_re = re.compile(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@')

    def __init__(self, udiff):
        self.lines = [escape(line) for line in udiff.splitlines()]

    def prepare(self):
        return self._parse_udiff()

    def _parse_udiff(self):
        info = self._parse_info()

        in_header = True
        header = []
        lineiter = iter(self.lines)
        files = []
        try:
            line = lineiter.next()
            while True:
                if not line.startswith('--- '):
                    if in_header:
                        header.append(line)
                    line = lineiter.next()
                    continue

                if header and all(o.strip() for o in header):
                    files.append({'is_header': True, 'lines': header})
                    header = []

                in_header = []
                chunks = []
                old, new = self._extract_rev(line, lineiter.next())
                files.append({
                    'is_header': False,
                    'old_filename': old[0],
                    'old_revision': old[1],
                    'new_filename': new[0],
                    'new_revision': new[1],
                    'chunks': chunks,
                })

                line = lineiter.next()
                while line:
                    match = self._chunk_re.match(line)
                    if not match:
                        in_header = False
                        break

                    lines = []
                    chunks.append(lines)

                    old_line, old_end, new_line, new_end = [int(o or 1) for o in match.groups()]
                    old_line -= 1
                    new_line -= 1
                    old_end += old_line
                    new_end += new_line
                    line = lineiter.next()

                    while old_line < old_end or new_line < new_end:
                        if line:
                            command, line = line[0], line[1:]
                        else:
                            command = ' '
                        affects_old = affects_new = False

                        if command == '+':
                            affects_new = True
                            action = 'add'
                        elif command == '-':
                            affects_old = True
                            action = 'del'
                        else:
                            affects_old = affects_new = True
                            action = 'unmod'

                        old_line += affects_old
                        new_line += affects_new
                        lines.append({
                            'old_lineno': affects_old and old_line or u'',
                            'new_lineno': affects_new and new_line or u'',
                            'action': action,
                            'line': line,
                        })
                        line = lineiter.next()
        except StopIteration:
            pass

        for file in files:
            if file['is_header']:
                continue
            for chunk in file['chunks']:
                lineiter = iter(chunk)
                first = True
                try:
                    while True:
                        line = lineiter.next()
                        if line['action'] != 'unmod':
                            nextline = lineiter.next()
                            if nextline['action'] == 'unmod' or nextline['action'] == line['action']:
                                continue
                            self._highlight_line(line, nextline)
                except StopIteration:
                    pass

        return files, info

    def _parse_info(self):
        nlines = len(self.lines)
        if not nlines:
            return
        firstline = self.lines[0]
        info = []

        # todo copy the HG stuff

        return info

    def _extract_rev(self, line1, line2):
        def _extract(line):
            parts = line.split(None, 1)
            return parts[0], (len(parts) == 2 and parts[1] or None)

        try:
            if line1.startswith('--- ') and line2.startswith('+++ '):
                return _extract(line1[4:]), _extract(line2[4:])
        except (ValueError, IndexError):
            pass
        return (None, None), (None, None)

    def _highlight_line(self, line, next):
        start = 0
        limit = min(len(line['line']), len(next['line']))
        while start < limit and line['line'][start] == next['line'][start]:
            start += 1
        end = -1
        limit -= start
        while -end <= limit and line['line'][end] == next['line'][end]:
            end -= 1
        end += 1
        if start or end:
            def do(l):
                last = end + len(l['line'])
                if l['action'] == 'add':
                    tag = 'ins'
                else:
                    tag = 'del'
                l['line'] = u'%s<%s>%s</%s>%s' % (
                    l['line'][:start],
                    tag,
                    l['line'][start:last],
                    tag,
                    l['line'][last:],
                )
            do(line)
            do(next)
