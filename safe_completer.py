# -*- coding: utf-8 -*-

# Import Completer Module for the prompt
from prompt_toolkit.completion import Completer, Completion, CompleteEvent
from prompt_toolkit.document import Document


# Import HTML for defining the prompt style
from prompt_toolkit import HTML

# Import Completer Constants defining the information of the commands withing the prompt
from safe_completer_constants import (
    safe_commands, safe_commands_arguments, safe_color_arguments, meta
)


class SafeCompleter(Completer):
    """ Command Completer
    This class will perform the utilities regarding auto-completion of known user input commands
    """
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Completion:
        """ Get Completions
        This will function will provide the completions for param types and function name
        :param document:
        :param complete_event:
        :return:
        """
        word = document.get_word_before_cursor()
        if document.find_previous_word_ending() is None:
            for _command in safe_commands:
                # note: force lower() to function as ignore_case.
                if _command.startswith(word.lower()):
                    if _command in safe_commands_arguments:
                        safe_command = safe_commands_arguments[_command]
                        safe_argument_color = safe_color_arguments.get(safe_command, 'default')
                        display = HTML('<b><ansired> &gt; </ansired>%s</b> <' + safe_argument_color + '>%s</'
                                       + safe_argument_color + '>') % (_command, safe_command)
                        yield Completion(_command, start_position=-len(word), display=display,
                                         display_meta=meta.get(_command))

