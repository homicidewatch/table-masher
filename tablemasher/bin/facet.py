#!/usr/bin/env python
# encoding: utf-8
"""
Facet a big CSV into lots more smaller ones
"""
import sys
import os

from table_fu import TableFu

def facet(starter, *facets):
    table = TableFu.from_file(starter)
    out_dir = os.path.dirname(starter)
    files = []
    for f in facets:
        try:
            tables = table.facet_by(f)
        except KeyError:
            sys.stderr.write('Bad column name: %s\n' % f)
            sys.stderr.write('Available columns: %s\n\n' % ', '.join(table.columns))
            continue

        for t in tables:
            out = open(os.path.join(out_dir, '%s.csv' % t.faceted_on), 'wb')
            out.write(t.csv().getvalue())
            out.close()
            files.append(out.name)
    
    return files

def main():
    if not sys.argv[1:]:
        sys.stderr.write("There's no point in faceting if you don't have something to facet on\n")
        sys.exit(0)
	
    files = facet(sys.argv[1], *sys.argv[2:])
    for f in files:
        print("New file: %s" % f)


if __name__ == '__main__':
	main()

