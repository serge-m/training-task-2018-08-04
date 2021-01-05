function F = EstimateFundamentalMatrix(x1, x2)
%% EstimateFundamentalMatrix
% Estimate the fundamental matrix from two image point correspondences 
% Inputs:
%     x1 - size (N x 2) matrix of points in image 1
%     x2 - size (N x 2) matrix of points in image 2, each row corresponding
%       to x1
% Output:
%    F - size (3 x 3) fundamental matrix with rank 2


u1 = x1(:, 1);
v1 = x1(:, 2);

u2 = x2(:, 1);
v2 = x2(:, 2);


A = [u1 .* u2, u1 .* v2, u1, v1.*u2, v1.*v2, v1, u1, v2, ones(size(u1))];

[ua, sa, va] = svd(A);

x = va(:, 9);

F = reshape(x, 3,3);

[uf, sf, vf] = svd(F);



sf(3,3) = 0;
%sf  = sf ./ (sf(1,1) * sf(2,2)) ^0.5;

F = uf * sf * vf';


