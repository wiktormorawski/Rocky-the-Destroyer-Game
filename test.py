from funkcje import *
import unittest

def test_add_enemy():
    assert number_enemy_add(6, 2) == 8


def test_level():
    assert level(27) == 2


def test_collision():
    assert collision(1, 1, 1, 1) == True


def test_highscore():
    assert highscore(-1) == False


def test_enemy_tables():

    assert creating_enemies_tables(0) == None



