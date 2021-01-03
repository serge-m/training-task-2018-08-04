function [ H ] = est_homography(video_pts, logo_pts)
% est_homography estimates the homography to transform each of the
% video_pts into the logo_pts
% Inputs:
%     video_pts: a 4x2 matrix of corner points in the video
%     logo_pts: a 4x2 matrix of logo points that correspond to video_pts
% Outputs:
%     H: a 3x3 homography matrix such that logo_pts ~ H*video_pts

A = [video_pts(1,:)' video_pts(2,:)' video_pts(3,:)'; 1 1 1];
a = [video_pts(4,:)';1];
coeffs = A\a;
A = A .* coeffs';

B = [logo_pts(1,:)' logo_pts(2,:)' logo_pts(3,:)'; 1 1 1];
b = [logo_pts(4,:)';1];
coeffs = B\b;
B = B .* coeffs';

% for a check:
% z = B * inv(A) * [video_pts ones(4,1)]'; z ./ z(3, :)
H = B * inv(A);

end
