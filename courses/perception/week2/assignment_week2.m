function [ H ] = est_homography(video_pts, logo_pts)
H = [];

A = [];

for i = 1:4
    x=video_pts(i,:);
    x_=logo_pts(i,:);
    A = [A;
        -x(1) -x(2) -1 0 0 0 x(1)*x_(1) x(2)*x_(1) x_(1);
        0 0 0 -x(1) -x(2) -1 x(1)*x_(2) x(2) *x_(2) x_(2)
        ];
end

[U, S, V] = svd(A);
H = reshape(V(:, -1), [3,3]);

end
