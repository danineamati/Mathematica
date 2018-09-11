%% Graph 1, US Gross National Product
% Load the lab5_1_GNP.csv data into MATLAB
% Hint: use csvread() to store the data in a variable
Yearly_GNP = csvread('lab5_1_GNP.csv');

% Store the fist column of the data in a variable called 'years'
years = Yearly_GNP(:,1);

% Store the second column of the data in a variable called 'GNP'
GNP = Yearly_GNP(:,2);

% Set the location of this graph as the top left corner of the figure
% Hint: use subplot()
figure();
subplot(2, 2, 1);

% Plot Graph 1 with years on the x-axis and GNP on the y-axis
plot(years, GNP);

% Title Graph 1 as 'US GNP, 1947-2005'
title('US GNP, 1947-2005');
% Label the x-axis as 'Year'
xlabel('Year');
% Label the y-axis as 'Billion Dollars (2000)'
ylabel('Billion Dollars (2000)');

%% Graph 2, Quadratic Function
% Create a vector, x1, with values from 0 to 10 with increments of 0.01
x1 = linspace(0, 10, 101);

% Create a vector, y1, with the same dimensions of x1, 
% where y1 is x1 squared
y1 = x1 .^ 2;

% Plot this graph in the top right corner of the figure
% Use your x variable for the x-axis and y variable as the y-axis
% Use a red line with circle markers when plotting
subplot(2, 2, 2);
p = plot(x1, y1, 'o', 'MarkerFaceColor', 'r');
p(1).Color = 'red';
%set(gca, 'XTick', (0:2:10));
%set(gca, 'YTick', (0:20:100));

% Title this graph as 'Graph of a Quadratic Function'
title('Graph of a Quadratic Function');
% Label the x-axis as 'x'
xlabel('x');
% Label the y-axis as 'y'
ylabel('y');


%% Graph 3, Square Root Function
% Create a vector, x2, of x values from 0 to 10 with increments of 0.01
% Create a vector, y2, of y values where y is the square root of x
x2 = linspace(0, 10, 101);
y2 = sqrt(x2);

% Plot this graph in the bottom left corner of the figure
% Use your x variable for the x-axis and y variable as the y-axis
% Use a green solid line when plotting
subplot(2, 2, 3);
p2 = plot(x2, y2);
p2(1).Color = 'green';

% Title this graph as 'Graph of a Square Root Function'
title('Graph of a Square Root Function');
% Label the x-axis as 'x'
xlabel('x');
%set(gca, 'XTick', (0:2:10));
% Label the y-axis as 'y'
ylabel('y');



%% Graph 4, Multiple Functions on One Plot!
% Plot the functions from Graph 2 and Graph 3 on the same plot
% Set the location of this graph as the bottom right corner of the figure
% Hint: use one plot() function
subplot(2, 2, 4);
p3 = plot(x1,y1,x2,y2);

% Set the x-axis bounds from 0 to 10 and the y-axis bounds from 0 to 5
xlim([0 10]);
ylim([0 5]);

% Title this graph as 'Graph of Two Functions'
title('Graph of Two Functions');
% Label the x-axis as 'x'
xlabel('x');
% Label the y-axis as 'y'
ylabel('y');

% Add a legend in the bottom right corner of the graph
% Label the functions as 'y = x^2' and 'y = sqrt(x)'
legend('y = x^2', 'y = sqrt(x)', 'Location', 'southeast');


%% Saving data as a CSV
% Place your y1 and y2 data in a matrix
% Ensure the matrix has two columns (instead of two rows)
% Hint: you may have to transpose your data
Mat(:, 1) = y1;
Mat(:, 2) = y2;

% Write the matrix to the file 'lab5_1.csv'
csvwrite('lab5_1.csv', Mat);


%% Saving data as a PNG
% Save the figure (with the four plots) to the file 'lab5_1.png'
% Hint: print(filename, filetype)
print('lab5_1.png', '-dpng');

