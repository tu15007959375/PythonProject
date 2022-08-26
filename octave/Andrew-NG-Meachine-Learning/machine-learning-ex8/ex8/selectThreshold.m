function [bestEpsilon bestF1] = selectThreshold(yval, pval)
%SELECTTHRESHOLD Find the best threshold (epsilon) to use for selecting
%outliers
%   [bestEpsilon bestF1] = SELECTTHRESHOLD(yval, pval) finds the best
%   threshold to use for selecting outliers based on the results from a
%   validation set (pval) and the ground truth (yval).
%

bestEpsilon = 0;
bestF1 = 0;
F1 = 0;

stepsize = (max(pval) - min(pval)) / 1000;
for epsilon = min(pval):stepsize:max(pval)
    
    % ====================== YOUR CODE HERE ======================
    % Instructions: Compute the F1 score of choosing epsilon as the
    %               threshold and place the value in F1. The code at the
    %               end of the loop will compare the F1 score for this
    %               choice of epsilon and set it to be the best epsilon if
    %               it is better than the current choice of epsilon.
    %               
    % Note: You can use predictions = (pval < epsilon) to get a binary vector
    %       of 0's and 1's of the outlier predictions








    % 求出阈值为epsilon时的预测情况，pval值小于epsilon的点是异常点
    % predictions是一个01列向量
    predictions = (pval < epsilon);
    % 下求F-score
    % 求true positive值
    tp = sum( (predictions == 1) & (yval == 1) );
    % 求false positive值
    fp = sum( (predictions == 1) & (yval == 0) );
    % 求false negative值
    fn = sum( (predictions == 0) & (yval == 1) );
    % 求精准率（precision）
    prec = tp / ( tp + fp );
    % 求召回率（recall）
    rec = tp / ( tp + fn );
    % 最后求F-score
    F1 = 2 * prec * rec / ( prec + rec);
    % F-score越大越好
    % 若当前epsilon对应的F-score更大，则该epsilon是更好的epsilon值





    % =============================================================

    if F1 > bestF1
       bestF1 = F1;
       bestEpsilon = epsilon;
    end
end

end
