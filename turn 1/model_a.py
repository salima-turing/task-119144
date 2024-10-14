import unittest
import time
from data_breach_response import detect_breach, respond_to_breach

class TestDataBreachResponse(unittest.TestCase):

	def test_breach_detection_time(self):
		# Benchmarked target: Detection time should be less than 1 second
		start_time = time.time()
		is_breach = detect_breach(self.sample_data)
		end_time = time.time()
		detection_time = end_time - start_time

		self.assertLess(detection_time, 1.0, "Breach detection time exceeded benchmark")
		print(f"Breach Detection Time: {detection_time:.2f} seconds")

	def test_response_time(self):
		# Benchmarked target: Response time should be less than 5 seconds
		if detect_breach(self.sample_data):
			start_time = time.time()
			respond_to_breach()
			end_time = time.time()
			response_time = end_time - start_time
			self.assertLess(response_time, 5.0, "Response time exceeded benchmark")
			print(f"Response Time: {response_time:.2f} seconds")
		else:
			print("Breach not detected.")

if __name__ == '__main__':
	unittest.main()
