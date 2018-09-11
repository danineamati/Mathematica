% Create a 800x1000 white matrix
img = ones(800, 1000) * 0.5;
% Create a black bar near the bottom of the image for the mouth
img(600:700, 200:800) = 0;
% Create each eye as a black box
img(100:500, 150:400) = 0;
img(100:500, 600:850) = 0;
% Create the glare of each eye
img(400:500, 300:400) = 1;
img(400:500, 750:850) = 1;

% Display the matrix as an image
imshow(img);