import csv
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CustomerFeedbackScriptTests(unittest.TestCase):
    def test_script_generates_analyzed_csv(self):
        repo_dir = Path(__file__).resolve().parent

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            shutil.copy(repo_dir / "customer_feedback.py", temp_path / "customer_feedback.py")
            shutil.copy(repo_dir / "Customer_Data.csv", temp_path / "Customer_Data.csv")
            shutil.copy(repo_dir / "customer_feedback.csv", temp_path / "customer_feedback.csv")

            result = subprocess.run(
                [sys.executable, str(temp_path / "customer_feedback.py")],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)

            output_file = temp_path / "analyzed_customer_feedback.csv"
            self.assertTrue(output_file.exists())

            with output_file.open(newline="") as output_handle:
                rows = list(csv.DictReader(output_handle))

            self.assertEqual(len(rows), 20)
            self.assertIn("sentiment", rows[0])

            james_row = next(row for row in rows if row["name"] == "James")
            self.assertEqual(james_row["city"], "Houston")
            self.assertEqual(james_row["sentiment"], "Negative")


if __name__ == "__main__":
    unittest.main()
