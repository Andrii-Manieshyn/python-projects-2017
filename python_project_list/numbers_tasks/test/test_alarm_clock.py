from nose.tools import assert_equal
from parameterized import parameterized

import unittest
from  unittest.mock import Mock, call
from  unittest.mock import MagicMock

import pygame
from numbers_tasks.src.alarm_clock import *

class AlarmClock(unittest.TestCase):

    def setUp(self):
        pygame.init = Mock()
        pygame.mixer.init = Mock()
        pygame.display.set_mode = Mock()
        pygame.mixer.music.load = Mock()
        pygame.mixer.music.play = Mock()
        pygame.time.Clock = Mock()
        pygame.event.poll = Mock()

        pygame.mixer.music.get_busy = MagicMock(side_effect=[True, True, False])

        pygame.mixer.music.stop = Mock()
        pygame.display.quit = Mock()
        global calls
        calls = [call(), call()]

    def test_play_sound(self):
        play_sound()
        pygame_called()



def pygame_called():
    pygame.init.assert_called_once()
    pygame.mixer.init.assert_called_once()
    pygame.display.set_mode.assert_called_once()
    pygame.event.poll.assert_has_calls(calls)

