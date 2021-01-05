function X = Nonlinear_Triangulation(K, C1, R1, C2, R2, C3, R3, x1, x2, x3, X0)
%% Nonlinear_Triangulation
% Refining the poses of the cameras to get a better estimate of the points
% 3D position
% Inputs: 
%     K - size (3 x 3) camera calibration (intrinsics) matrix
%     x
% Outputs: 
%     X - size (N x 3) matrix of refined point 3D locations 


N = size(x1, 1);
X = [];
for i=1:N
    Xi = Single_Point_Nonlinear_Triangulation(K, C1, R1, C2, R2, C3, R3, x1(i, :), x2(i, :), x3(i, :), X0(i, :));
    X = [X; Xi'];
end

end



function X = Single_Point_Nonlinear_Triangulation(K, C1, R1, C2, R2, C3, R3, x1, x2, x3, X0)
X_cur = X0;
while 1
    b = [x1 x2 x3]';
    uvw1 = K * R1 * (X_cur - C1);
    uvw2 = K * R2 * (X_cur - C2);
    uvw3 = K * R3 * (X_cur - C3);
    fX = [uvw1(1:2) ./ uvw1(3)  uvw2(1:2) ./ uvw2(3)  uvw3(1:2) ./ uvw3(3)]';
    J = [
        Jacobian_Triangulation(C1, R1, K, X_cur);
        Jacobian_Triangulation(C2, R2, K, X_cur);
        Jacobian_Triangulation(C3, R3, K, X_cur)
        ];
        
    delta_X = inv(J' * J) * J' * (b - fX);
%     if norm(delta_X) < 1e-3
%        break
%     end
    X_cur  = X_cur + delta_X;
    break;
end
X = X_cur;
end

function J = Jacobian_Triangulation(C, R, K, X)
     uvw = K * R * (X - C);
     u = uvw(1);
     v = uvw(2);
     w = uvw(3);
     t = K*R;
     du_dX = t(1, :);
     dv_dX = t(2, :);
     dw_dX = t(3, :);
     df_dX = [ (w * du_dX - u * dw_dX) / w^2; (w * dv_dX - v * dw_dX) / w^2 ];
     J = df_dX;
     
end
