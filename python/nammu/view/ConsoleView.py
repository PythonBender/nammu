'''
Copyright 2015, 2016 University College London.

This file is part of Nammu.

Nammu is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Nammu is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Nammu.  If not, see <http://www.gnu.org/licenses/>.
'''

from java.awt import Font, BorderLayout, Color, Dimension
from javax.swing import JTextArea, JScrollPane, JPanel, BorderFactory
from javax.swing.text import DefaultCaret


class ConsoleView(JPanel):
    '''
    Initializes the console view and sets its layout.
    '''
    def __init__(self, controller):
        '''
        Creates default empty console-looking panel.
        It should be separated from the rest of the GUI so that users can
        choose to show or hide the console. Or should it be a split panel?
        This panel will display log and validation/lemmatization messages.
        It might need its own toolbar for searching, etc.
        It will also accept commands in later stages of development, if need
        be.
        '''
        # Give reference to controller to delegate action response
        self.controller = controller

        # Make text area occupy all available space and resize with parent
        # window
        self.setLayout(BorderLayout())

        # Create console-looking area
        self.edit_area = JTextArea()
        self.edit_area.setLineWrap(True)
        self.edit_area.setWrapStyleWord(True)
        self.edit_area.border = BorderFactory.createEmptyBorder(4, 4, 4, 4)
        self.edit_area.font = Font("Courier New", Font.BOLD, 14)
        self.edit_area.background = Color.BLACK
        self.edit_area.foreground = Color.WHITE

        # Disable writing in the console
        self.edit_area.setEditable(False)

        # Will need scrolling controls
        scrollingText = JScrollPane(self.edit_area)
        scrollingText.setPreferredSize(Dimension(1, 150))

        # Make text area auto scroll down to last printed line
        caret = self.edit_area.getCaret()
        caret.setUpdatePolicy(DefaultCaret.ALWAYS_UPDATE)

        # Add to parent panel
        self.add(scrollingText, BorderLayout.CENTER)

    def scroll(self):
        '''
        Scroll down to bottom.
        '''
        length = self.edit_area.getDocument().getLength()
        self.edit_area.setCaretPosition(length)
