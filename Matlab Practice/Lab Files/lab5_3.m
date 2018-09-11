%% Contour Mapping
% Define x as an evenly spaced vector from -pi to pi with 100 values
x = linspace(-pi, pi, 101);

% Define y as an evenly spaced vector from -2*pi to 2*pi with 100 values
y = linspace(-2*pi, 2*pi, 101);

% Try running your script. Notice that an error occurs, indicating that the
% contour function REQUIRES THREE input arguments.
% Comment out the below line before continuing.
% contour(x, y);

% We will now create our third dimension
% NOTE:
% When creating the z dimension, we have to map every pair of x
% and y values to a z value.
% Consider the function z = x + y for
%       x = 0 1 2
%       y = 2 4 6
%
% Then we need a z value for
%       x = 0 and y = 2
%       x = 0 and y = 4
%       x = 0 and y = 6
%       x = 1 and y = 2
%       ... (etc.)
%
% It is not simply enough to say z = x + y
% We need x and y to be matrices (so that we have all pairs of x and y)
%       X = 0 1 2       Y = 2 2 2
%           0 1 2           4 4 4
%           0 1 2           6 6 6
%
% Thus Z(1) = X(1) + Y(1) gives the correct z value when x = 0 and y = 2
% And  Z(2) = X(2) + Y(2) gives the correct z value when x = 0 and y = 4
% And  Z(3) = X(3) + Y(3) gives the correct z value when x = 0 and y = 6
% And  Z(4) = X(4) + Y(4) gives the correct z value when x = 1 and y = 2
% ... (etc.)
%
% The meshgrid() command below creates the matrices X and Y.
% X will have copies of x in it's rows
% Y will have copies of y in it's columns
[X, Y] = meshgrid(x, y);

% Define Z as sin(X) + sin(Y)
Z = sin(X) + sin(Y);

% Plot a FILLED contour map of X, Y, and Z
contourf(X, Y, Z);

% Set the colormap as 'autumn'
colormap('autumn');

% Place the colorbar on the right of the figure outside of the graph
colorbar('eastoutside');

% Save the figure to the file 'lab5_3.png'
print('lab5_3.png', '-dpng');
