clc
A=imread('lena_color_256.tif');
[h,w,d]=size(A);
tform=maketform('affine',[-1 0 0; 0 1 0; w  0 1]);
%����ˮƽ����任����
tform2=maketform('affine',[1 0 0; 0 -1 0; h 0 1]);

B=imtransform(A, tform,'nearest');
C=imtransform(A, tform2,'nearest');

subplot(1,3,1);  imshow(A);  title('ԭͼ��');
subplot(1,3,2);  imshow(B);  title('ˮƽ����ͼ��');
subplot(1,3,3);  imshow(C);  title('��ֱ����ͼ��');