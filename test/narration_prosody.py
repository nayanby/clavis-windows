"""Clavis+ phrasing and pause parity without a model download."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'python_app'))
import listen


class ProsodyTests(unittest.TestCase):
    def test_heading_paragraph_and_sentence_pauses(self):
        plan = listen.speech_plan('Chapter IV\n\nIs this right?\n\nYes, it is.')
        self.assertEqual(plan, [('Chapter four', 1200), ('Is this right?', 900), ('Yes, it is.', 450)])
        self.assertEqual(listen.speech_plan('Introduction', headings=['Introduction']), [('Introduction', 1200)])

    def test_paragraph_boundary_outside_generated_chunk(self):
        self.assertEqual(listen.speech_plan('The paragraph ends.', paragraph_end=True)[0][1], 900)
        self.assertEqual(listen.speech_plan('The sentence ends.')[0][1], 450)

    def test_punctuation_is_preserved_for_neural_intonation(self):
        text = 'Doctor Smith asked: "Really?" It costs 1.50; wait, then continue!'
        self.assertEqual(listen.speech_plan(text), [(text, 450)])

    def test_pause_scaling_keeps_natural_silence_and_voice(self):
        class Engine:
            def __init__(self):
                self.calls = []

            def generate(self, text, sid, speed):
                self.calls.append((text, sid, speed))
                return type('Audio', (), {'samples': [.1] * 100 + [0.] * 100})()

        engine = Engine()
        output = listen.generate_phrased(engine, [('Chapter four', 1200), ('Read on.', 450)], 1000, 1, 0)
        self.assertEqual(len(output), 100 + 1200 + 100 + 450)
        self.assertEqual(engine.calls, [('Chapter four', 4, 1), ('Read on.', 4, 1)])
        fast = listen.generate_phrased(engine, [('Read on.', 450)], 1000, 2, 1)
        self.assertEqual(len(fast), 100 + 300)
        natural = listen.generate_phrased(engine, [('No added gap', 0)], 1000, 1, 1)
        self.assertEqual(len(natural), 200)

    def test_silent_model_output_is_rejected(self):
        engine = type('Engine', (), {'generate': lambda *args, **kwargs: type('Audio', (), {'samples': [0.] * 20})()})()
        with self.assertRaises(ValueError):
            listen.generate_phrased(engine, [('Hello.', 450)], 1000, 1, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
