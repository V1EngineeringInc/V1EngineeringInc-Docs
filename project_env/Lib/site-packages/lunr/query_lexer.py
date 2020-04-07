from __future__ import unicode_literals

import re

from lunr.tokenizer import SEPARATOR


class QueryLexer:
    # TODO: use iteration protocol?
    EOS = "EOS"
    FIELD = "FIELD"
    TERM = "TERM"
    EDIT_DISTANCE = "EDIT_DISTANCE"
    BOOST = "BOOST"
    TERM_SEPARATOR = SEPARATOR
    PRESENCE = "PRESENCE"

    def __init__(self, string):
        self.lexemes = []
        self.string = string
        self.length = len(string)
        self.pos = 0
        self.start = 0
        self.escape_char_positions = []

    @property
    def width(self):
        return self.pos - self.start

    def ignore(self):
        if self.start == self.pos:
            self.pos += 1

        self.start = self.pos

    def backup(self):
        self.pos -= 1

    def accept_digit_run(self):
        char = self.next()
        while char != self.EOS and (47 < ord(char) < 58):
            char = self.next()

        if char != self.EOS:
            self.backup()

    def run(self):
        state = self.lex_text()
        while state:
            state = state()

    def slice_string(self):
        subslices = []
        slice_start = self.start

        for escape_char_position in self.escape_char_positions:
            subslices.append(self.string[slice_start:escape_char_position])
            slice_start = escape_char_position + 1

        subslices.append(self.string[slice_start : self.pos])
        self.escape_char_positions = []

        return "".join(subslices)

    def next(self):
        if self.pos >= self.length:
            return self.EOS

        char = self.string[self.pos]
        self.pos += 1
        return char

    def emit(self, type_):
        self.lexemes.append(
            {
                "type": type_,
                "string": self.slice_string(),
                "start": self.start,
                "end": self.pos,
            }
        )
        self.start = self.pos

    def escape_character(self):
        self.escape_char_positions.append(self.pos - 1)
        self.pos += 1

    def lex_field(self):
        self.backup()
        self.emit(self.FIELD)
        self.ignore()
        return self.lex_text

    def lex_term(self):
        if self.width > 1:
            self.backup()
            self.emit(self.TERM)

        self.ignore()

        return self.lex_text

    def lex_edit_distance(self):
        self.ignore()
        self.accept_digit_run()
        self.emit(self.EDIT_DISTANCE)
        return self.lex_text

    def lex_boost(self):
        self.ignore()
        self.accept_digit_run()
        self.emit(self.BOOST)
        return self.lex_text

    def lex_EOS(self):
        if self.width > 0:
            self.emit(self.TERM)

    def lex_text(self):
        while True:
            char = self.next()
            if char == self.EOS:
                return self.lex_EOS

            if ord(char) == 92:  # Escape character is '\'
                self.escape_character()
                continue

            if char == ":":
                return self.lex_field

            if char == "~":
                self.backup()
                if self.width > 0:
                    self.emit(self.TERM)

                return self.lex_edit_distance

            if char == "^":
                self.backup()
                if self.width > 0:
                    self.emit(self.TERM)

                return self.lex_boost

            # '+' indicates term presence is required, check for length to
            # ensure only a leading '+' is considered
            if char == "+" and self.width == 1:
                self.emit(self.PRESENCE)
                return self.lex_text

            # '-' indicates term presence is prohibited
            if char == "-" and self.width == 1:
                self.emit(self.PRESENCE)
                return self.lex_text

            if re.match(self.TERM_SEPARATOR, char):
                return self.lex_term
