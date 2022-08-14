function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a 
%               vector containing labels between 1 to num_labels.
%
% Hint: The max function might come in useful. In particular, the max
%       function can also return the index of the max element, for more
%       information see 'help max'. If your examples are in rows, then, you
%       can use max(A, [], 2) to obtain the max for each row.
%



X = [ones(size(X,1),1) X];
z2 = X * Theta1';
a2 = sigmoid(z2);
 
a2 = [ones(size(a2,1),1) a2];
z3 = a2 * Theta2';
a3 = sigmoid(z3);
 
% 上面的计算方法与课程中的θx不同，因为下面max函数的需要，max是找出每一列中的最大值，所以上方的每一层的函数要变动一下，也就是把θx进行了转置，其中x在数据导入时已经是转置好的矩阵（x的行向量代表的是输入特征）
[c,b] = max(a3,[],2);
p = b;






% =========================================================================


end
