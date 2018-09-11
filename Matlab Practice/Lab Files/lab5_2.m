%% Histogram of Exam Grades

% Resets the workspace
clear;

% Load the 'examgrades.mat' file into the workspace
% Hint: actually write this in the script, not just in the command window
load('examgrades.mat');

% Use a histogram to plot the grades data
h = histogram(grades);

% Title the histogram as 'Exam Grade Distribution'
title('Exam Grade Distribution');
% Label the x-axis as 'Score'
xlabel('Score');
xlim([40 100]);
% Label the y-axis as 'Number of Students'
ylabel('Number of Students');

% The set() command below sets the fontsize of the text to 18
set(gca, 'fontsize', 18);


% Save the figure to the file 'lab5_2.png'
print('lab5_2.png', '-dpng');

