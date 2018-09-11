% 1. Load the image lab4_2.png
img = imread('lab4_2.png');
% imshow(img);

% 2. Extract the R, G, and B layers into variables
red = img(:, :, 1);
green = img(:, :, 2);
blue = img(:, :, 3);

% 3. Using logical arrays, if the R value is greater than 100, subtract 50
large_red = uint8((red > 100) * 50);
red = red - large_red;

% 4. Using logical arrays, if the G value is less than 150, add 100
small_green = uint8((green < 150) * 100);
green = green + small_green;

%{
img(:, :, 1) = red;
img(:, :, 2) = green;
imshow(img);
%}

% 5. Using logical arrays, if the B value is strictly between 50 and 100,
% 	 double the value
mid_blue = uint8((50 < blue & blue < 100) * 2);
blue = blue .* mid_blue;

% 6. Note that we have only changed red, green, and blue
%    and that our image 'img' has not changed.
%	 Copy the red, blue, and green layers back into 'im'
im = img(:, :, :);
im(:, :, 1) = red;
im(:, :, 2) = green;
im(:, :, 3) = blue;
% imshow(im);

% 7. Save the image as lab4_2.jpg
imwrite(im, 'lab4_2.jpg');
