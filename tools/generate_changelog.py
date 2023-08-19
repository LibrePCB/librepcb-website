#!/usr/bin/env python

import argparse
import re
from subprocess import check_output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('repository', metavar='REPOSITORY', type=str,
                        help='File path to the LibrePCB repository')
    parser.add_argument('from_ref', metavar='FROM_REF', type=str,
                        help='Git ref of the previous release')
    parser.add_argument('to_ref', metavar='TO_REF', type=str,
                        help='Git ref of the next release')
    args = parser.parse_args()

    separator = '~~~~'
    output = check_output(
        ['git', '--no-pager', 'log', '--reverse', '--first-parent',
         '--format=' + separator + '%H%n%an (%ae)%n%B',
         args.from_ref + '..' + args.to_ref],
        cwd=args.repository).decode()
    commits = output.split(separator)
    authors = {}
    for commit in commits:
        if not commit.strip():
            continue
        lines = commit.splitlines()
        sha = lines[0].strip()
        author = lines[1].strip()
        body_lines = lines[2:]
        subject = re.sub('\\(#\\d+\\)', '', body_lines[0]).strip()
        match = re.match('.*\\(?#(\\d+)(\\)?).*', body_lines[0])
        number = match.group(1) if match else None
        is_simple = len(match.group(2)) if match else 1
        title = body_lines[2] if ((len(body_lines) > 2) and not is_simple) \
                              else subject
        authors[author] = authors.get(author, 0) + 1
        if number:
            text = '#{}'.format(number)
            url = 'https://github.com/LibrePCB/LibrePCB/pull/{}'.format(number)
        else:
            text = sha[:8]
            url = 'https://github.com/LibrePCB/LibrePCB/commit/{}'.format(sha)
        print('- ' + title)
        print('  ({url}[{text}])'.format(text=text, url=url))

    print('\nAuthors:')
    for name, count in authors.items():
        print('- [{}] {}'.format(count, name))
