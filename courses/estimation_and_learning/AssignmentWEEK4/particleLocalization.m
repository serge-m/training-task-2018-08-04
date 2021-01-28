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
M = param.num_partices;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Create M number of particles
P = repmat(myPose(:,1), [1, M]);
P_next = zeros(size(P));

sigmas = [0.1 0.1 0.1]';
%sigmas = sigmas .* 10;
weights = ones([1 M]) / M;
weights_next = zeros(size(weights));
min_map = min(map(:));
max_map = max(map(:));
for j = 2:N % You will start estimating myPose from j=2 using ranges(:,2).

    % 1) Propagate the particles
    P_propagated = P + randn(size(P)) .* sigmas;
    % for debugging
    %P_propagated(:, 1) = param.pose_true(:, j);

    % 2) Measurement Update
    %   2-1) Find grid cells hit by the rays (in the grid map coordinate frame)
    score = zeros([1 M]);
    for p_id=1:M
        p1 = P_propagated(:, p_id);
        p_on_map = [p1(1)*param.resol + param.origin(1); p1(2)*param.resol + param.origin(2)];
        p_on_map  = ceil(p_on_map );
        if map(p_on_map(2), p_on_map(1)) > 1
            score(p_id) = 0;
            continue;
        end
        hitx = ceil((ranges(:,j).*cos(scanAngles + p1(3)) + p1(1))*param.resol + param.origin(1));
        hity = ceil((-ranges(:,j).*sin(scanAngles + p1(3)) + p1(2))*param.resol + param.origin(2));

        in_range = 0 <= hitx & hitx <= size(map, 2) & 0 <= hity & hity <= size(map, 1);
        hitx = hitx(in_range);
        hity = hity(in_range);

        hit = map(hity, hitx);

        %score(p_id) = mean(hit(:));
        score(p_id) = (sum(hit>1,[1,2])) / size(ranges, 1);

    end

    %score = (score - min_map) / (max_map - min_map);
    %   2-2) For each particle, calculate the correlation scores of the particles
    %score = score / sum(score(:));
    %   2-3) Update the particle weights
    weights_new = weights .* score;
    weights_new = weights_new - min(weights_new(:));
    weights_new = weights_new / sum(weights_new(:));
    weights_new_c = cumsum(weights_new);

    shift = ((1:M) -1) .* (1/M);
    probe = rand() * (1/M) + shift;
    c = weights_new_c(1);
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

    [m_val, m_idx] = max(weights);
    myPose(:,j) = P(:, m_idx);
    %   2-4) Choose the best particle to update the pose



    % 3) Resample if the effective number of particles is smaller than a threshold

    % 4) Visualize the pose on the map as needed

    % The final grid map:
    if mod(j, 10) == 0
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

        pose_to_plot = P_propagated(:, 1);
        hitx = (ranges(:,1).*cos(scanAngles + pose_to_plot(3)) + pose_to_plot(1))*param.resol + param.origin(1);
        hity = (-ranges(:,1).*sin(scanAngles + pose_to_plot(3)) + pose_to_plot(2))*param.resol + param.origin(2);
        plot(hitx,hity, 'r.');


        plot(P(1, 1:10:end)*param.resol+param.origin(1), ...
             P(2, 1:10:end)*param.resol+param.origin(2), 'g.');


        plot(myPose(1,1)*param.resol+param.origin(1), ...
            myPose(2,1)*param.resol+param.origin(2), 'ro');


        plot(myPose(1,j)*param.resol+param.origin(1), ...
            myPose(2,j)*param.resol+param.origin(2), 'rx');


    end


end

end

