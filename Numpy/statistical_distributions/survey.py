# First, import numpy and matplotlib.
import numpy as np
from matplotlib import pyplot as plt


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos',
                    'Ceballos', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos',
                    'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos',
                    'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan',
                    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos',
                    'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan',
                    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

# At the top of script.py is a list of the different survey responses.
# Calculate the number of people who answered ‘Ceballos’ and save the answer to the variable total_ceballos.
# Print the variable to the terminal to see its value.

total_ceballos = survey_responses.count('Ceballos')
print(f'total_ceballos: {total_ceballos}')
print(f'count surveys: {len(survey_responses)}')

# Calculate the percentage of people in the survey who voted for Ceballos and save it to the variable
# percentage_ceballos.
# Print the variable to the terminal to see its value.

percentage_ceballos = total_ceballos/len(survey_responses)
print(f'percentage_ceballos: {percentage_ceballos}')

# In the real election, 54% of the 10,000 town population voted for Cynthia Ceballos. Your supervisors are
# concerned because this is a very different outcome than what the poll predicted. They want you to determine
# if there is something wrong with the poll or if given the sample size, it was an entirely reasonable result.
#
# Generate a binomial distribution that takes the number of total survey responses, the actual success rate,
# and the size of the town’s population as its parameters. Then divide the distribution by the number of survey
# responses. Save your calculation to the variable possible_surveys.

possible_surveys = np.random.binomial(len(survey_responses), .54, size=10000)/len(survey_responses)

# Plot a histogram of possible_surveys with a range of 0-1 and 20 bins.

plt.hist(possible_surveys, bins=20, range=(0, 1))
plt.show()

# As we saw, 47% of people we surveyed said they would vote for Ceballos, but 54% of people voted for Ceballos
# in the actual election.
# Calculate the percentage of surveys that could have an outcome of Ceballos receiving less than 50% of
# the vote and save it to the variable ceballos_loss_surveys.
# Print the variable to the terminal.

ceballos_loss_surveys = np.mean(possible_surveys < .5)
print(ceballos_loss_surveys)

# With this current poll, about 20% of the time a survey output would predict Kerrigan winning,
# even if Ceballos won the actual election.
# Your co-worker points out that your poll would be more accurate if it had more responders.
# Generate another binomial distribution, but this time, see what would happen if you had instead surveyed 7,000
# people. Divide the distribution by the size of the survey and save your findings to large_survey.

large_survey = np.random.binomial(7000, .54, size=10000) / 7000

# Now, recalculate the percentage of surveys that would have an outcome of Ceballos losing and save it to
# the variable ceballos_loss_new, and print the value to the terminal.
# What do we notice about this new value?
# What advice would you give to your supervisors about predicting results from surveys?

ceballos_loss_new = np.mean(large_survey < .5)
print(ceballos_loss_new)
