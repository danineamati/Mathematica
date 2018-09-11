% Read the image from the file
img = imread('evil.jpg');

% Converts from RGB to HSV (hue, value, saturation)
hsv = rgb2hsv(img);

% Fixes the image with our function
outImg = lab3_1_recolor(hsv);

% Converts from HSV to RGB
rgb_img = hsv2rgb(outImg);

% Displays the image
imshow(rgb_img);

%imshow(img);
