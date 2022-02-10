from mrjob.job import MRJob
from mrjob.step import MRStep
import csv


columns = 'Review,Rating'.split(',')
class NoRatings(MRJob):
	def steps(self):
		return[
			MRStep(mapper=self.mapper_get_ratings, 
			reducer=self.reducer_count_ratings)]

	def mapper_get_ratings(self, _, line):
		reader = csv.reader([line])
		for row in reader:
			zipped=zip(columns,row)
			diction=dict(zipped)
			ratings=diction['Rating']
			yield ratings, 1

	def reducer_count_ratings(self, key, values):
		yield key, sum(values)
if __name__ == "__main__":
	NoRatings.run()
