function [C, R] = LinearPnP(X, x, K)
%% LinearPnP
% Getting pose from 2D-3D correspondences
% Inputs:
%     X - size (N x 3) matrix of 3D points
%     x - size (N x 2) matrix of 2D points whose rows correspond with X
%     K - size (3 x 3) camera calibration (intrinsics) matrix
% Outputs:
%     C - size (3 x 1) pose transation
%     R - size (3 x 1) pose rotation
%
% IMPORTANT NOTE: While theoretically you can use the x directly when solving
% for the P = [R t] matrix then use the K matrix to correct the error, this is
% more numeically unstable, and thus it is better to calibrate the x values
% before the computation of P then extract R and t directly


N = size(x, 1);
xh =  [x ones(N, 1)];

zero_1x4 = zeros([1,4]);
Kinv = inv(K);
X = [X ones([N, 1])];

A = [];
for i=1:N
    Xi = X(i, :);
    %uvi = Kinv_x(:, i);
    uvi = xh(i, :);
    Ai = skew(Kinv * uvi') * [Xi zero_1x4 zero_1x4; 
        zero_1x4 Xi zero_1x4; 
        zero_1x4 zero_1x4 Xi];
    A = [A; Ai];
end

[u, s, v] = svd(A);
sol = v(:, end);
P = reshape(sol, 4, 3)';

R_raw = P(:, 1:3);
[ru, rs, rv] = svd(R_raw);

t = P(:, 4)  / rs(1,1);
R = ru * rv';

if det(R) < 0
    R = -R;
    t = -t;
end

C = -R' * t;

% 
% N = size(x, 1);
% xh =  [x ones(N, 1)];
% Kinv_x = inv(K) * xh';
% 
% zero_1x4 = zeros([1,4]);
% 
% X = [X ones([N, 1])];
% 
% A = [];
% for i=1:N
%     Xi = X(i, :);
%     %uvi = Kinv_x(:, i);
%     uvi = xh(i, :);
%     Ai = skew(uvi) * [Xi zero_1x4 zero_1x4; 
%         zero_1x4 Xi zero_1x4; 
%         zero_1x4 zero_1x4 Xi];
%     A = [A; Ai];
% end
% 
% 
% [u, s, v] = svd(A);
% sol = v(:, end);
% P = reshape(sol, 4, 3)';
% 
% R_raw = inv(K) * P(:, 1:3);
% 
% [ru, rs, rv] = svd(R_raw);
% 
% R = ru * rv';
% t = P(:, 4) / rs(1,1);
% if det(R) < 0
%     R = -R;
%     t = -t;
% end
% 
% C = -R' * t;
% 
% 
% 
function s = skew(v)
s = [0 -v(3) v(2); v(3) 0 -v(1); -v(2) v(1) 0];
