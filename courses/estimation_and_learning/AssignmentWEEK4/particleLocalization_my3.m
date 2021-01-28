% Robotics: Estimation and Learning 
% WEEK 4
% 
% Complete this function following the instruction. 
function myPose = particleLocalization(ranges, scanAngles, map, param)

% Number of poses to calculate
N = size(ranges, 2);
% Output format is [x1 x2, ...; y1, y2, ...; z1, z2, ...]
myPose = zeros(3, N);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
% Map Parameters 
% 
% % the number of grids for 1 meter.
myResolution = param.resol;
% % the origin of the map in pixels
myOrigin = param.origin; 

% The initial pose is given
myPose(:,1) = param.init_pose;
% You should put the given initial pose into myPose for j=1, ignoring the j=1 ranges. 
% The pose(:,1) should be the pose when ranges(:,j) were measured.



% Decide the number of particles, M.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%M =                            % Please decide a reasonable number of M, 
                               % based on your experiment using the practice data.
%M = param.num_partices;
M = 500;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Create M number of particles
P = repmat(myPose(:,1), [1, M]);
P_next = zeros(size(P));

sigmas = [0.2 0.2 0.05]';
%sigmas = sigmas .* 10;
weights = ones([1 M]) / M;
weights_next = zeros(size(weights));
score = zeros([1 M]);
[h, w] = size(map);
K = size(scanAngles, 1);
    
    
for j = 2:N % You will start estimating myPose from j=2 using ranges(:,2).
    % 1) Propagate the particles 
    P_propagated = P + randn(size(P)) .* sigmas;
    % for debugging
    %P_propagated(:, 1) = param.pose_true(:, j);
      
    % 2) Measurement Update 
    %   2-1) Find grid cells hit by the rays (in the grid map coordinate frame)    
    score(:) = 0;
    for p_id=1:M
        p1 = P_propagated(:, p_id);
        p_on_map = [p1(1)*param.resol + param.origin(1); p1(2)*param.resol + param.origin(2)];
        p_on_map  = ceil(p_on_map );
       
        for k = 1:K
            theta = p1(3) + scanAngles(k);
            occu_ = p1(1:2) + ranges(k, j) * [cos(theta) -sin(theta)]';
            occu = ceil(myResolution*occu_) + myOrigin;
            
            occu(1) = min(max(1, occu(1)), w);
            occu(2) = min(max(1, occu(2)), h);
            hit = map(occu(2),occu(1));
            per_scan_score = -5*(hit<0.75) + 20*(hit>=0.75);
            score(p_id) = score(p_id) + per_scan_score;
        end
        
    end
    

    
    %score = (score - min_map) / (max_map - min_map);
    %   2-2) For each particle, calculate the correlation scores of the particles
    
    %   2-3) Update the particle weights         
    score = score - min(score(:));
    weights_new = weights .* score;
    %weights_new = weights_new - min(weights_new(:));
    weights_new = weights_new / sum(weights_new(:));
    
    [m_val, m_idx] = max(weights_new);
    myPose(:,j) = P_propagated(:, m_idx);
    %disp(sprintf("J %d m_val %f m_idx %f", j, m_val, m_idx))
    %disp(score(1,1))
    %disp(score(1,m_idx))
    
    effective_n = 1.0/sum(weights_new.^2);
    j
    effective_n
    
    weights_new_c = cumsum(weights_new);
    
    shift = ((1:M) -1) .* (1/M);
    probe = rand() * (1/M) + shift;
    p_id = 1;
    for probe_id=1:M
        while probe(probe_id) > weights_new_c(p_id)
            p_id = p_id + 1;
        end
        P_next(:, probe_id) = P_propagated(:, p_id);
        weights_next(:, probe_id) = weights_new(:, p_id);
    end
    
    P = P_next;
    weights = weights_next;
        
    
    %   2-4) Choose the best particle to update the pose
    
    
    
    % 3) Resample if the effective number of particles is smaller than a threshold

    % 4) Visualize the pose on the map as needed
   
    % The final grid map:
    if j > 20 && mod(j, 10) == 0
        if exist('f1','var')
            close(f1)
        end
        f1 = figure;
        imagesc(map); hold on;
        colormap('gray');
        axis equal;
    %     hold on;
    
        idx_to_plot = j;
        pose_to_plot = myPose(:, idx_to_plot);
        hitx = (ranges(:,idx_to_plot).*cos(scanAngles + pose_to_plot(3)) + pose_to_plot(1))*param.resol + param.origin(1);
        hity = (-ranges(:,idx_to_plot).*sin(scanAngles + pose_to_plot(3)) + pose_to_plot(2))*param.resol + param.origin(2);
        plot(hitx,hity, 'b.');
        
%         pose_to_plot = P_propagated(:, 1);
%         hitx = (ranges(:,1).*cos(scanAngles + pose_to_plot(3)) + pose_to_plot(1))*param.resol + param.origin(1);
%         hity = (-ranges(:,1).*sin(scanAngles + pose_to_plot(3)) + pose_to_plot(2))*param.resol + param.origin(2);
%         plot(hitx,hity, 'r.');
        
    
        plot(P_propagated(1, 1:1:end)*param.resol+param.origin(1), ...
             P_propagated(2, 1:1:end)*param.resol+param.origin(2), 'g.');
    
        
        plot(myPose(1,1)*param.resol+param.origin(1), ...
            myPose(2,1)*param.resol+param.origin(2), 'ro');
    
        
        plot(myPose(1,j)*param.resol+param.origin(1), ...
            myPose(2,j)*param.resol+param.origin(2), 'rx'); 
        
        saveas(f1,sprintf("vis_%05d.jpg", j));
    end
    

end

end

