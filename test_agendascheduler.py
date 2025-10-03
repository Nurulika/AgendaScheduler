# test_agendascheduler.py
"""
Tests for AgendaScheduler module.
"""

import unittest
from agendascheduler import AgendaScheduler

class TestAgendaScheduler(unittest.TestCase):
    """Test cases for AgendaScheduler class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgendaScheduler()
        self.assertIsInstance(instance, AgendaScheduler)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgendaScheduler()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
