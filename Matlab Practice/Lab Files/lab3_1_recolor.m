function [ outputImg ] = lab3_1_recolor(hsvImg)
% This function takes an hsv image.
% An image is composed of 3 matrices (hue, saturation, and value).
% This function fixes the red/green colors of the OSU algorithm.
% The corrected image is assigned into outputImg.

    % Obtains the hue and saturation layers from the matrix
    % An image has 3D dimensions, which is why we use hsvImg(:, :, layer)
    hue = hsvImg(:, :, 1);
    sat = hsvImg(:, :, 2);
    
    % Fix the green and make it blue
    hue(0.25 < hue & hue < 0.35) = hue(0.25 < hue & hue < 0.35) .* 2;

    % Replace the red with yellow
    hue(0.2 > hue) = 0.15;

    % Increase saturation by a multiplier of 1.2 to make colors more vivid
    sat(:, :) = sat(:, :) .* 1.2;
    
    % We modified hue and sat
    % We need to copy these back into hsvImg!
    hsvImg(:, :, 1) = hue;
    hsvImg(:, :, 2) = sat;
    
    % Copy everything to the output image
    outputImg = hsvImg(:, :, :);

end