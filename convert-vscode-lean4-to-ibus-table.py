#!/usr/bin/python3
#
# Copyright (c) 2021 Mike FABIAN <mfabian@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
(DOCSTRING := '''
Converting abbreviations.json from the github.com/leanprover/vscode-lean4
repository to a ibus-table source file.
''')

import json

def parse_args() -> any:
    import argparse
    parser = argparse.ArgumentParser(description=DOCSTRING)
    parser.add_argument('-i', '--inputfilename',
                        nargs='?',
                        type=str,
                        default='abbreviations.json',
                        help='input file, default is %(default)s')
    parser.add_argument('-o', '--outputfilename',
                        nargs='?',
                        type=str,
                        default='lean.txt',
                        help='output file, default is %(default)s')
    return parser.parse_args()

HEAD = r'''### File header must not be modified
### This file must be encoded into UTF-8.
### This file comes from vscode-lean4's abbreviation table:
### <https://github.com/leanprover/vscode-lean4/raw/5a938adc7913fbb4e177391bc2b762a35ab29153/lean4-unicode-input/src/abbreviations.json>
SCIM_Generic_Table_Phrase_Library_TEXT
VERSION_1_0

### Begin Table definition.
BEGIN_DEFINITION

### An unique id to distinguish this table among others.
### Use uuidgen to generate this kind of id.
UUID = 3fa17a5a-7423-40fb-931e-1930e30e1657

### A unique number indicates the version of this file.
### For example the last modified date of this file.
### This number must be less than 2^32.
SERIAL_NUMBER = 20250522

### License
LICENSE = LGPL-2.1-or-later

ICON = lean.svg

### The symbol to be displayed in IM switchers
SYMBOL = ∀

### Prompt string to be displayed in the status area.
STATUS_PROMPT = ∀

### The default name of this table
NAME = Lean 4

### Description
DESCRIPTION = Use Lean abbreviations to enter mathematical symbols. All abbreviations start with a backslash (\).

### Author of this table
AUTHOR = Alba Mendez <me@alba.sh>

### Supported locales of this table
LANGUAGES = other

### If true then the phrases' frequencies will be adjusted dynamically.
DYNAMIC_ADJUST = TRUE

### If true then the preedit area will be filled up by the current candidate phrase automatically.

### Use full width punctuation by default
DEF_FULL_WIDTH_PUNCT = FALSE

### Use full width letter by default
DEF_FULL_WIDTH_LETTER = FALSE

### The maxmium length of a key.
MAX_KEY_LENGTH = 20

### Valid input chars.
### Since '=' is one of the VALID_INPUT_CHARS, we use '==' as delimiter
### so it is correctly picked up by the parser
VALID_INPUT_CHARS == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890^\_[] !"#&'()*+-./:=<>?|`{}~

### Start characters, every key in the table starts with one of these characters
START_CHARS = \

### Layout
### This table can be used with any layout capable of typing ASCII.
### Therefore, we should not require a special layout like “us”.
LAYOUT = default

### If true then a multi wildcard will be appended
### at the end of inputing string automatically.
AUTO_WILDCARD = TRUE

### Single wildcard char (leave empty if you don’t want a wildcard character).
SINGLE_WILDCARD_CHAR =

### Multi wildcard char (leave empty if you don’t want a wildcard character).
MULTI_WILDCARD_CHAR =

### Whether user are allow to define phrase, default is true
### You have to define the word construction rules below.
### For input methods which do not input phrases, set this to False
USER_CAN_DEFINE_PHRASE = FALSE

### Whether support PinYin Mode, default is true.
### this feature is just for Chinese, set it to False if your IM is not
### Chinese.
PINYIN_MODE = FALSE

### The key strokes to select candidiate phrases.
SELECT_KEYS = F1,F2,F3,F4,F5,F6,F7,F8,F9,F10

END_DEFINITION

### Begin Table data.
BEGIN_TABLE
'''

TAIL = '''\
END_TABLE
'''

def convert_vscode_lean4_to_ibus_table(
        inputfilename: str,
        outputfilename: str) -> None:
    '''
    Read VSCode Lean 4 abbreviations.json and write ibus-table .txt file
    '''
    t = json.load(open(inputfilename))
    with open(outputfilename, 'w') as outputfile:
        outputfile.write(HEAD)
        for k, v in t.items():
            outputfile.write(f'\\{k}\t{v}\t0\n')
        outputfile.write(TAIL)

def main() -> None:
    args = parse_args()
    convert_vscode_lean4_to_ibus_table(
        args.inputfilename,
        args.outputfilename)

if __name__ == '__main__':
    main()
